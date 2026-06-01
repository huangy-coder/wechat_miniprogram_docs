# RealtimeLogManager

> 官方文档：[RealtimeLogManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeLogManager.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 调试 / RealtimeLogManager
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [实时日志](https://developers.weixin.qq.com/miniprogram/dev/framework/realtimelog/index.html)

实时日志管理器实例，可以通过 [wx.getRealtimeLogManager](wx.getRealtimeLogManager.md) 获取。

## 方法

### RealtimeLogManager.info()

写 info 日志，暂不支持在插件使用

### RealtimeLogManager.warn()

写 warn 日志，暂不支持在插件使用

### RealtimeLogManager.error()

写 error 日志，暂不支持在插件使用

### RealtimeLogManager.setFilterMsg(string msg)

设置过滤关键字，暂不支持在插件使用

### RealtimeLogManager.addFilterMsg(string msg)

添加过滤关键字，暂不支持在插件使用

## 使用说明

为帮助小程序开发者快捷地排查小程序漏洞、定位问题，我们推出了实时日志功能。从基础库2.7.1开始，开发者可通过提供的接口打印日志，日志汇聚并实时上报到小程序后台。

开发者可从小程序管理后台“WE分析->性能质量->实时日志”进入小程序端日志查询页面，或从“小程序插件->实时日志”进入插件端日志查询页面，进而查看开发者打印的日志信息。
