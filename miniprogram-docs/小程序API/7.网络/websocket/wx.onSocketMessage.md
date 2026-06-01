# wx.onSocketMessage(function listener)

> 官方文档：[wx.onSocketMessage(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.onSocketMessage.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / WebSocket / wx.onSocketMessage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

推荐使用 [SocketTask](SocketTask.md) 的方式去管理 webSocket 链接，每一条链路的生命周期都更加可控，同时存在多个 webSocket 的链接的情况下使用 wx 前缀的方法可能会带来一些和预期不一致的情况。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)、[局域网通信](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/mDNS.html)

## 功能描述

监听 WebSocket 接收到服务器的消息事件。

## 参数

### function listener

WebSocket 接收到服务器的消息事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| data | string/ArrayBuffer | 服务器返回的消息 |
