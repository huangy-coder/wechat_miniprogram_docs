# UDPSocket.send(Object object)

> 官方文档：[UDPSocket.send(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.send.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / UDP 通信 / UDPSocket / UDPSocket.send
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.11.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)、[局域网通信](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/mDNS.html)

## 功能描述

向指定的 IP 和 port 发送消息。基础库 2.9.0 起支持广播 (指定地址为 255.255.255.255)。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| address | string |   | 是 | 要发消息的地址。在基础库 <= 2.9.3 版本必须是和本机同网段的 IP 地址，或安全域名列表内的域名地址；之后版本可以是任意 IP 和域名 |
| port | number |   | 是 | 要发送消息的端口号 |
| message | string/ArrayBuffer |   | 是 | 要发送的数据 |
| offset | number | 0 | 否 | 发送数据的偏移量，仅当 message 为 ArrayBuffer 类型时有效 |
| length | number | message.byteLength | 否 | 发送数据的长度，仅当 message 为 ArrayBuffer 类型时有效 |
| setBroadcast | boolean | false | 否 | 向指定地址发消息时，是否要开启广播，基础库 2.24.0 开始支持 |

## 示例代码

```javascript
  const udp = wx.createUDPSocket()
  udp.bind()
  udp.send({
    address: '192.168.193.2',
    port: 8848,
    message: 'hello, how are you'
  })
```
