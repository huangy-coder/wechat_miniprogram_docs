# wx.onHCEMessage(function listener)

> 官方文档：[wx.onHCEMessage(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc-hce/wx.onHCEMessage.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / NFC 主机卡模拟 / wx.onHCEMessage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.9.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 iOS 版**：不支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [近场通信 (NFC)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/nfc.html)

## 功能描述

监听接收 NFC 设备消息事件。仅能注册一个监听

## 参数

### function listener

接收 NFC 设备消息事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| messageType | number | 消息类型 |
| data | ArrayBuffer | `messageType=1` 时 ,客户端接收到 NFC 设备的指令 |
| reason | number | `messageType=2` 时，原因 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 1 | HCE APDU Command类型，小程序需对此指令进行处理，并调用 sendHCEMessage 接口返回处理指令 |
| 2 | 设备离场事件类型 |
