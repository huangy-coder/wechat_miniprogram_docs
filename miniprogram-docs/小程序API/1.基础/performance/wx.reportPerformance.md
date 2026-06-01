# wx.reportPerformance(Number id, Number value, String|Array dimensions)

> 官方文档：[wx.reportPerformance(Number id, Number value, String|Array dimensions)](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.reportPerformance.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 性能 / wx.reportPerformance
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.9.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.9.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [小程序测速](https://developers.weixin.qq.com/miniprogram/dev/framework/performanceReport/index.html)

## 功能描述

小程序测速上报。使用前，需要在小程序管理后台配置。

## 参数

### Number id

指标 id

### Number value

需要上报的数值

### String|Array dimensions

自定义维度 (选填)

## 示例代码

```js
wx.reportPerformance(1101, 680)
wx.reportPerformance(1101, 680, 'custom')
```
