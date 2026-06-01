# SelectorQuery SelectorQuery.in(Component component)

> 官方文档：[SelectorQuery SelectorQuery.in(Component component)](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.in.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / SelectorQuery / SelectorQuery.in
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.6.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

> 相关文档: [获取界面上的节点信息](https://developers.weixin.qq.com/miniprogram/dev/framework/view/selector.html)

## 功能描述

将选择器的选取范围更改为自定义组件 `component` 内。（初始时，选择器仅选取页面范围的节点，不会选取任何自定义组件中的节点）。

## 参数

### Component component

自定义组件实例

## 返回值

### SelectorQuery

## 示例代码

```js
Component({
  queryMultipleNodes (){
    const query = wx.createSelectorQuery().in(this)
    query.select('#the-id').boundingClientRect(function(res){
      res.top // 这个组件内 #the-id 节点的上边界坐标
    }).exec()
  }
})
```
