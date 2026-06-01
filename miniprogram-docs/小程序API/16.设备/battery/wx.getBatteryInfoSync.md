# Object wx.getBatteryInfoSync()

> 官方文档：[Object wx.getBatteryInfoSync()](https://developers.weixin.qq.com/miniprogram/dev/api/device/battery/wx.getBatteryInfoSync.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 电量 / wx.getBatteryInfoSync
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [2.15.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

[wx.getBatteryInfo](wx.getBatteryInfo.md) 的同步版本

## 返回值

### Object res

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| level | number | 设备电量，范围 1 - 100 |   |
| isCharging | boolean | 是否正在充电中 |   |
| isLowPowerModeEnabled | boolean | 是否处于省电模式 | [3.5.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
