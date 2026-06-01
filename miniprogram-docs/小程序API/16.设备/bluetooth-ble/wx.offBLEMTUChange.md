# wx.offBLEMTUChange(function listener)

> 官方文档：[wx.offBLEMTUChange(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.offBLEMTUChange.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 蓝牙-低功耗中心设备 / wx.offBLEMTUChange
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.20.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [蓝牙低功耗 (BLE)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/ble.html)

## 功能描述

移除蓝牙低功耗的最大传输单元变化事件的监听函数

## 参数

### function listener

onBLEMTUChange 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```js
const listener = function (res) { console.log(res) }

wx.onBLEMTUChange(listener)
wx.offBLEMTUChange(listener) // 需传入与监听时同一个的函数对象
```
