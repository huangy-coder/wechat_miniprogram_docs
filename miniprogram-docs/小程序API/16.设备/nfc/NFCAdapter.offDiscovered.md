# NFCAdapter.offDiscovered(function listener)

> 官方文档：[NFCAdapter.offDiscovered(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.offDiscovered.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / NFC 读写 / NFCAdapter / NFCAdapter.offDiscovered
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持
> **微信 iOS 版**：不支持
> **微信 Android 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [近场通信 (NFC)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/nfc.html)

## 功能描述

移除 NFC Tag的监听函数

## 参数

### function listener

onDiscovered 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```js
const listener = function (res) { console.log(res) }

NFCAdapter.onDiscovered(listener)
NFCAdapter.offDiscovered(listener) // 需传入与监听时同一个的函数对象
```
