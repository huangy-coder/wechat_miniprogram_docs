# EventChannel

> 官方文档：[EventChannel](https://developers.weixin.qq.com/miniprogram/dev/api/route/EventChannel.html)
> 所属分类：[路由](路由目录.md)
> 导航路径：路由 / EventChannel
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.7.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

页面间事件通信通道

## 方法

### EventChannel.emit(string eventName, any args)

触发一个事件

### EventChannel.on(string eventName, EventCallback fn)

持续监听一个事件

### EventChannel.once(string eventName, EventCallback fn)

监听一个事件一次，触发后失效

### EventChannel.off(string eventName, EventCallback fn)

取消监听一个事件。给出第二个参数时，只取消给出的监听函数，否则取消所有监听函数
