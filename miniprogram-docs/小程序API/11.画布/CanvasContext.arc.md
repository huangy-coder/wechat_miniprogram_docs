# CanvasContext.arc(number x, number y, number r, number sAngle, number eAngle, boolean counterclockwise)

> 官方文档：[CanvasContext.arc(number x, number y, number r, number sAngle, number eAngle, boolean counterclockwise)](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.arc.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / CanvasContext / CanvasContext.arc
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

CanvasContext 是旧版的接口，新版 [Canvas 2D](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html) 接口与 Web 一致

从基础库 [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [RenderingContext](RenderingContext.md) 代替

> **小程序插件**：支持

> 相关文档: [旧版画布迁移指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas-legacy-migration.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

## 功能描述

创建一条弧线。

- 创建一个圆可以指定起始弧度为 0，终止弧度为 2 * Math.PI。
- 用 `stroke` 或者 `fill` 方法来在 `canvas` 中画弧线。

## 参数

### number x

圆心的 x 坐标

### number y

圆心的 y 坐标

### number r

圆的半径

### number sAngle

起始弧度，单位弧度（在3点钟方向）

### number eAngle

终止弧度

### boolean counterclockwise

弧度的方向是否是逆时针

## 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

// Draw coordinates
ctx.arc(100, 75, 50, 0, 2 * Math.PI)
ctx.setFillStyle('#EEEEEE')
ctx.fill()

ctx.beginPath()
ctx.moveTo(40, 75)
ctx.lineTo(160, 75)
ctx.moveTo(100, 15)
ctx.lineTo(100, 135)
ctx.setStrokeStyle('#AAAAAA')
ctx.stroke()

ctx.setFontSize(12)
ctx.setFillStyle('black')
ctx.fillText('0', 165, 78)
ctx.fillText('0.5*PI', 83, 145)
ctx.fillText('1*PI', 15, 78)
ctx.fillText('1.5*PI', 83, 10)

// Draw points
ctx.beginPath()
ctx.arc(100, 75, 2, 0, 2 * Math.PI)
ctx.setFillStyle('lightgreen')
ctx.fill()

ctx.beginPath()
ctx.arc(100, 25, 2, 0, 2 * Math.PI)
ctx.setFillStyle('blue')
ctx.fill()

ctx.beginPath()
ctx.arc(150, 75, 2, 0, 2 * Math.PI)
ctx.setFillStyle('red')
ctx.fill()

// Draw arc
ctx.beginPath()
ctx.arc(100, 75, 50, 0, 1.5 * Math.PI)
ctx.setStrokeStyle('#333333')
ctx.stroke()

ctx.draw()
```

针对 arc(100, 75, 50, 0, 1.5 * Math.PI)的三个关键坐标如下：

- 绿色: 圆心 (100, 75)
- 红色: 起始弧度 (0)
- 蓝色: 终止弧度 (1.5 * Math.PI)
