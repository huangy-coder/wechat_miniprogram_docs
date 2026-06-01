# SelectorQuery NodesRef.scrollOffset(function callback)

> 官方文档：[SelectorQuery NodesRef.scrollOffset(function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.scrollOffset.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / NodesRef / NodesRef.scrollOffset
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持

> 相关文档: [获取界面上的节点信息](https://developers.weixin.qq.com/miniprogram/dev/framework/view/selector.html)

## 功能描述

添加节点的滚动位置查询请求。以像素为单位。节点必须是 `scroll-view` 或者 `viewport`，返回 `NodesRef` 对应的 `SelectorQuery`。

## 参数

### function callback

回调函数，在执行 `SelectorQuery.exec` 方法后，节点信息会在 `callback` 中返回。

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 节点的 ID |
| dataset | Object | 节点的 dataset |
| scrollLeft | number | 节点的水平滚动位置 |
| scrollTop | number | 节点的竖直滚动位置 |
| scrollWidth | number | 节点的滚动宽度 |
| scrollHeight | number | 节点的滚动高度 |

## 返回值

### SelectorQuery

## 示例代码

```js
Page({
  getScrollOffset () {
    wx.createSelectorQuery().selectViewport().scrollOffset(function(res){
      res.id      // 节点的ID
      res.dataset // 节点的dataset
      res.scrollLeft // 节点的水平滚动位置
      res.scrollTop  // 节点的竖直滚动位置
    }).exec()
  }
})
```
