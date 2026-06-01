# CanvasContext.translate(number x, number y)

> 官方文档：[CanvasContext.translate(number x, number y)](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.translate.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / CanvasContext / CanvasContext.translate
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

CanvasContext 是旧版的接口，新版 [Canvas 2D](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html) 接口与 Web 一致

从基础库 [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [RenderingContext](RenderingContext.md) 代替

> **小程序插件**：支持

> 相关文档: [旧版画布迁移指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas-legacy-migration.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

## 功能描述

对当前坐标系的原点 (0, 0) 进行变换。默认的坐标系原点为页面左上角。

## 参数

### number x

水平坐标平移量

### number y

竖直坐标平移量

## 示例代码

```javascript
const ctx = wx.createCanvasContext('myCanvas')

ctx.strokeRect(10, 10, 150, 100)
ctx.translate(20, 20)
ctx.strokeRect(10, 10, 150, 100)
ctx.translate(20, 20)
ctx.strokeRect(10, 10, 150, 100)

ctx.draw()
```
