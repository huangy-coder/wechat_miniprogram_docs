# wx.checkIsSupportFacialRecognition(Object object)

> 官方文档：[wx.checkIsSupportFacialRecognition(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/face/wx.checkIsSupportFacialRecognition.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 人脸检测 / wx.checkIsSupportFacialRecognition
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.8.12 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：不支持

> 相关文档: [微信人脸核身](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/cityservice/FacialRecognitionVerify.html)

## 功能描述

检查当前设备是否支持人脸识别能力

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

## 示例代码

```js
wx.checkIsSupportFacialRecognition({
  success() {
   // 支持人脸识别
  },
  fail() {
   // 不支持人脸识别
  },
})
```
