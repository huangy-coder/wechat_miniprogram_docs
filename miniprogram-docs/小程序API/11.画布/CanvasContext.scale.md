# CanvasContext.scale(number scaleWidth, number scaleHeight)

> 官方文档：[CanvasContext.scale(number scaleWidth, number scaleHeight)](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.scale.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / CanvasContext / CanvasContext.scale
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

CanvasContext 是旧版的接口，新版 [Canvas 2D](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html) 接口与 Web 一致

从基础库 [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [RenderingContext](RenderingContext.md) 代替

> **小程序插件**：支持

> 相关文档: [旧版画布迁移指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas-legacy-migration.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

## 功能描述

在调用后，之后创建的路径其横纵坐标会被缩放。多次调用倍数会相乘。

## 参数

### number scaleWidth

横坐标缩放的倍数 (1 = 100%，0.5 = 50%，2 = 200%)

### number scaleHeight

纵坐标轴缩放的倍数 (1 = 100%，0.5 = 50%，2 = 200%)

## 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

ctx.strokeRect(10, 10, 25, 15)
ctx.scale(2, 2)
ctx.strokeRect(10, 10, 25, 15)
ctx.scale(2, 2)
ctx.strokeRect(10, 10, 25, 15)

ctx.draw()
```
