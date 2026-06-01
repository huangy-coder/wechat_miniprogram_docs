# wx.onBLEPeripheralConnectionStateChanged(function listener)

> 官方文档：[wx.onBLEPeripheralConnectionStateChanged(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/wx.onBLEPeripheralConnectionStateChanged.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 蓝牙-低功耗外围设备 / wx.onBLEPeripheralConnectionStateChanged
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.10.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.22.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听当前外围设备被连接或断开连接事件

## 参数

### function listener

当前外围设备被连接或断开连接事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| deviceId | String | 连接状态变化的设备 id |
| serverId | String | server 的 UUID |
| connected | Boolean | 连接目前状态 |
