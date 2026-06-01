# wx.requestDeviceVoIP(Object object)

> 官方文档：[wx.requestDeviceVoIP(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/device-voip/wx.requestDeviceVoIP.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 音视频通话 / wx.requestDeviceVoIP
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.27.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [小程序音视频通话（for 硬件）](https://developers.weixin.qq.com/miniprogram/dev/framework/device/device-voip.html)

## 功能描述

请求用户授权与设备（组）间进行音视频通话。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| sn | String |   | 是 | 设备唯一序列号。由厂商分配，长度不能超过128字节。字符只接受数字，大小写字母，下划线（_）和连字符（-）。 |   |
| snTicket | String |   | 是 | [设备票据](https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/hardware-device/getSnTicket.html)，5分钟内有效。 |   |
| modelId | String |   | 是 | 设备型号 id。通过微信公众平台注册设备获得。 |   |
| deviceName | String |   | 是 | 设备名称，将显示在授权弹窗内（长度不超过13）。授权框中「设备名字」= 「deviceName」 + 「modelId 对应设备型号」。 |   |
| isGroup | Boolean | false | 否 | 是否为授权设备组，默认 false 。 | [2.30.4](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| groupId | String |   | 是 | 设备组的唯一标识 id 。isGroup 为 true 时只需要传该参数，isGroup 为 false 时不需要传该参数，但需要传 sn、snTicket、modelId、deviceName 。 | [2.30.4](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

## 示例代码

```js
// 授权单台设备
wx.requestDeviceVoIP({
  sn: 'xxxx',
  snTicket: 'xxxxx',
  modelId: 'xxx',
  deviceName: 'xxx',
  success(res) {
    console.log(res)
  },
  fail(res) {
    console.log(res)
  }
})

// 批量授权（授权设备组）
wx.requestDeviceVoIP({
  isGroup: true,
  groupId: '设备组 ID',
  success(res) {
    console.log(res)
  },
  fail(res) {
    console.log(res)
  }
})
```
