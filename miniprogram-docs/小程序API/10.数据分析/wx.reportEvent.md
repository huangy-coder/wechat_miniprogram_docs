# wx.reportEvent(string eventId, object data)

> 官方文档：[wx.reportEvent(string eventId, object data)](https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.reportEvent.html)
> 所属分类：[数据分析](数据分析目录.md)
> 导航路径：数据分析 / wx.reportEvent
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.14.4 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

事件上报

## 参数

### string eventId

在 mp 实验系统中设置的事件英文名

### object data

可被 JSON.stringify 的对象，将一起上报至系统
