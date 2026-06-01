# wx.onUserCaptureScreen(function listener)

> 官方文档：[wx.onUserCaptureScreen(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.onUserCaptureScreen.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 屏幕 / wx.onUserCaptureScreen
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.4.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听用户主动截屏事件。用户使用系统截屏按键截屏时触发，只能注册一个监听

## 参数

### function listener

用户主动截屏事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| query | string | 支持开发者自定义一键打开小程序时的 query | [3.3.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| promise | promise | 如果该参数存在，则其它的参数将会以 resolve 结果为准，如果一秒内不 resolve，分享会使用上面传入的默认参数 | [3.3.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 示例代码

页面要先调用wx.showShareMenu()来允许调用

```js
wx.onUserCaptureScreen(function (res) {
  console.log('用户截屏了')
  return {
    query: "parameter=test", // 通过截屏图片打开小程序的query参数
    promise: new Promise((resolve) => { // 通过promise延时传递小程序的query参数
      setTimeout(() => {
        resolve({
          query: "parameter=test2",
        })
      }, 1000) // 在1秒内对query进行解析
    })
  }
})
```
