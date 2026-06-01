# wx.onScreenRecordingStateChanged(function listener)

> 官方文档：[wx.onScreenRecordingStateChanged(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.onScreenRecordingStateChanged.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 屏幕 / wx.onScreenRecordingStateChanged
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.24.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 iOS 版**：支持
> **微信 Android 版**：不支持

## 功能描述

监听用户录屏事件。

## 参数

### function listener

用户录屏事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| state | string | 录屏状态 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| start | 开始录屏 |
| stop | 结束录屏 |

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
