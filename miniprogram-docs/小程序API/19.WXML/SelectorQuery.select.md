# NodesRef SelectorQuery.select(string selector)

> 官方文档：[NodesRef SelectorQuery.select(string selector)](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.select.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / SelectorQuery / SelectorQuery.select
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持

> 相关文档: [获取界面上的节点信息](https://developers.weixin.qq.com/miniprogram/dev/framework/view/selector.html)

## 功能描述

在当前页面下选择第一个匹配选择器 `selector` 的节点。返回一个 `NodesRef` 对象实例，可以用于获取节点信息。

## 参数

### string selector

选择器

## 返回值

### NodesRef

## selector 语法

selector类似于 CSS 的选择器，但仅支持下列语法。

- ID选择器：#the-id
- class选择器（可以连续指定多个）：.a-class.another-class
- 子元素选择器：.the-parent > .the-child
- 后代选择器：.the-ancestor .the-descendant
- 跨自定义组件的后代选择器：.the-ancestor >>> .the-descendant
- 多选择器的并集：#a-node, .some-other-nodes
