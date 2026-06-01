# wx.onWifiConnectedWithPartialInfo(function listener)

> 官方文档：[wx.onWifiConnectedWithPartialInfo(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.onWifiConnectedWithPartialInfo.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / Wi-Fi / wx.onWifiConnectedWithPartialInfo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.22.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.22.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

> 相关文档: [无线局域网 (Wi-Fi)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/wifi.html)

## 功能描述

监听连接上 Wi-Fi 的事件

## 参数

### function listener

连接上 Wi-Fi 的事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| wifi | [WifiInfo](WifiInfo.md) | 只包含 SSID 属性的 WifiInfo 对象 |
