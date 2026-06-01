# wx.requestFacialVerify(Object object)

> 官方文档：[wx.requestFacialVerify(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/face/wx.requestFacialVerify.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 人脸检测 / wx.requestFacialVerify
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.8.12 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：不支持

> 相关文档: [微信人脸核身](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/cityservice/FacialRecognitionVerify.html)

## 功能描述

对用户实名信息进行基于生物识别的人脸核身验证

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| verifyId | string |   | 是 | 人脸核身会话唯一标识（小程序后台根据「用户实名信息（姓名+身份证）」调用微信后台[getVerifyId](https://developers.weixin.qq.com/miniprogram/dev/server/API/face/api_getverifyid.html)接口获取） |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

## 错误

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 0 | 人脸识别完成（需要通过[queryVerifyInfo](https://developers.weixin.qq.com/miniprogram/dev/server/API/face/api_queryverifyinfo.html)接口查询人脸核身真实验证结果） |   |

## 示例代码

```js
wx.requestFacialVerify({
  // 人脸核身会话唯一标识
  verifyId: 'xxx',
  success() {
    // 人脸核身验证成功，需要通知小程序后台根据本次人脸核身会话唯一标识 verifyId 字段调用微信后台 queryVerifyInfo 接口查询人脸核身真实验证结果。
  },
  fail() {
    // 人脸核身验证失败
  },
})
```
