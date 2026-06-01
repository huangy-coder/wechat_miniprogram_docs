# TCPSocket.onMessage(function listener)

> 官方文档：[TCPSocket.onMessage(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.onMessage.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / TCP 通信 / TCPSocket / TCPSocket.onMessage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)

## 功能描述

监听当接收到数据的时触发该事件

## 参数

### function listener

当接收到数据的时触发该事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| message | ArrayBuffer | 收到的消息 |
| remoteInfo | Object | 发送端地址信息 |
| localInfo | Object | 接收端地址信息 |

补充表：
| 结构属性 | 类型 | 说明 |
| --- | --- | --- |
| address | string | 发送消息的 socket 的地址 |
| family | string | 使用的协议族，为 IPv4 或者 IPv6 |
| port | number | 端口号 |

补充表：
| 结构属性 | 类型 | 说明 |
| --- | --- | --- |
| address | string | 接收消息的 socket 的地址 |
| family | string | 使用的协议族，为 IPv4 或者 IPv6 |
| port | number | 端口号 |
