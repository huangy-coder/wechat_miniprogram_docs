# wx.onBLEMTUChange(function listener)

> 官方文档：[wx.onBLEMTUChange(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.onBLEMTUChange.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 蓝牙-低功耗中心设备 / wx.onBLEMTUChange
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.20.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [蓝牙低功耗 (BLE)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/ble.html)

## 功能描述

监听蓝牙低功耗的最大传输单元变化事件（仅安卓触发）。

## 参数

### function listener

蓝牙低功耗的最大传输单元变化事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| deviceId | string | 蓝牙设备 id |
| mtu | number | 最大传输单元 |

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/pQU51zmz7a3K)

```js
wx.onBLEMTUChange(function (res) {
  console.log('bluetooth mtu is', res.mtu)
})
```
