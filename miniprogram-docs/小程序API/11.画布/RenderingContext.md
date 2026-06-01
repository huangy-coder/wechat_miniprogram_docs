# RenderingContext

> 官方文档：[RenderingContext](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/RenderingContext.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / RenderingContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [画布指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

Canvas 绘图上下文。

- 通过 Canvas.getContext('2d') 接口可以获取 CanvasRenderingContext2D 对象，实现了 [HTML Canvas 2D Context](https://www.w3.org/TR/2dcontext/) 定义的属性、方法。
- 通过 Canvas.getContext('webgl') 或 OffscreenCanvas.getContext('webgl') 接口可以获取 WebGLRenderingContext 对象，实现了 [WebGL 1.0](https://www.khronos.org/registry/webgl/specs/latest/1.0/) 定义的所有属性、方法、常量。
- CanvasRenderingContext2D 的 drawImage 方法 2.10.0 起支持传入通过 [SelectorQuery](../19.WXML/SelectorQuery.md) 获取的 video 对象，2.29.0 起支持传入开启了自定义渲染的 [LivePusherContext](../12.媒体/live/LivePusherContext.md) 对象。

## 示例代码

video 画到 2D Canvas 示例
[在开发者工具中预览效果](https://developers.weixin.qq.com/s/tJTak7mU7sfX)
