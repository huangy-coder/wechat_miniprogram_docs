#!/usr/bin/env python3
"""Build local Mini Program server API Markdown from official server docs."""

from __future__ import annotations

import argparse
from collections import OrderedDict
import concurrent.futures
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlparse

from bs4 import BeautifulSoup, Tag

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from update_api_content import (  # noqa: E402
    fetch_html,
    normalize_official_url,
    official_body_to_markdown,
)


SERVER_ROOT = ROOT / "miniprogram-docs" / "服务端API目录"
NAV_HTML = Path("/tmp/wechat_dev_pages/服务端.html")
OFFICIAL_BASE = "https://developers.weixin.qq.com"
TODAY = "2026-06-01"


INTRO = {
    "开发前必读": "服务端接口调用前的签名、请求安全和接入规范。",
    "事件通知": "平台、物流、配送、短剧、付费、评价、直播等服务端事件推送。",
    "接口调用凭证": "服务端调用小程序接口所需的 access_token 与稳定凭证。",
    "openApi管理": "接口调用额度、调用次数、rid、微信服务器 IP 等管理能力。",
    "用户信息": "用户基础信息、加密信息、手机号和用户 encryptKey 等接口。",
    "小程序登录": "登录凭证校验、登录态检验和登录态重置。",
    "小程序码与小程序链接": "小程序码、URL Scheme、URL Link 和 Short Link 生成与查询。",
    "小程序客服": "客服账号、客服消息、临时素材和客服子商户管理。",
    "微信客服": "微信客服账号、客户、消息、升级服务和会话状态管理。",
    "消息相关": "动态消息、订阅消息、统一服务消息、插件消息和内容安全消息能力。",
    "用工关系": "用工关系绑定、查询和解除。",
    "小程序安全": "内容安全、用户安全、违规风险和安全风控能力。",
    "数据分析": "访问趋势、留存、画像、性能、广告等数据分析接口。",
    "硬件设备": "蓝牙、NFC、IOT 和硬件设备相关服务端能力。",
    "运维中心": "性能监控、告警、日志、即时反馈和运维工具接口。",
    "插件管理": "插件申请、使用、管理和插件服务能力。",
    "云开发": "云开发相关服务端资源、数据库、云函数和文件能力。",
    "物流助手": "物流服务商、运单、面单、退货、保险和轨迹能力。",
    "即时配送": "配送下单、查询、取消、异常处理和配送服务商能力。",
    "微信物流服务": "微信物流服务订单、商户、运力和轨迹能力。",
    "付费管理": "付费服务、订单、用量和额度管理。",
    "小程序交易管理服务": "订单发货、售后、资金、纠纷和交易组件相关接口。",
    "交易保障": "交易保障、评价、投诉和履约相关服务端能力。",
    "B2b门店助手": "B2B 门店助手业务接口。",
    "短剧媒资管理": "短剧媒资上传、审核、查询和管理能力。",
    "短剧播放器": "短剧播放器、播放授权和播放相关接口。",
    "小说作品管理": "小说作品、章节、审核和内容管理能力。",
    "微信学生身份快速验证": "学生身份快速验证相关服务端接口。",
    "城市服务": "城市服务能力接入与管理接口。",
    "附近小程序": "附近地点、门店和附近小程序相关接口。",
    "小程序直播": "直播间、商品、订阅、回放和长期订阅相关接口。",
    "图像处理与文字识别": "图像处理、OCR 和证照识别相关能力。",
    "微信红包封面": "红包封面领取、发放和管理能力。",
    "微信服务市场": "服务市场订单、服务商和相关业务接口。",
    "生物认证": "SOTER 生物认证相关服务端接口。",
    "微信人脸核身": "人脸核身、实名验证和身份认证接口。",
    "微信搜一搜": "搜索接入、页面收录和搜索能力。",
    "虚拟支付": "虚拟支付订单、结算、退款和权益相关接口。",
    "广告": "广告数据回传和广告能力相关服务端接口。",
}


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def safe_segment(text: str) -> str:
    text = unquote(text).strip().strip("/")
    text = re.sub(r"[\\:*?\"<>|]", "-", text)
    text = text.replace(" ", "-")
    return text or "index"


def absolute_url(href: str) -> str:
    return normalize_official_url(urljoin(OFFICIAL_BASE, href))


def nav_tree() -> list[dict]:
    soup = BeautifulSoup(NAV_HTML.read_text(encoding="utf-8"), "html.parser")
    level0 = soup.select_one(".TreeNavigation .NavigationLevel--level-0")
    if not level0:
        raise RuntimeError("missing server navigation")
    root_ul = level0.find("ul", recursive=False)
    if not root_ul:
        raise RuntimeError("missing server navigation list")
    return [parse_li(li) for li in root_ul.find_all("li", recursive=False)]


