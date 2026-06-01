# UDPSocket.connect(Object object)

> 官方文档：[UDPSocket.connect(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.connect.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / UDP 通信 / UDPSocket / UDPSocket.connect
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.15.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.11.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)、[局域网通信](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/mDNS.html)

## 功能描述

预先连接到指定的 IP 和 port，需要配合 write 方法一起使用

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| address | string |   | 是 | 要发消息的地址 |
| port | number |   | 是 | 要发送消息的端口号 |

## 示例代码

```javascript
  const udp = wx.createUDPSocket()
  udp.bind()
  udp.connect({
    address: '192.168.193.2',
    port: 8848,
  })
  udp.write({
    address: '192.168.193.2',
    port: 8848,
    message: 'hello, how are you'
  })
```
