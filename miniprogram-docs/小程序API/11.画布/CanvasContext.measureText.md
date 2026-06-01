# Object CanvasContext.measureText(string text)

> 官方文档：[Object CanvasContext.measureText(string text)](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.measureText.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / CanvasContext / CanvasContext.measureText
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

CanvasContext 是旧版的接口，新版 [Canvas 2D](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html) 接口与 Web 一致

从基础库 [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [RenderingContext](RenderingContext.md) 代替

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

> 相关文档: [旧版画布迁移指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas-legacy-migration.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

## 功能描述

测量文本尺寸信息。目前仅返回文本宽度。同步接口。

## 参数

### string text

要测量的文本

## 返回值

### Object

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 文本的宽度 |

## 示例代码

```javascript
  const ctx = wx.createCanvasContext('myCanvas')
  ctx.font = 'italic bold 20px cursive'
  const metrics = ctx.measureText('Hello World')
  console.log(metrics.width)
```
