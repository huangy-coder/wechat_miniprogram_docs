# wx.onGetWifiList(function listener)

> 官方文档：[wx.onGetWifiList(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.onGetWifiList.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / Wi-Fi / wx.onGetWifiList
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.6.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.9.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [无线局域网 (Wi-Fi)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/wifi.html)

## 功能描述

监听获取到 Wi-Fi 列表数据事件

## 参数

### function listener

获取到 Wi-Fi 列表数据事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| wifiList | Array.<[WifiInfo](WifiInfo.md)> | Wi-Fi 列表数据 |
