# wx.setBLEMTU(Object object)

> 官方文档：[wx.setBLEMTU(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.setBLEMTU.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 蓝牙-低功耗中心设备 / wx.setBLEMTU
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [2.11.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [蓝牙低功耗 (BLE)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/ble.html)

## 功能描述

协商设置蓝牙低功耗的最大传输单元 (Maximum Transmission Unit, MTU)。需在 [wx.createBLEConnection](wx.createBLEConnection.md) 调用成功后调用。仅安卓系统 5.1 以上版本有效，iOS 因系统限制不支持。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string |   | 是 | 蓝牙设备 id |
| mtu | number |   | 是 | 最大传输单元。设置范围为 (22,512) 区间内，单位 bytes |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| mtu | number | 最终协商的 MTU 值，与传入参数一致。安卓客户端 8.0.9 开始支持。 |

#### object.fail 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| mtu | number | 最终协商的 MTU 值。如果协商失败则无此参数。安卓客户端 8.0.9 开始支持。 |
