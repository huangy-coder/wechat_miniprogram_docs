# PerformanceObserver.observe(Object options)

> 官方文档：[PerformanceObserver.observe(Object options)](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/PerformanceObserver.observe.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 性能 / PerformanceObserver / PerformanceObserver.observe
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

开始监听

## 参数

### Object options

设置 type 监听单个类型的指标，设置 entryTypes 监听多个类型指标。

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| type | string |   | 否 | 指标类型。不能和 entryTypes 同时使用 |
| entryTypes | Array.<string> |   | 否 | 指标类型列表。不能和 type 同时使用。 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| navigation | 路由 |
| render | 渲染 |
| script | 脚本 |
| loadPackage | 代码包下载 |
