#!/usr/bin/env python3
"""Update local Mini Program API Markdown files from official API pages.

The script keeps the local API directory structure, fetches each official
page's document body, and converts the reference content into Markdown.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import os
from pathlib import Path
import re
import sys
import threading
from typing import Iterable
from urllib.parse import unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup, NavigableString, Tag


ROOT = Path(__file__).resolve().parents[1]
API_ROOT = ROOT / "miniprogram-docs" / "小程序API"
OFFICIAL_BASE = "https://developers.weixin.qq.com"
TODAY = "2026-06-01"

OFFICIAL_LINE_RE = re.compile(r"^> 官方文档：(.+)$", re.MULTILINE)
OFFICIAL_URL_RE = re.compile(r"https://developers\.weixin\.qq\.com/[^\s)]+")
CATEGORY_RE = re.compile(r"> 所属分类：(\[[^\]]+\]\([^)]+\))")
NAV_RE = re.compile(r"> 导航路径：(.+)")

thread_state = threading.local()


def session() -> requests.Session:
    if not hasattr(thread_state, "session"):
        s = requests.Session()
        s.headers.update(
            {
                "User-Agent": "wechat-miniprogram-docs-updater/1.0",
                "Accept": "text/html,application/xhtml+xml",
            }
        )
        thread_state.session = s
    return thread_state.session


def markdown_files() -> list[Path]:
    files = []
    for path in API_ROOT.rglob("*.md"):
        if path.name == "API目录.md" or path.name.endswith("目录.md"):
            continue
        files.append(path)
    return sorted(files)


def parse_existing(path: Path) -> tuple[str, str, str]:
    text = path.read_text(encoding="utf-8")
    official_line = OFFICIAL_LINE_RE.search(text)
    official = OFFICIAL_URL_RE.search(official_line.group(1) if official_line else text)
    if not official:
        raise ValueError("missing official URL")
    category = CATEGORY_RE.search(text)
    nav = NAV_RE.search(text)
    return official.group(0), category.group(1) if category else "", nav.group(1).strip() if nav else ""


def build_url_map(paths: Iterable[Path]) -> dict[str, Path]:
    mapping: dict[str, Path] = {}
    for path in paths:
        try:
            url, _, _ = parse_existing(path)
        except ValueError:
            continue
        mapping[normalize_official_url(url)] = path
    return mapping


def normalize_official_url(url: str) -> str:
    parsed = urlparse(url)
    clean = parsed._replace(fragment="", query="").geturl()
    if clean.endswith("/"):
        clean = clean[:-1]
    return clean


def cache_path(cache_dir: Path, url: str) -> Path:
    return cache_dir / (hashlib.sha1(url.encode("utf-8")).hexdigest() + ".html")


def fetch_html(url: str, cache_dir: Path, refresh: bool) -> str:
    cache_dir.mkdir(parents=True, exist_ok=True)
    target = cache_path(cache_dir, url)
    if target.exists() and not refresh:
        return target.read_text(encoding="utf-8")
    response = session().get(url, timeout=25)
    response.raise_for_status()
    response.encoding = response.encoding or "utf-8"
    html = response.text
    target.write_text(html, encoding="utf-8")
    return html


def clean_text(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def plain_text(node) -> str:
    if node is None:
        return ""
    clone = BeautifulSoup(str(node), "html.parser")
    for anchor in clone.select("a.header-anchor"):
        anchor.decompose()
    return clean_text(clone.get_text(" ", strip=True)).lstrip("#").strip()


def inline_text(node, page_url: str, current_path: Path, url_map: dict[str, Path]) -> str:
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""

    if node.name == "br":
        return "\n"
    if node.name == "code":
        return "`" + node.get_text("", strip=True).replace("`", "\\`") + "`"
    if node.name in {"strong", "b"}:
        text = clean_text("".join(inline_text(c, page_url, current_path, url_map) for c in node.children))
        return f"**{text}**" if text else ""
    if node.name in {"em", "i"} and "toggle-children-table" not in node.get("class", []):
        text = clean_text("".join(inline_text(c, page_url, current_path, url_map) for c in node.children))
        return f"*{text}*" if text else ""
    if node.name == "a":
        if "header-anchor" in node.get("class", []):
            return ""
        text = clean_text("".join(inline_text(c, page_url, current_path, url_map) for c in node.children))
        href = node.get("href")
        if not href:
            return text
        mapped = map_link(href, page_url, current_path, url_map)
        return f"[{text}]({mapped})" if text and mapped else text

    return "".join(inline_text(c, page_url, current_path, url_map) for c in node.children)


def map_link(href: str, page_url: str, current_path: Path, url_map: dict[str, Path]) -> str:
    if href.startswith("#"):
        return href
    absolute = urljoin(page_url, href)
    parsed = urlparse(absolute)
    if parsed.netloc == "developers.weixin.qq.com":
        normalized = normalize_official_url(absolute)
        local = url_map.get(normalized)
        if local:
            return os.path.relpath(local, current_path.parent)
    return absolute


def escape_table_cell(value: str) -> str:
    value = clean_text(value)
    value = value.replace("|", "\\|")
    value = value.replace("\n", "<br>")
    return value or " "


def direct_children(parent: Tag, names: set[str]) -> list[Tag]:
    return [c for c in parent.children if isinstance(c, Tag) and c.name in names]


def table_rows(section: Tag | None) -> list[list[Tag]]:
    if section is None:
        return []
    rows = []
    for tr in direct_children(section, {"tr"}):
        rows.append(direct_children(tr, {"th", "td"}))
    return rows


def cell_text(cell: Tag, page_url: str, current_path: Path, url_map: dict[str, Path]) -> str:
    clone = BeautifulSoup(str(cell), "html.parser")
    for nested in clone.find_all("table"):
        nested.decompose()
    return inline_text(clone, page_url, current_path, url_map)


def convert_table(table: Tag, page_url: str, current_path: Path, url_map: dict[str, Path]) -> list[str]:
    lines: list[str] = []
    thead = table.find("thead", recursive=False)
    tbody = table.find("tbody", recursive=False)
    header_cells = table_rows(thead)
    body_rows = table_rows(tbody)

    headers = [cell_text(c, page_url, current_path, url_map) for c in header_cells[0]] if header_cells else []
    rows: list[list[str]] = []
    nested_tables: list[Tag] = []
    for cells in body_rows:
        if any(c.find("table") for c in cells):
            nested_tables.extend(c.find("table") for c in cells if c.find("table"))
            clean_cells = [cell_text(c, page_url, current_path, url_map) for c in cells]
            if any(clean_text(c) for c in clean_cells):
                rows.append(clean_cells)
            continue
        rows.append([cell_text(c, page_url, current_path, url_map) for c in cells])

    if not headers and rows:
        headers = [f"列 {i + 1}" for i in range(max(len(r) for r in rows))]

    if headers and headers[0].strip() == "" and all((not r or r[0].strip() == "") for r in rows):
        headers = headers[1:]
        rows = [r[1:] for r in rows]

    if headers:
        width = len(headers)
        normalized_rows = [(r + [""] * width)[:width] for r in rows]
        lines.append("| " + " | ".join(escape_table_cell(h) for h in headers) + " |")
        lines.append("| " + " | ".join("---" for _ in headers) + " |")
        for row in normalized_rows:
            lines.append("| " + " | ".join(escape_table_cell(c) for c in row) + " |")

    for nested in nested_tables:
        nested_md = convert_table(nested, page_url, current_path, url_map)
        if nested_md:
            if lines:
                lines.append("")
            lines.append("补充表：")
            lines.extend(nested_md)

    return lines


def convert_list(list_node: Tag, page_url: str, current_path: Path, url_map: dict[str, Path], ordered: bool) -> list[str]:
    lines = []
    index = 1
    for li in direct_children(list_node, {"li"}):
        nested = [c for c in li.children if isinstance(c, Tag) and c.name in {"ul", "ol"}]
        for n in nested:
            n.extract()
        text = clean_text(inline_text(li, page_url, current_path, url_map))
        prefix = f"{index}. " if ordered else "- "
        if text:
            lines.append(prefix + text)
        for n in nested:
            for sub in convert_list(n, page_url, current_path, url_map, n.name == "ol"):
                lines.append("  " + sub)
        index += 1
    return lines


def convert_block(node: Tag, page_url: str, current_path: Path, url_map: dict[str, Path]) -> list[str]:
    name = node.name
    if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        level = int(name[1])
        text = plain_text(node)
        return [f"{'#' * level} {text}"] if text else []
    if name == "p":
        text = clean_text(inline_text(node, page_url, current_path, url_map))
        return [text] if text else []
    if name == "blockquote":
        lines = []
        for child in node.children:
            if isinstance(child, Tag):
                for line in convert_block(child, page_url, current_path, url_map):
                    lines.append("> " + line)
        return lines
    if name in {"ul", "ol"}:
        return convert_list(node, page_url, current_path, url_map, name == "ol")
    if name == "pre":
        code = node.get_text("", strip=False).strip("\n")
        lang = ""
        classes = node.get("class", [])
        for cls in classes:
            if cls.startswith("language-"):
                lang = cls.split("-", 1)[1]
        return [f"```{lang}", code, "```"]
    if name == "table":
        return convert_table(node, page_url, current_path, url_map)
    if name == "div":
        if node.find("pre", recursive=False):
            result: list[str] = []
            for child in node.children:
                if isinstance(child, Tag):
                    result.extend(convert_block(child, page_url, current_path, url_map))
            return result
        if "table-wrp" in node.get("class", []):
            table = node.find("table", recursive=False)
            return convert_table(table, page_url, current_path, url_map) if table else []
        result = []
        for child in node.children:
            if isinstance(child, Tag):
                result.extend(convert_block(child, page_url, current_path, url_map))
                if result and result[-1] != "":
                    result.append("")
        while result and result[-1] == "":
            result.pop()
        return result
    return [clean_text(inline_text(node, page_url, current_path, url_map))]


def official_body_to_markdown(html: str, page_url: str, current_path: Path, url_map: dict[str, Path]) -> tuple[str, list[str]]:
    soup = BeautifulSoup(html, "html.parser")
    content = soup.select_one("main .content.custom") or soup.select_one("main")
    if content is None:
        raise ValueError("missing official content")
    title_node = content.find("h1", recursive=False) or content.find("h1")
    title = plain_text(title_node) if title_node else current_path.stem

    lines: list[str] = []
    for child in content.children:
        if not isinstance(child, Tag):
            continue
        if child is title_node:
            continue
        block = convert_block(child, page_url, current_path, url_map)
        if not block:
            continue
        if lines and lines[-1] != "":
            lines.append("")
        lines.extend(block)
    while lines and lines[-1] == "":
        lines.pop()
    return title, lines


def render_file(path: Path, official_url: str, category: str, nav: str, title: str, body_lines: list[str]) -> str:
    lines = [
        f"# {title}",
        "",
        f"> 官方文档：[{title}]({official_url})",
    ]
    if category:
        lines.append(f"> 所属分类：{category}")
    if nav:
        lines.append(f"> 导航路径：{nav}")
    lines.extend(
        [
            f"> 整理日期：{TODAY}",
            "> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。",
            "",
        ]
    )
    lines.extend(body_lines)
    lines.append("")
    return "\n".join(lines)


def update_one(args) -> tuple[Path, bool, str]:
    path, cache_dir, refresh, url_map = args
    try:
        official_url, category, nav = parse_existing(path)
        html = fetch_html(official_url, cache_dir, refresh)
        title, body_lines = official_body_to_markdown(html, official_url, path, url_map)
        new_text = render_file(path, official_url, category, nav, title, body_lines)
        old_text = path.read_text(encoding="utf-8")
        if old_text != new_text:
            path.write_text(new_text, encoding="utf-8")
            return path, True, "updated"
        return path, False, "unchanged"
    except Exception as exc:  # noqa: BLE001 - batch updater should keep going.
        return path, False, f"error: {exc}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="Only update the first N API files.")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--refresh", action="store_true", help="Refresh cached official HTML.")
    parser.add_argument("--cache-dir", default="/tmp/wechat_api_page_cache")
    args = parser.parse_args()

    paths = markdown_files()
    if args.limit:
        paths = paths[: args.limit]
    url_map = build_url_map(markdown_files())
    cache_dir = Path(args.cache_dir)

    updated = 0
    errors: list[tuple[Path, str]] = []
    total = len(paths)
    print(f"api_files={total}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [
            executor.submit(update_one, (path, cache_dir, args.refresh, url_map))
            for path in paths
        ]
        for idx, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            path, changed, status = future.result()
            if changed:
                updated += 1
            if status.startswith("error:"):
                errors.append((path, status))
            if idx == total or idx % 50 == 0:
                print(f"processed={idx}/{total} updated={updated} errors={len(errors)}", flush=True)

    if errors:
        for path, status in errors[:50]:
            print(f"{path}: {status}", file=sys.stderr)
        return 1
    print(f"done updated={updated} errors=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
