# CanvasContext.createPattern(string image, string repetition)

> 官方文档：[CanvasContext.createPattern(string image, string repetition)](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.createPattern.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / CanvasContext / CanvasContext.createPattern
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

CanvasContext 是旧版的接口，新版 [Canvas 2D](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html) 接口与 Web 一致

从基础库 [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [RenderingContext](RenderingContext.md) 代替

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

> 相关文档: [旧版画布迁移指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas-legacy-migration.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

## 功能描述

对指定的图像创建模式的方法，可在指定的方向上重复元图像

## 参数

### string image

重复的图像源，支持代码包路径和本地临时路径 (本地路径)

### string repetition

如何重复图像

**repetition 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| repeat | 水平竖直方向都重复 |   |
| repeat-x | 水平方向重复 |   |
| repeat-y | 竖直方向重复 |   |
| no-repeat | 不重复 |   |

## 示例代码

```javascript
    const ctx = wx.createCanvasContext('myCanvas')
    const pattern = ctx.createPattern('/path/to/image', 'repeat-x')
    ctx.fillStyle = pattern
    ctx.fillRect(0, 0, 300, 150)
    ctx.draw()
```
