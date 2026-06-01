# TCPSocket.close()

> 官方文档：[TCPSocket.close()](https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.close.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / TCP 通信 / TCPSocket / TCPSocket.close
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)

## 功能描述

关闭连接

## 示例代码

```javascript
  const tcp = wx.createTCPSocket()
  tcp.close()
```