def parse_li(li: Tag) -> dict:
    own_link = None
    parent = li.find("div", class_="NavigationLevel__parent", recursive=True)
    if parent:
        own_link = parent.find("a", href=True)
    if own_link is None:
        own_link = li.find("a", href=True)
    title = clean_text(own_link.get_text(" ", strip=True)) if own_link else "未命名"
    href = absolute_url(own_link["href"]) if own_link else ""
    children = []
    child_ul = None
    if parent:
        parent_container = parent.find_parent("div", class_="NavigationLevel")
        child_ul = parent_container.find("ul", class_="NavigationLevel__children", recursive=False) if parent_container else None
    if child_ul is None:
        child_ul = li.find("ul", class_="NavigationLevel__children", recursive=False)
    if child_ul:
        children = [parse_li(child) for child in child_ul.find_all("li", recursive=False)]
    return {"title": title, "url": href, "children": children}


def collect_pages_for_category(node: dict) -> list[dict]:
    pages: OrderedDict[str, dict] = OrderedDict()

    def walk(item: dict, trail: list[str]) -> None:
        url = item["url"]
        if url and not url.endswith("/miniprogram/dev/server/API"):
            pages.setdefault(url, {"title": item["title"], "url": url, "trail": trail + [item["title"]]})
        for child in item["children"]:
            walk(child, trail + [item["title"]])

    walk(node, [])
    return list(pages.values())


def category_base_url(category: dict) -> str:
    url = category["url"]
    path = urlparse(url).path
    if path.endswith("/"):
        return url
    if "/server/event_push/" in path:
        return OFFICIAL_BASE + "/miniprogram/dev/server/event_push/"
    if "/server/getting_started/" in path:
        return OFFICIAL_BASE + "/miniprogram/dev/server/getting_started/"
    if "/server/ad/" in path:
        return OFFICIAL_BASE + "/miniprogram/dev/server/ad/"
    return url.rsplit("/", 1)[0] + "/"


def local_page_path(category_dir: Path, category: dict, page: dict) -> Path:
    base = category_base_url(category)
    url = page["url"]
    if url == normalize_official_url(base) or url + "/" == base:
        return category_dir / "概览.md"
    rel = url[len(base) :] if url.startswith(base) else urlparse(url).path.split("/server/", 1)[-1]
    rel = rel.strip("/")
    if not rel:
        rel = "overview"
    if rel.endswith(".html"):
        rel = rel[:-5]
    parts = [safe_segment(part) for part in rel.split("/") if part]
    if not parts:
        parts = ["概览"]
    return category_dir.joinpath(*parts).with_suffix(".md")


def build_model() -> tuple[list[dict], dict[str, Path]]:
    categories = nav_tree()
    url_map: dict[str, Path] = {}
    for idx, category in enumerate(categories, start=1):
        category_dir = SERVER_ROOT / f"{idx}.{safe_segment(category['title'])}"
        pages = collect_pages_for_category(category)
        category["pages"] = pages
        category["dir"] = category_dir
        for page in pages:
            path = local_page_path(category_dir, category, page)
            page["path"] = path
            url_map[normalize_official_url(page["url"])] = path
    return categories, url_map


def rel_link(path: Path, from_dir: Path) -> str:
    return os.path.relpath(path, from_dir)


def render_tree(nodes: list[dict], from_dir: Path, url_map: dict[str, Path], depth: int = 0) -> list[str]:
    lines: list[str] = []
    seen_at_level = set()
    for node in nodes:
        url = normalize_official_url(node["url"]) if node["url"] else ""
        target = url_map.get(url)
        title = node["title"]
        indent = "  " * depth
        if target:
            line = f"{indent}- [{title}]({rel_link(target, from_dir)})"
        else:
            line = f"{indent}- {title}"
        key = (depth, title, str(target))
        if key not in seen_at_level:
            lines.append(line)
            seen_at_level.add(key)
        if node["children"]:
            lines.extend(render_tree(node["children"], from_dir, url_map, depth + 1))
    return lines


def render_category_doc(idx: int, category: dict, url_map: dict[str, Path]) -> str:
    title = category["title"]
    category_dir = category["dir"]
    pages = category["pages"]
    lines = [
        f"# {title}服务端 API 目录",
        "",
        f"> 官方入口：[{title}]({category['url']})",
        f"> 整理日期：{TODAY}",
        "> 所属范围：微信小程序「开发 / 服务端」栏目。",
        "",
        "## 功能范围",
        "",
        INTRO.get(title, "微信小程序服务端开发能力。"),
        "",
        "## 本地条目",
        "",
        f"- 本分类共整理 {len(pages)} 个独立服务端页面。",
        "- 下方目录保持官方左侧导航层级，并链接到本地 Markdown 正文。",
        "",
        "## 目录",
        "",
    ]
    lines.extend(render_tree([category], category_dir, url_map))
    lines.append("")
    return "\n".join(lines)


def official_full_tree(categories: list[dict], depth: int = 0) -> list[str]:
    lines: list[str] = []
    for node in categories:
        indent = "  " * depth
        lines.append(f"{indent}- [{node['title']}]({node['url']})")
        if node["children"]:
            lines.extend(official_full_tree(node["children"], depth + 1))
    return lines


