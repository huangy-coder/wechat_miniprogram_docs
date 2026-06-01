# CanvasContext.fillText(string text, number x, number y, number maxWidth)

> 官方文档：[CanvasContext.fillText(string text, number x, number y, number maxWidth)](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.fillText.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / CanvasContext / CanvasContext.fillText
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

CanvasContext 是旧版的接口，新版 [Canvas 2D](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html) 接口与 Web 一致

从基础库 [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [RenderingContext](RenderingContext.md) 代替

> **小程序插件**：支持

> 相关文档: [旧版画布迁移指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas-legacy-migration.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

## 功能描述

在画布上绘制被填充的文本

## 参数

### string text

在画布上输出的文本

### number x

绘制文本的左上角 x 坐标位置

### number y

绘制文本的左上角 y 坐标位置

### number maxWidth

需要绘制的最大宽度，可选

## 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

ctx.setFontSize(20)
ctx.fillText('Hello', 20, 20)
ctx.fillText('MINA', 100, 100)

ctx.draw()
```
