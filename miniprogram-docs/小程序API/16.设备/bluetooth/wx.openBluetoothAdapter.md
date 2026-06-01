# wx.openBluetoothAdapter(Object object)

> 官方文档：[wx.openBluetoothAdapter(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.openBluetoothAdapter.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 蓝牙-通用 / wx.openBluetoothAdapter
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.1.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **[用户授权](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/authorize.html)**：需要 scope.bluetooth
> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [蓝牙介绍](https://developers.weixin.qq.com/miniprogram/dev/framework/device/bluetooth.html)

## 功能描述

初始化蓝牙模块。iOS 上开启主机/从机（外围设备）模式时需分别调用一次，并指定对应的 `mode`。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| mode | string | central | 否 | 蓝牙模式，可作为主/从设备，仅 iOS 需要。 | [2.10.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

补充表：
| 合法值 | 说明 |
| --- | --- |
| central | 主机模式 |
| peripheral | 从机（外围设备）模式 |

## 错误

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | ok | 正常 |
| -1 | already connect | 已连接 |
| 10000 | not init | 未初始化蓝牙适配器 |
| 10001 | not available | 当前蓝牙适配器不可用 |
| 10002 | no device | 没有找到指定设备 |
| 10003 | connection fail | 连接失败 |
| 10004 | no service | 没有找到指定服务 |
| 10005 | no characteristic | 没有找到指定特征 |
| 10006 | no connection | 当前连接已断开 |
| 10007 | property not support | 当前特征不支持此操作 |
| 10008 | system error | 其余所有系统上报的异常 |
| 10009 | system not support | Android 系统特有，系统版本低于 4.3 不支持 BLE |
| 10012 | operate time out | 连接超时 |
| 10013 | invalid_data | 连接 deviceId 为空或者是格式不正确 |

## object.fail 回调函数返回的 state 参数（仅 iOS）

| 状态码 | 说明 |
| --- | --- |
| 0 | 未知 |
| 1 | 重置中 |
| 2 | 不支持 |
| 3 | 未授权 |
| 4 | 未开启 |

## 注意

- 其他蓝牙相关 API 必须在 [wx.openBluetoothAdapter](wx.openBluetoothAdapter.md) 调用之后使用。否则 API 会返回错误（errCode=10000）。
- 在用户蓝牙开关未开启或者手机不支持蓝牙功能的情况下，调用 [wx.openBluetoothAdapter](wx.openBluetoothAdapter.md) 会返回错误（errCode=10001），表示手机蓝牙功能不可用。此时小程序蓝牙模块已经初始化完成，可通过 [wx.onBluetoothAdapterStateChange](wx.onBluetoothAdapterStateChange.md) 监听手机蓝牙状态的改变，也可以调用蓝牙模块的所有API。

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/pQU51zmz7a3K)

```js
wx.openBluetoothAdapter({
  success (res) {
    console.log(res)
  }
})
```
