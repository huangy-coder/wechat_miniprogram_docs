# wx.onNetworkStatusChange(function listener)

> 官方文档：[wx.onNetworkStatusChange(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.onNetworkStatusChange.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 网络 / wx.onNetworkStatusChange
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.1.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持
> **微信 Windows 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [弱网体验优化](https://developers.weixin.qq.com/miniprogram/dev/framework/performance/weak-network.html)、[网络调优](https://developers.weixin.qq.com/miniprogram/dev/framework/performance/network.html)

## 功能描述

监听网络状态变化事件

## 参数

### function listener

网络状态变化事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| isConnected | boolean | 当前是否有网络连接 |
| networkType | string | 网络类型 |

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
wx.onNetworkStatusChange(function (res) {
  console.log(res.isConnected)
  console.log(res.networkType)
})
```
