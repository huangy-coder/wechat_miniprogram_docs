# BLEPeripheralServer

> 官方文档：[BLEPeripheralServer](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 蓝牙-低功耗外围设备 / BLEPeripheralServer
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.10.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [蓝牙介绍](https://developers.weixin.qq.com/miniprogram/dev/framework/device/bluetooth.html)

外围设备的服务端

## 方法

### BLEPeripheralServer.addService(Object object)

添加服务。

### BLEPeripheralServer.removeService(Object object)

移除服务。

### BLEPeripheralServer.startAdvertising(Object Object)

开始广播本地创建的外围设备。

### BLEPeripheralServer.stopAdvertising()

停止广播。

### BLEPeripheralServer.writeCharacteristicValue(Object Object)

往指定特征写入二进制数据值，并通知已连接的主机，从机的特征值已发生变化，该接口会处理是走回包还是走订阅。

### BLEPeripheralServer.onCharacteristicWriteRequest(function listener)

监听已连接的设备请求写当前外围设备的特征值事件。收到该消息后需要立刻调用 [writeCharacteristicValue](BLEPeripheralServer.writeCharacteristicValue.md) 写回数据，否则主机不会收到响应。

### BLEPeripheralServer.offCharacteristicWriteRequest(function listener)

移除已连接的设备请求写当前外围设备的特征值事件的监听函数

### BLEPeripheralServer.onCharacteristicReadRequest(function listener)

监听已连接的设备请求读当前外围设备的特征值事件。收到该消息后需要立刻调用 [writeCharacteristicValue](BLEPeripheralServer.writeCharacteristicValue.md) 写回数据，否则主机不会收到响应。

### BLEPeripheralServer.offCharacteristicReadRequest(function listener)

移除已连接的设备请求读当前外围设备的特征值事件的监听函数

### BLEPeripheralServer.onCharacteristicSubscribed(function listener)

监听特征订阅事件，仅 iOS 支持。

### BLEPeripheralServer.offCharacteristicSubscribed(function listener)

移除特征订阅事件的监听函数

### BLEPeripheralServer.onCharacteristicUnsubscribed(function listener)

监听取消特征订阅事件，仅 iOS 支持。

### BLEPeripheralServer.offCharacteristicUnsubscribed(function listener)

移除取消特征订阅事件的监听函数
