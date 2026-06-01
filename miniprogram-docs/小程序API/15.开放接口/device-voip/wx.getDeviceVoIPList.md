# wx.getDeviceVoIPList(Object object)

> 官方文档：[wx.getDeviceVoIPList(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/device-voip/wx.getDeviceVoIPList.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 音视频通话 / wx.getDeviceVoIPList
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.30.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [小程序音视频通话（for 硬件）](https://developers.weixin.qq.com/miniprogram/dev/framework/device/device-voip.html)

## 功能描述

查询当前用户授权的音视频通话设备（组）信息

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| list | Array.<Object> |   |

补充表：
| 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| sn | string | 设备唯一序列号。（仅单台设备时） |   |
| model_id | string | 设备型号 id。通过微信公众平台注册设备获得。（仅单台设备时） |   |
| group_id | string | 设备组的唯一标识 id（仅设备组时） | [2.30.4](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| status | number | 设备（组）授权状态。0：未授权；1：已授权 |   |

## 示例代码

```js
wx.getDeviceVoIPList({
  success(res) {
    console.log(res)
  },
  fail(res) {
    console.log(res)
  }
})
```
