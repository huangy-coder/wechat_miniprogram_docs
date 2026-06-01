# wx.onBatteryInfoChange(function listener)

> 官方文档：[wx.onBatteryInfoChange(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/battery/wx.onBatteryInfoChange.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 电量 / wx.onBatteryInfoChange
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.5.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 Windows 版**：支持

## 功能描述

监听电池信息变化事件，目前只支持监听省电模式的切换

## 参数

### function listener

电池信息变化事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| isLowPowerModeEnabled | boolean | 是否处于省电模式 |

## 示例代码

```js
const cb = res => {
  console.log(res.isLowPowerModeEnabled)
}
wx.onBatteryInfoChange(cb)
// 取消监听
wx.offBatteryInfoChange(cb)
```
