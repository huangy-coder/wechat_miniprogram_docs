# MediaQueryObserver.observe(Object descriptor, function callback)

> 官方文档：[MediaQueryObserver.observe(Object descriptor, function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/MediaQueryObserver.observe.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / MediaQueryObserver / MediaQueryObserver.observe
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持

## 功能描述

开始监听页面 media query 变化情况

## 参数

### Object descriptor

media query 描述符

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| minWidth | number |   | 否 | 页面最小宽度（ px 为单位） |
| maxWidth | number |   | 否 | 页面最大宽度（ px 为单位） |
| width | number |   | 否 | 页面宽度（ px 为单位） |
| minHeight | number |   | 否 | 页面最小高度（ px 为单位） |
| maxHeight | number |   | 否 | 页面最大高度（ px 为单位） |
| height | number |   | 否 | 页面高度（ px 为单位） |
| orientation | string |   | 否 | 屏幕方向（ `landscape` 或 `portrait` ） |

### function callback

监听 media query 状态变化的回调函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| matches | boolean | 页面的当前状态是否满足所指定的 media query |
