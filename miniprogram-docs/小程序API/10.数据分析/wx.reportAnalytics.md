# wx.reportAnalytics(string eventName, Object data)

> 官方文档：[wx.reportAnalytics(string eventName, Object data)](https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.reportAnalytics.html)
> 所属分类：[数据分析](数据分析目录.md)
> 导航路径：数据分析 / wx.reportAnalytics
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

从基础库 [2.31.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [wx.reportEvent](wx.reportEvent.md) 代替

> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> 在小程序插件中使用时，可以被正常调用，但目前不会进行统计展示
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

自定义分析数据上报接口。使用前，需要在小程序管理后台自定义分析中新建事件，配置好事件名与字段。

## 参数

### string eventName

事件名

### Object data

上报的自定义数据，key 为配置中的字段名，value 为上报的数据。

## 示例代码

```js
wx.reportAnalytics('purchase', {
  price: 120,
  color: 'red'
})
```
