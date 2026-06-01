# number UDPSocket.bind(number port)

> 官方文档：[number UDPSocket.bind(number port)](https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.bind.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / UDP 通信 / UDPSocket / UDPSocket.bind
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.11.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)、[局域网通信](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/mDNS.html)

## 功能描述

绑定一个系统随机分配的可用端口，或绑定一个指定的端口号

## 参数

### number port

> 基础库 2.9.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

指定要绑定的端口号，不传则返回系统随机分配的可用端口

## 返回值

### number

绑定成功的端口号

## 示例代码

```javascript
  const udp = wx.createUDPSocket()
  const port = udp.bind()
```
