# wx.getNetworkType(Object object)

> 官方文档：[wx.getNetworkType(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.getNetworkType.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 网络 / wx.getNetworkType
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [弱网体验优化](https://developers.weixin.qq.com/miniprogram/dev/framework/performance/weak-network.html)、[网络调优](https://developers.weixin.qq.com/miniprogram/dev/framework/performance/network.html)

## 功能描述

获取网络类型

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

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| networkType | string | 网络类型 |   |
| signalStrength | Number | 信号强弱，单位 dbm |   |
| hasSystemProxy | Boolean | 设备是否使用了网络代理 | [2.22.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| weakNet | Boolean | 是否处于弱网环境 | [3.5.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

补充表：
| 合法值 | 说明 |
| --- | --- |
| wifi | wifi 网络 |
| 2g | 2g 网络 |
| 3g | 3g 网络 |
| 4g | 4g 网络 |
| 5g | 5g 网络 |
| unknown | Android 下不常见的网络类型 |
| none | 无网络 |

## 示例代码

```js
wx.getNetworkType({
  success (res) {
    const networkType = res.networkType
    const weakNet = res.weakNet
  }
})
```
