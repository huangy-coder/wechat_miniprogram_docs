# RenderingContext Canvas.getContext(string contextType)

> 官方文档：[RenderingContext Canvas.getContext(string contextType)](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.getContext.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / Canvas / Canvas.getContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

> 相关文档: [画布指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

## 功能描述

该方法返回 Canvas 的绘图上下文

## 参数

### string contextType

上下文类型

**contextType 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 2d | 2d 绘图上下文 |   |
| webgl | webgl 绘图上下文 |   |
| webgl2 | webgl2 绘图上下文 | [2.24.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 返回值

### RenderingContext

支持获取 2D 和 WebGL 绘图上下文
