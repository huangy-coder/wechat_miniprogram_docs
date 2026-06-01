# TCPSocket.bindWifi(Object options)

> 官方文档：[TCPSocket.bindWifi(Object options)](https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.bindWifi.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / TCP 通信 / TCPSocket / TCPSocket.bindWifi
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.25.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)

## 功能描述

将 TCP Socket 绑定到当前 wifi 网络，成功后会触发 onBindWifi 事件（仅安卓支持）

## 参数

### Object options

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| BSSID | string |   | 是 | 当前 wifi 网络的 BSSID ，可通过 wx.getConnectedWifi 获取 |

## 示例代码

```javascript
  const tcp = wx.createTCPSocket()
  tcp.bindWifi({ BSSID: 'xxx' })
  tcp.onBindWifi(() => {})
```
