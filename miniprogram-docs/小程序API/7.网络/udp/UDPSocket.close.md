# UDPSocket.close()

> 官方文档：[UDPSocket.close()](https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.close.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / UDP 通信 / UDPSocket / UDPSocket.close
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.11.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)、[局域网通信](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/mDNS.html)

## 功能描述

关闭 UDP Socket 实例，相当于销毁。 在关闭之后，UDP Socket 实例不能再发送消息，每次调用 `UDPSocket.send` 将会触发错误事件，并且 message 事件回调函数也不会再也执行。在 `UDPSocket` 实例被创建后将被 Native 强引用，保证其不被 GC。在 `UDPSocket.close` 后将解除对其的强引用，让 UDPSocket 实例遵从 GC。
