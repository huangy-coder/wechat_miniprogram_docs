# SelectorQuery

> 官方文档：[SelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / SelectorQuery
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [获取界面上的节点信息](https://developers.weixin.qq.com/miniprogram/dev/framework/view/selector.html)

查询节点信息的对象

## 方法

### SelectorQuery SelectorQuery.in(Component component)

将选择器的选取范围更改为自定义组件 `component` 内。（初始时，选择器仅选取页面范围的节点，不会选取任何自定义组件中的节点）。

### NodesRef SelectorQuery.select(string selector)

在当前页面下选择第一个匹配选择器 `selector` 的节点。返回一个 `NodesRef` 对象实例，可以用于获取节点信息。

### NodesRef SelectorQuery.selectAll(string selector)

在当前页面下选择匹配选择器 selector 的所有节点。

### NodesRef SelectorQuery.selectViewport()

选择显示区域。可用于获取显示区域的尺寸、滚动位置等信息。

### NodesRef SelectorQuery.exec(function callback)

执行所有的请求。请求结果按请求次序构成数组，在callback的第一个参数中返回。
