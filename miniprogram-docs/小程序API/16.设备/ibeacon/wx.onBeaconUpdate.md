# wx.onBeaconUpdate(function listener)

> 官方文档：[wx.onBeaconUpdate(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.onBeaconUpdate.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 蓝牙-信标(Beacon) / wx.onBeaconUpdate
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.2.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [蓝牙信标 (Beacon)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/beacon.html)

## 功能描述

监听 Beacon 设备更新事件，仅能注册一个监听

## 参数

### function listener

Beacon 设备更新事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| beacons | Array.<[BeaconInfo](BeaconInfo.md)> | 当前搜寻到的所有 Beacon 设备列表 |

## 示例代码

```js
wx.onBeaconUpdate(res => {
   console.log(res.beacons)
})
```
