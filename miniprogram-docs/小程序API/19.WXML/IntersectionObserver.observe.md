# IntersectionObserver.observe(string targetSelector, function callback)

> 官方文档：[IntersectionObserver.observe(string targetSelector, function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/IntersectionObserver.observe.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / IntersectionObserver / IntersectionObserver.observe
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持

> 相关文档: [获取界面上的节点信息](https://developers.weixin.qq.com/miniprogram/dev/framework/view/selector.html)

## 功能描述

指定目标节点并开始监听相交状态变化情况

## 参数

### string targetSelector

选择器

### function callback

监听相交状态变化的回调函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 节点 ID |
| dataset | Record.<string, any> | 节点自定义数据属性 |
| intersectionRatio | number | 相交比例 |
| intersectionRect | Object | 相交区域的边界 |
| boundingClientRect | Object | 目标边界 |
| relativeRect | Object | 参照区域的边界 |
| time | number | 相交检测时的时间戳 |

补充表：
| 结构属性 | 类型 | 说明 |
| --- | --- | --- |
| left | number | 左边界 |
| right | number | 右边界 |
| top | number | 上边界 |
| bottom | number | 下边界 |
| width | number | 宽度 |
| height | number | 高度 |

补充表：
| 结构属性 | 类型 | 说明 |
| --- | --- | --- |
| left | number | 左边界 |
| right | number | 右边界 |
| top | number | 上边界 |
| bottom | number | 下边界 |
| width | number | 宽度 |
| height | number | 高度 |

补充表：
| 结构属性 | 类型 | 说明 |
| --- | --- | --- |
| left | number | 左边界 |
| right | number | 右边界 |
| top | number | 上边界 |
| bottom | number | 下边界 |
