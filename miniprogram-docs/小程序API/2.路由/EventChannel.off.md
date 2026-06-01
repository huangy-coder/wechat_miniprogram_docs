# EventChannel.off(string eventName, function fn)

> 官方文档：[EventChannel.off(string eventName, function fn)](https://developers.weixin.qq.com/miniprogram/dev/api/route/EventChannel.off.html)
> 所属分类：[路由](路由目录.md)
> 导航路径：路由 / EventChannel / EventChannel.off
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.7.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

## 功能描述

取消监听一个事件。给出第二个参数时，只取消给出的监听函数，否则取消所有监听函数

## 参数

### string eventName

事件名称

### function fn

事件监听函数

#### 参数

##### any args

触发事件参数
