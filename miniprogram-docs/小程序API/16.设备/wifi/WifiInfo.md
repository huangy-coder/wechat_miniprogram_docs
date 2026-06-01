# WifiInfo

> 官方文档：[WifiInfo](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/WifiInfo.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / Wi-Fi / WifiInfo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [无线局域网 (Wi-Fi)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/wifi.html)

Wifi 信息

## 属性

### string SSID

Wi-Fi 的 SSID

### string BSSID

Wi-Fi 的 BSSID

### boolean secure

Wi-Fi 是否安全

### number signalStrength

Wi-Fi 信号强度, 安卓取值 0 ～ 100 ，iOS 取值 0 ～ 1 ，值越大强度越大

### number frequency

> 基础库 2.12.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

Wi-Fi 频段单位 MHz

## 注意

- 安卓 wx.connectWifi / wx.getConnectedWifi 若设置了 partialInfo:true ，或者调用了 wx.onWifiConnectedWithPartialInfo 事件。将会返回只包含 SSID 属性的 WifiInfo 对象。
- iOS wx.getConnectedWifi 若设置了 partialInfo:true ，将会返回只包含 SSID、BSSID 属性的 WifiInfo 对象，且需要用户开启微信定位权限才能正确返回结果。
- 在某些情况下，可能 Wi-Fi 已经连接成功，但会因为获取不到完整的 WifiInfo 对象报错。具体错误信息为 errCode: 12010, errMsg: can't gain current wifi 或 no wifi is connected 。如果开发者不需要完整的 WifiInfo 对象，则可以通过采取上述策略解决报错问题。
