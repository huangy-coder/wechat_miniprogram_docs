# wx.offGetWifiList(function listener)

> 官方文档：[wx.offGetWifiList(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.offGetWifiList.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / Wi-Fi / wx.offGetWifiList
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.9.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.9.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [无线局域网 (Wi-Fi)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/wifi.html)

## 功能描述

移除获取到 Wi-Fi 列表数据事件的监听函数

## 参数

### function listener

onGetWifiList 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```js
const listener = function (res) { console.log(res) }

wx.onGetWifiList(listener)
wx.offGetWifiList(listener) // 需传入与监听时同一个的函数对象
```
