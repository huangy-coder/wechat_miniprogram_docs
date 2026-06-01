# wx.offScreenRecordingStateChanged(function listener)

> 官方文档：[wx.offScreenRecordingStateChanged(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.offScreenRecordingStateChanged.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 屏幕 / wx.offScreenRecordingStateChanged
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.24.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 iOS 版**：支持
> **微信 Android 版**：不支持

## 功能描述

移除用户录屏事件的监听函数

## 参数

### function listener

onScreenRecordingStateChanged 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```javascript
// 监听用户录屏事件
const handler = function (res) {
  console.log(res.state)
}
wx.onScreenRecordingStateChanged(handler)

// 取消监听用户录屏事件
wx.offScreenRecordingStateChanged(handler)
```

## 示例代码

```js
const listener = function (res) { console.log(res) }

wx.onScreenRecordingStateChanged(listener)
wx.offScreenRecordingStateChanged(listener) // 需传入与监听时同一个的函数对象
```
