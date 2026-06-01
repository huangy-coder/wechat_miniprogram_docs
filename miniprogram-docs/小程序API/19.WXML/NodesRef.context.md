# SelectorQuery NodesRef.context(function callback)

> 官方文档：[SelectorQuery NodesRef.context(function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.context.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / NodesRef / NodesRef.context
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.4.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

> 相关文档: [获取界面上的节点信息](https://developers.weixin.qq.com/miniprogram/dev/framework/view/selector.html)

## 功能描述

添加节点的 Context 对象查询请求。目前支持 [VideoContext](../12.媒体/video/VideoContext.md)、[CanvasContext](../11.画布/CanvasContext.md)、[LivePlayerContext](../12.媒体/live/LivePlayerContext.md)、[EditorContext](../12.媒体/editor/EditorContext.md)、[SelectionContext](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectionContext.html) 和 [MapContext](../12.媒体/map/MapContext.md) 的获取。

## 参数

### function callback

回调函数，在执行 `SelectorQuery.exec` 方法后，返回节点信息。

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| context | Object | 节点对应的 Context 对象 |

## 返回值

### SelectorQuery

## 示例代码

```js
Page({
  getContext () {
    wx.createSelectorQuery().select('.the-video-class').context(function(res){
      console.log(res.context) // 节点对应的 Context 对象。如：选中的节点是 <video> 组件，那么此处即返回 VideoContext 对象
    }).exec()
  }
})
```
