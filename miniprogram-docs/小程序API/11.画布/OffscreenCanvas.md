# OffscreenCanvas

> 官方文档：[OffscreenCanvas](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/OffscreenCanvas.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / OffscreenCanvas
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [画布指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

离屏 canvas 实例，可通过 [wx.createOffscreenCanvas](wx.createOffscreenCanvas.md) 创建。

## 属性

### number width

画布宽度

### number height

画布高度

## 方法

### RenderingContext OffscreenCanvas.getContext(string contextType)

该方法返回 OffscreenCanvas 的绘图上下文

### Image OffscreenCanvas.createImage()

创建一个图片对象。支持在 2D Canvas 和 WebGL Canvas 下使用, 但不支持混用 2D 和 WebGL 的方法。
