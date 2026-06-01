# ScrollViewContext.scrollTo(Object object)

> 官方文档：[ScrollViewContext.scrollTo(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/scroll/ScrollViewContext.scrollTo.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 滚动 / ScrollViewContext / ScrollViewContext.scrollTo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.14.4 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

滚动至指定位置

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| top | number |   | 否 | 顶部距离 |
| left | number |   | 否 | 左边界距离 |
| velocity | number |   | 否 | 初始速度 (webview 仅在 iOS 下生效；skyline 在 3.14.3 后支持) |
| duration | number |   | 否 | 滚动动画时长 (webview 仅在 iOS 下生效；skyline 在 3.14.3 后支持) |
| animated | boolean |   | 否 | 是否启用滚动动画 |
