# NFCAdapter.onDiscovered(function listener)

> 官方文档：[NFCAdapter.onDiscovered(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.onDiscovered.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / NFC 读写 / NFCAdapter / NFCAdapter.onDiscovered
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持
> **微信 iOS 版**：不支持
> **微信 Android 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [近场通信 (NFC)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/nfc.html)

## 功能描述

监听 NFC Tag

## 参数

### function listener

的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| id | ArrayBuffer |   |
| techs | Array | tech 数组，用于匹配NFC卡片具体可以使用什么标准（NfcA等实例）处理 |
| messages | Array | 可选，NdefMessage 数组，消息格式为 {id: ArrayBuffer, type: ArrayBuffer, payload: ArrayBuffer} |
