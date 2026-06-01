# wx.requirePrivacyAuthorize(Object object)

> 官方文档：[wx.requirePrivacyAuthorize(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/privacy/wx.requirePrivacyAuthorize.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 隐私信息授权 / wx.requirePrivacyAuthorize
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.32.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

模拟隐私接口调用，并触发隐私弹窗逻辑。隐私合规开发指南详情可见[《小程序隐私协议开发指南》](https://developers.weixin.qq.com/miniprogram/dev/framework/user-privacy/PrivacyAuthorize.html)

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

## 具体说明：

1. 调用 wx.requirePrivacyAuthorize() 时：

  1. 如果用户之前已经同意过隐私授权，会立即返回success回调，不会触发 wx.onNeedPrivacyAuthorization 事件。
  1. 如果用户之前没有授权过，并且开发者注册了 [wx.onNeedPrivacyAuthorization()](wx.onNeedPrivacyAuthorization.md) 事件监听，就会立即触发 wx.onNeedPrivacyAuthorization 事件，然后开发者在 onNeedPrivacyAuthorization 回调中弹出自定义隐私授权弹窗，用户点了同意后开发者调用 wx.onNeedPrivacyAuthorization 的回调接口 resolve({ event: 'agree', buttonId: 'agree-btn' })，会触发 requirePrivacyAuthorize 的 success 回调。开发者调用 wx.onNeedPrivacyAuthorization 的回调接口 resolve({ event: 'disagree' }) 的话，会触发 requirePrivacyAuthorize 的 fail 回调。
  1. 基于上述特性，开发者可以在调用任何真实隐私接口之前调用 wx.requirePrivacyAuthorize 接口来模拟隐私接口调用，并触发隐私弹窗逻辑。

1. 一定要调用 wx.requirePrivacyAuthorize 接口吗？

- 不是，wx.requirePrivacyAuthorize 只是一个辅助接口，可以根据实际情况选择使用。

## 示例代码

```html
// page.wxml
<view wx:if="{{showPrivacy}}">
  <view>隐私弹窗内容....</view>
  <button id="agree-btn" open-type="agreePrivacyAuthorization" bindagreeprivacyauthorization="handleAgreePrivacyAuthorization">同意</button>
</view>
```

```js
// page.js
Page({
  data: {
    showPrivacy: false
  },
  onLoad() {
    wx.onNeedPrivacyAuthorization(resolve => {
      // 需要用户同意隐私授权时
      // 弹出开发者自定义的隐私授权弹窗
      this.setData({
        showPrivacy: true
      })
      this.resolvePrivacyAuthorization = resolve
    })

    wx.requirePrivacyAuthorize({
      success: () => {
        // 用户同意授权
        // 继续小程序逻辑
      },
      fail: () => {}, // 用户拒绝授权
      complete: () => {}
    })
  },
  handleAgreePrivacyAuthorization() {
    // 用户点击同意按钮后
    this.resolvePrivacyAuthorization({ buttonId: 'agree-btn', event: 'agree' })
  }
})
```

## 完整示例demo

demo1: 演示使用 `wx.getPrivacySetting` 和 `<button open-type="agreePrivacyAuthorization">` 在首页处理隐私弹窗逻辑
[https://developers.weixin.qq.com/s/gi71sGm67hK0](https://developers.weixin.qq.com/s/gi71sGm67hK0)

demo2: 演示使用 `wx.onNeedPrivacyAuthorization` 和 `<button open-type="agreePrivacyAuthorization">` 在多个页面处理隐私弹窗逻辑，同时演示了如何处理多个隐私接口同时调用。
[https://developers.weixin.qq.com/s/hndZUOmA7gKn](https://developers.weixin.qq.com/s/hndZUOmA7gKn)

demo3: 演示 `wx.onNeedPrivacyAuthorization`、`wx.requirePrivacyAuthorize`、`<button open-type="agreePrivacyAuthorization">` 和 `<input type="nickname">` 组件如何结合使用
[https://developers.weixin.qq.com/s/jX7xWGmA7UKa](https://developers.weixin.qq.com/s/jX7xWGmA7UKa)

demo4: 演示使用 `wx.onNeedPrivacyAuthorization` 和 `<button open-type="agreePrivacyAuthorization">` 在多个 tabBar 页面处理隐私弹窗逻辑。
[https://developers.weixin.qq.com/s/g6BWZGmt7XK9](https://developers.weixin.qq.com/s/g6BWZGmt7XK9)
