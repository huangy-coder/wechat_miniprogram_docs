# RenderingContext OffscreenCanvas.getContext(string contextType)

> 官方文档：[RenderingContext OffscreenCanvas.getContext(string contextType)](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/OffscreenCanvas.getContext.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / OffscreenCanvas / OffscreenCanvas.getContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.16.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

> 相关文档: [画布指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

## 功能描述

该方法返回 OffscreenCanvas 的绘图上下文

## 参数

### string contextType

绘图上下文类型，需要与 createOffscreenCanvas 时传入的 type 一致

**contextType 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| webgl | webgl类型上下文 |   |
| 2d | 2d类型上下文 | [2.16.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 返回值

### RenderingContext

注意不允许混用 webgl 和 2d 绘图上下文，传入的 contextType 必须要与 `wx.createOffscreenCanvas` 传入的 type 类型一致。
