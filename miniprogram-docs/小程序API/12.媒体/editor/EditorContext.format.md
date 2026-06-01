# EditorContext.format(string name, string value)

> 官方文档：[EditorContext.format(string name, string value)](https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.format.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 富文本 / EditorContext / EditorContext.format
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

> 相关文档: [editor 组件](https://developers.weixin.qq.com/miniprogram/dev/component/editor.html)

## 功能描述

修改样式

## 参数

### string name

属性

### string value

值

## 支持设置的样式列表

| name | value | verson |
| --- | --- | --- |
| bold |   | 2.7.0 |
| italic |   | 2.7.0 |
| underline |   | 2.7.0 |
| strike |   | 2.7.0 |
| ins |   | 2.7.0 |
| script | sub / super | 2.7.0 |
| header | H1 / H2 / h3 / H4 / h5 / H6 | 2.7.0 |
| align | left / center / right / justify | 2.7.0 |
| direction | rtl | 2.7.0 |
| indent | -1 / +1 | 2.7.0 |
| list | ordered / bullet / check | 2.7.0 |
| color | hex color | 2.7.0 |
| backgroundColor | hex color | 2.7.0 |
| margin/marginTop/marginBottom/marginLeft/marginRight | css style | 2.7.0 |
| padding/paddingTop/paddingBottom/paddingLeft/paddingRight | css style | 2.7.0 |
| font/fontSize/fontStyle/fontVariant/fontWeight/fontFamily | css style | 2.7.0 |
| lineHeight | css style | 2.7.0 |
| letterSpacing | css style | 2.7.0 |
| textDecoration | css style | 2.7.0 |
| textIndent | css style | 2.8.0 |
| wordWrap | css style | 2.10.2 |
| wordBreak | css style | 2.10.2 |
| whiteSpace | css style | 2.10.2 |

对已经应用样式的选区设置会取消样式。css style 表示 css 中规定的允许值。
