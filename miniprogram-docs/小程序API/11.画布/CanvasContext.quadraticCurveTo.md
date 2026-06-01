# CanvasContext.quadraticCurveTo(number cpx, number cpy, number x, number y)

> 官方文档：[CanvasContext.quadraticCurveTo(number cpx, number cpy, number x, number y)](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.quadraticCurveTo.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / CanvasContext / CanvasContext.quadraticCurveTo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

CanvasContext 是旧版的接口，新版 [Canvas 2D](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html) 接口与 Web 一致

从基础库 [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [RenderingContext](RenderingContext.md) 代替

> **小程序插件**：支持

> 相关文档: [旧版画布迁移指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas-legacy-migration.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

## 功能描述

创建二次贝塞尔曲线路径。曲线的起始点为路径中前一个点。

## 参数

### number cpx

贝塞尔控制点的 x 坐标

### number cpy

贝塞尔控制点的 y 坐标

### number x

结束点的 x 坐标

### number y

结束点的 y 坐标

## 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

// Draw points
ctx.beginPath()
ctx.arc(20, 20, 2, 0, 2 * Math.PI)
ctx.setFillStyle('red')
ctx.fill()

ctx.beginPath()
ctx.arc(200, 20, 2, 0, 2 * Math.PI)
ctx.setFillStyle('lightgreen')
ctx.fill()

ctx.beginPath()
ctx.arc(20, 100, 2, 0, 2 * Math.PI)
ctx.setFillStyle('blue')
ctx.fill()

ctx.setFillStyle('black')
ctx.setFontSize(12)

// Draw guides
ctx.beginPath()
ctx.moveTo(20, 20)
ctx.lineTo(20, 100)
ctx.lineTo(200, 20)
ctx.setStrokeStyle('#AAAAAA')
ctx.stroke()

// Draw quadratic curve
ctx.beginPath()
ctx.moveTo(20, 20)
ctx.quadraticCurveTo(20, 100, 200, 20)
ctx.setStrokeStyle('black')
ctx.stroke()

ctx.draw()
```

针对 moveTo(20, 20) quadraticCurveTo(20, 100, 200, 20) 的三个关键坐标如下：

- 红色：起始点(20, 20)
- 蓝色：控制点(20, 100)
- 绿色：终止点(200, 20)
