# wx.reportMonitor(string name, number value)

> 官方文档：[wx.reportMonitor(string name, number value)](https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.reportMonitor.html)
> 所属分类：[数据分析](数据分析目录.md)
> 导航路径：数据分析 / wx.reportMonitor
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

从基础库 [2.31.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [wx.reportEvent](wx.reportEvent.md) 代替

> 基础库 2.0.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

自定义业务数据监控上报接口。

## 参数

### string name

监控ID，在「小程序管理后台」新建数据指标后获得

### number value

上报数值，经处理后会在「小程序管理后台」上展示每分钟的上报总量

## 使用说明

使用前，需要在「小程序管理后台-运维中心-性能监控-业务数据监控」中新建监控事件，配置监控描述与告警类型。每一个监控事件对应唯一的监控ID，开发者最多可以创建128个监控事件。

## 示例代码

```js
wx.reportMonitor('1', 1)
```
