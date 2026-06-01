# SelectorQuery NodesRef.boundingClientRect(function callback)

> 官方文档：[SelectorQuery NodesRef.boundingClientRect(function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.boundingClientRect.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / NodesRef / NodesRef.boundingClientRect
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持

> 相关文档: [获取界面上的节点信息](https://developers.weixin.qq.com/miniprogram/dev/framework/view/selector.html)

## 功能描述

添加节点的布局位置的查询请求。相对于显示区域，以像素为单位。其功能类似于 DOM 的 `getBoundingClientRect`。返回 `NodesRef` 对应的 `SelectorQuery`。

## 参数

### function callback

回调函数，在执行 `SelectorQuery.exec` 方法后，节点信息会在 `callback` 中返回。

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 节点的 ID |
| dataset | Object | 节点的 dataset |
| left | number | 节点的左边界坐标 |
| right | number | 节点的右边界坐标 |
| top | number | 节点的上边界坐标 |
| bottom | number | 节点的下边界坐标 |
| width | number | 节点的宽度 |
| height | number | 节点的高度 |

## 返回值

### SelectorQuery

## 示例代码

```js
Page({
  getRect () {
    wx.createSelectorQuery().select('#the-id').boundingClientRect(function(rect){
      rect.id      // 节点的ID
      rect.dataset // 节点的dataset
      rect.left    // 节点的左边界坐标
      rect.right   // 节点的右边界坐标
      rect.top     // 节点的上边界坐标
      rect.bottom  // 节点的下边界坐标
      rect.width   // 节点的宽度
      rect.height  // 节点的高度
    }).exec()
  },
  getAllRects () {
    wx.createSelectorQuery().selectAll('.a-class').boundingClientRect(function(rects){
      rects.forEach(function(rect){
        rect.id      // 节点的ID
        rect.dataset // 节点的dataset
        rect.left    // 节点的左边界坐标
        rect.right   // 节点的右边界坐标
        rect.top     // 节点的上边界坐标
        rect.bottom  // 节点的下边界坐标
        rect.width   // 节点的宽度
        rect.height  // 节点的高度
      })
    }).exec()
  }
})
```