def render_index(categories: list[dict]) -> str:
    total_pages = sum(len(c["pages"]) for c in categories)
    lines = [
        "# 微信开放文档 / 服务端 API 目录",
        "",
        "> 来源：[服务端](https://developers.weixin.qq.com/miniprogram/dev/server/API/)",
        f"> 整理日期：{TODAY}",
        "> 整理范围：仅限小程序顶部导航「开发」栏目；不整理顶部「介绍 / 设计 / 运营 / 数据 / 安全」大类。",
        "",
        "## 定位",
        "",
        "整理小程序服务端 API 和服务端开发文档，覆盖调用凭证、事件通知、登录、码和链接、客服、消息、安全、数据分析、硬件、运维、插件、交易、广告等服务端能力。",
        "",
        "## 覆盖统计",
        "",
        "| 分组 | 官方入口 | 导航项 | 本地服务端文档 |",
        "| --- | --- | ---: | ---: |",
        f"| 服务端 | [服务端](https://developers.weixin.qq.com/miniprogram/dev/server/API/) | 574 | {total_pages} |",
        "",
        "## 一级分组",
        "",
        "| 分组 | 本地目录 | 官方入口 | 页面数 |",
        "| --- | --- | --- | ---: |",
    ]
    for idx, category in enumerate(categories, start=1):
        name = category["title"]
        directory = f"{idx}.{safe_segment(name)}/{safe_segment(name)}目录.md"
        lines.append(f"| {name} | [{name}目录]({directory}) | [官方入口]({category['url']}) | {len(category['pages'])} |")
    lines.extend(
        [
            "",
            "## 本地正文",
            "",
            f"- 已按官方左侧导航补齐 {len(categories)} 个服务端一级分类目录。",
            f"- 已按官方 URL 层级生成 {total_pages} 个服务端 API 正文文档，分类目录中的条目均链接到本地 Markdown。",
            "- 每个服务端文档保留官方文档链接、所属分类、导航路径，并整理接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。",
            "",
            "## 官方完整目录",
            "",
        ]
    )
    lines.extend(official_full_tree(categories))
    lines.append("")
    return "\n".join(lines)


def render_page(path: Path, page: dict, category: dict, title: str, body_lines: list[str]) -> str:
    category_doc = category["dir"] / f"{safe_segment(category['title'])}目录.md"
    category_link = rel_link(category_doc, path.parent)
    nav = " / ".join(page["trail"])
    lines = [
        f"# {title}",
        "",
        f"> 官方文档：[{title}]({page['url']})",
        f"> 所属分类：[{category['title']}]({category_link})",
        f"> 导航路径：{nav}",
        f"> 整理日期：{TODAY}",
        "> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。",
        "",
    ]
    lines.extend(body_lines)
    lines.append("")
    return "\n".join(lines)


def write_catalogs(categories: list[dict], url_map: dict[str, Path]) -> None:
    SERVER_ROOT.mkdir(parents=True, exist_ok=True)
    (SERVER_ROOT / "服务端API目录.md").write_text(render_index(categories), encoding="utf-8")
    for idx, category in enumerate(categories, start=1):
        category["dir"].mkdir(parents=True, exist_ok=True)
        doc_path = category["dir"] / f"{safe_segment(category['title'])}目录.md"
        doc_path.write_text(render_category_doc(idx, category, url_map), encoding="utf-8")


def update_one(args) -> tuple[Path, bool, str]:
    page, category, cache_dir, refresh, url_map = args
    path = page["path"]
    try:
        html = fetch_html(page["url"], cache_dir, refresh)
        title, body_lines = official_body_to_markdown(html, page["url"], path, url_map)
        path.parent.mkdir(parents=True, exist_ok=True)
        new_text = render_page(path, page, category, title, body_lines)
        old_text = path.read_text(encoding="utf-8") if path.exists() else ""
        if old_text != new_text:
            path.write_text(new_text, encoding="utf-8")
            return path, True, "updated"
        return path, False, "unchanged"
    except Exception as exc:  # noqa: BLE001
        return path, False, f"error: {exc}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--cache-dir", default="/tmp/wechat_server_page_cache")
    args = parser.parse_args()

    categories, url_map = build_model()
    write_catalogs(categories, url_map)

    jobs = []
    for category in categories:
        for page in category["pages"]:
            jobs.append((page, category, Path(args.cache_dir), args.refresh, url_map))
    if args.limit:
        jobs = jobs[: args.limit]

    updated = 0
    errors: list[tuple[Path, str]] = []
    total = len(jobs)
    print(f"server_pages={total}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(update_one, job) for job in jobs]
        for idx, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            path, changed, status = future.result()
            if changed:
                updated += 1
            if status.startswith("error:"):
                errors.append((path, status))
            if idx == total or idx % 50 == 0:
                print(f"processed={idx}/{total} updated={updated} errors={len(errors)}", flush=True)

    if errors:
        for path, status in errors[:80]:
            print(f"{path}: {status}", file=sys.stderr)
        return 1
    print(f"done updated={updated} errors=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
