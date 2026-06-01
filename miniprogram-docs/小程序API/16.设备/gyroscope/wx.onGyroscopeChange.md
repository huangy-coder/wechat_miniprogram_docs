# wx.onGyroscopeChange(function listener)

> 官方文档：[wx.onGyroscopeChange(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/gyroscope/wx.onGyroscopeChange.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 陀螺仪 / wx.onGyroscopeChange
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.3.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.9.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

监听陀螺仪数据变化事件。频率根据 [wx.startGyroscope()](wx.startGyroscope.md) 的 interval 参数。可以使用 [wx.stopGyroscope()](wx.stopGyroscope.md) 停止监听。

## 参数

### function listener

陀螺仪数据变化事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | x 轴的角速度 |
| y | number | y 轴的角速度 |
| z | number | z 轴的角速度 |
