# BLEPeripheralServer.onCharacteristicReadRequest(function listener)

> 官方文档：[BLEPeripheralServer.onCharacteristicReadRequest(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.onCharacteristicReadRequest.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 蓝牙-低功耗外围设备 / BLEPeripheralServer / BLEPeripheralServer.onCharacteristicReadRequest
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.10.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [蓝牙介绍](https://developers.weixin.qq.com/miniprogram/dev/framework/device/bluetooth.html)

## 功能描述

监听已连接的设备请求读当前外围设备的特征值事件。收到该消息后需要立刻调用 [writeCharacteristicValue](BLEPeripheralServer.writeCharacteristicValue.md) 写回数据，否则主机不会收到响应。

## 参数

### function listener

已连接的设备请求读当前外围设备的特征值事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| serviceId | String | 蓝牙特征对应服务的 UUID |
| characteristicId | String | 蓝牙特征的 UUID |
| callbackId | Number | 唯一标识码，调用 [writeCharacteristicValue](BLEPeripheralServer.writeCharacteristicValue.md) 时使用 |
