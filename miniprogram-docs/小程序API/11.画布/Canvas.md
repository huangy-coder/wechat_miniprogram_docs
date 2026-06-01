# Canvas

> 官方文档：[Canvas](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / Canvas
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [画布指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

Canvas 实例，可通过 [SelectorQuery](../19.WXML/SelectorQuery.md) 获取。

## 属性

### number width

画布宽度

### number height

画布高度

## 方法

### RenderingContext Canvas.getContext(string contextType)

该方法返回 Canvas 的绘图上下文

### Image Canvas.createImage()

创建一个图片对象。 支持在 2D Canvas 和 WebGL Canvas 下使用, 但不支持混用 2D 和 WebGL 的方法。

### ImageData Canvas.createImageData()

创建一个 ImageData 对象。仅支持在 2D Canvas 中使用。

### Path2D Canvas.createPath2D(Path2D path)

创建 Path2D 对象

### number Canvas.requestAnimationFrame(function callback)

在下次进行重绘时执行。 支持在 2D Canvas 和 WebGL Canvas 下使用, 但不支持混用 2D 和 WebGL 的方法。

### Canvas.cancelAnimationFrame(number requestID)

取消由 requestAnimationFrame 添加到计划中的动画帧请求。支持在 2D Canvas 和 WebGL Canvas 下使用, 但不支持混用 2D 和 WebGL 的方法。

### string Canvas.toDataURL(string type, number encoderOptions)

返回一个包含图片展示的 data URI 。可以使用 type 参数其类型，默认为 PNG 格式。

## 示例代码

2D Canvas 示例
[在开发者工具中预览效果](https://developers.weixin.qq.com/s/SHfgCmmq7UcM)

WebGL 示例
[在开发者工具中预览效果](https://developers.weixin.qq.com/s/qEGUOqmf7T8z)
