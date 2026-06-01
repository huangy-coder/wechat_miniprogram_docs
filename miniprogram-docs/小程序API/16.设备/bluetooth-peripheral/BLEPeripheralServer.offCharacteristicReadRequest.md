# BLEPeripheralServer.offCharacteristicReadRequest(function listener)

> 官方文档：[BLEPeripheralServer.offCharacteristicReadRequest(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.offCharacteristicReadRequest.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 蓝牙-低功耗外围设备 / BLEPeripheralServer / BLEPeripheralServer.offCharacteristicReadRequest
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.10.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [蓝牙介绍](https://developers.weixin.qq.com/miniprogram/dev/framework/device/bluetooth.html)

## 功能描述

移除已连接的设备请求读当前外围设备的特征值事件的监听函数

## 参数

### function listener

onCharacteristicReadRequest 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```js
const listener = function (res) { console.log(res) }

BLEPeripheralServer.onCharacteristicReadRequest(listener)
BLEPeripheralServer.offCharacteristicReadRequest(listener) // 需传入与监听时同一个的函数对象
```
