# CanvasContext.drawImage(string imageResource, number sx, number sy, number sWidth, number sHeight, number dx, number dy, number dWidth, number dHeight)

> 官方文档：[CanvasContext.drawImage(string imageResource, number sx, number sy, number sWidth, number sHeight, number dx, number dy, number dWidth, number dHeight)](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.drawImage.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / CanvasContext / CanvasContext.drawImage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

CanvasContext 是旧版的接口，新版 [Canvas 2D](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html) 接口与 Web 一致

从基础库 [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [RenderingContext](RenderingContext.md) 代替

> **小程序插件**：支持

> 相关文档: [旧版画布迁移指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas-legacy-migration.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

## 功能描述

绘制图像到画布

## 参数

### string imageResource

所要绘制的图片资源（网络图片要通过 getImageInfo / downloadFile 先下载）

### number sx

需要绘制到画布中的，imageResource的矩形（裁剪）选择框的左上角 x 坐标

### number sy

需要绘制到画布中的，imageResource的矩形（裁剪）选择框的左上角 y 坐标

### number sWidth

需要绘制到画布中的，imageResource的矩形（裁剪）选择框的宽度

### number sHeight

需要绘制到画布中的，imageResource的矩形（裁剪）选择框的高度

### number dx

imageResource的左上角在目标 canvas 上 x 轴的位置

### number dy

imageResource的左上角在目标 canvas 上 y 轴的位置

### number dWidth

在目标画布上绘制imageResource的宽度，允许对绘制的imageResource进行缩放

### number dHeight

在目标画布上绘制imageResource的高度，允许对绘制的imageResource进行缩放

## 示例代码

有三个版本的写法：

- drawImage(imageResource, dx, dy)
- drawImage(imageResource, dx, dy, dWidth, dHeight)
- drawImage(imageResource, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight) 从 1.9.0 起支持

```javascript
const ctx = wx.createCanvasContext('myCanvas')

wx.chooseImage({
  success: function(res){
    ctx.drawImage(res.tempFilePaths[0], 0, 0, 150, 100)
    ctx.draw()
  }
})
```
