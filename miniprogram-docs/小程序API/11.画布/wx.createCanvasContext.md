# CanvasContext wx.createCanvasContext(string canvasId, Object this)

> 官方文档：[CanvasContext wx.createCanvasContext(string canvasId, Object this)](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.createCanvasContext.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / wx.createCanvasContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

从基础库 [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [Canvas](Canvas.md) 代替

> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [旧版画布迁移指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas-legacy-migration.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

## 功能描述

创建 canvas 的绘图上下文 [CanvasContext](CanvasContext.md) 对象

## 参数

### string canvasId

要获取上下文的 [canvas](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html) 组件 canvas-id 属性

### Object this

在自定义组件下，当前组件实例的this，表示在这个自定义组件下查找拥有 canvas-id 的 [canvas](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html) ，如果省略则不在任何自定义组件内查找

## 返回值

### CanvasContext
