# UDPSocket.setTTL(number ttl)

> 官方文档：[UDPSocket.setTTL(number ttl)](https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.setTTL.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / UDP 通信 / UDPSocket / UDPSocket.setTTL
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.18.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)、[局域网通信](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/mDNS.html)

## 功能描述

设置 IP_TTL 套接字选项，用于设置一个 IP 数据包传输时允许的最大跳步数

## 参数

### number ttl

ttl 参数可以是 0 到 255 之间

## 示例代码

```javascript
  const udp = wx.createUDPSocket()
  udp.onListening(function () {
    udp.setTTL(64)
  })
  udp.bind()
```
