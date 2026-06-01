# IntersectionObserver IntersectionObserver.relativeTo(string selector, Object margins)

> 官方文档：[IntersectionObserver IntersectionObserver.relativeTo(string selector, Object margins)](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/IntersectionObserver.relativeTo.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / IntersectionObserver / IntersectionObserver.relativeTo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持

> 相关文档: [获取界面上的节点信息](https://developers.weixin.qq.com/miniprogram/dev/framework/view/selector.html)

## 功能描述

使用选择器指定一个节点，作为参照区域之一。

## 参数

### string selector

选择器

### Object margins

用来扩展（或收缩）参照节点布局区域的边界

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| left | number |   | 否 | 节点布局区域的左边界 |
| right | number |   | 否 | 节点布局区域的右边界 |
| top | number |   | 否 | 节点布局区域的上边界 |
| bottom | number |   | 否 | 节点布局区域的下边界 |

## 返回值

### IntersectionObserver
