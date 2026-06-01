# ScrollViewContext.scrollIntoView(string selector, object ScrollIntoViewOptions)

> 官方文档：[ScrollViewContext.scrollIntoView(string selector, object ScrollIntoViewOptions)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/scroll/ScrollViewContext.scrollIntoView.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 滚动 / ScrollViewContext / ScrollViewContext.scrollIntoView
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.14.4 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

滚动至指定位置

## 参数

### string selector

元素选择器

### object ScrollIntoViewOptions

> 基础库 3.1.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

配置项，仅 Skyine 模式支持

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 0 | 否 | 跳转到目标节点时的额外偏移 |
| withinExtent | boolean | false | 否 | 只跳转到 cacheExtent 以内的目标节点，性能更佳 |
| alignment | string | "start" | 否 | 指定目标节点在视口内的位置 |
| animated | boolean | true | 否 | 是否启用滚动动画 |
