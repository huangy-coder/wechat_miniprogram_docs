# wx.onAccelerometerChange(function listener)

> 官方文档：[wx.onAccelerometerChange(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.onAccelerometerChange.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 加速计 / wx.onAccelerometerChange
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听加速度数据事件。频率根据 [wx.startAccelerometer()](wx.startAccelerometer.md) 的 interval 参数, 接口调用后会自动开始监听。

## 参数

### function listener

加速度数据事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | X 轴 |
| y | number | Y 轴 |
| z | number | Z 轴 |

## 示例代码

```js
wx.onAccelerometerChange(callback)
```
