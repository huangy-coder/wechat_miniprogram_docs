# SelectorQuery NodesRef.ref(function callback)

> 官方文档：[SelectorQuery NodesRef.ref(function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.ref.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / NodesRef / NodesRef.ref
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.3.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

> 相关文档: [获取界面上的节点信息](https://developers.weixin.qq.com/miniprogram/dev/framework/view/selector.html) [scrollViewContext](../6.界面/worklet/base/worklet.scrollViewContext.scrollTo.md)

## 功能描述

获取 `Node` 节点的 Ref 对象，可用于 `worklet` 函数内操作节点。仅 `Skyline` 下支持，`Node` 必须是非 `virtual` 类型。

## 参数

### function callback

回调函数，在执行 `SelectorQuery.exec` 方法后，返回节点 Ref 对象。

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ref | Object | 节点对应的 Ref 对象 |

## 返回值

### SelectorQuery

## 示例代码

```js
Page({
  getNode() {
    this.createSelectorQuery().select('.scrollable').ref(function(res){
      console.log(res.ref) // 节点对应的 Ref 对象
    }).exec()
  }
})
```
