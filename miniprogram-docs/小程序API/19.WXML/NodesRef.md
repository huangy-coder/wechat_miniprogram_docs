# NodesRef

> 官方文档：[NodesRef](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / NodesRef
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [获取界面上的节点信息](https://developers.weixin.qq.com/miniprogram/dev/framework/view/selector.html)

用于获取 WXML 节点信息的对象

## 方法

### SelectorQuery NodesRef.fields(Object fields, NodesRef.FieldsCallback callback)

获取节点的相关信息。需要获取的字段在fields中指定。返回值是 `nodesRef` 对应的 `selectorQuery`

### SelectorQuery NodesRef.boundingClientRect(NodesRef.boundingClientRectCallback callback)

添加节点的布局位置的查询请求。相对于显示区域，以像素为单位。其功能类似于 DOM 的 `getBoundingClientRect`。返回 `NodesRef` 对应的 `SelectorQuery`。

### SelectorQuery NodesRef.scrollOffset(NodesRef.scrollOffsetCallback callback)

添加节点的滚动位置查询请求。以像素为单位。节点必须是 `scroll-view` 或者 `viewport`，返回 `NodesRef` 对应的 `SelectorQuery`。

### SelectorQuery NodesRef.context(NodesRef.contextCallback callback)

添加节点的 Context 对象查询请求。目前支持 [VideoContext](../12.媒体/video/VideoContext.md)、[CanvasContext](../11.画布/CanvasContext.md)、[LivePlayerContext](../12.媒体/live/LivePlayerContext.md)、[EditorContext](../12.媒体/editor/EditorContext.md)、[SelectionContext](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectionContext.html) 和 [MapContext](../12.媒体/map/MapContext.md) 的获取。

### SelectorQuery NodesRef.node(NodesRef.nodeCallback callback)

获取 Node 节点实例。目前支持 [Canvas](../11.画布/Canvas.md) 和 [ScrollViewContext](../6.界面/scroll/ScrollViewContext.md) 的获取。

### SelectorQuery NodesRef.ref(NodesRef.refCallback callback)

获取 `Node` 节点的 Ref 对象，可用于 `worklet` 函数内操作节点。仅 `Skyline` 下支持，`Node` 必须是非 `virtual` 类型。
