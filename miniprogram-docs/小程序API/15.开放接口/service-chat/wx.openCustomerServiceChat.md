# wx.openCustomerServiceChat(Object object)

> 官方文档：[wx.openCustomerServiceChat(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/service-chat/wx.openCustomerServiceChat.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 微信客服 / wx.openCustomerServiceChat
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.19.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 鸿蒙 OS 版**：支持
> **限制**：仅在点击行为时调用

## 功能描述

打开微信客服，页面产生点击事件后才可调用。了解更多信息，可以参考[微信客服介绍](https://work.weixin.qq.com/kf/)。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| extInfo | Object |   | 是 | 客服信息 |
| corpId | String |   | 是 | 企业ID |
| showMessageCard | Boolean | false | 否 | 是否发送小程序气泡消息 |
| sendMessageTitle | String |   | 否 | 气泡消息标题 |
| sendMessagePath | String |   | 否 | 气泡消息小程序路径 |
| sendMessageImg | String |   | 否 | 气泡消息图片 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

补充表：
| 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | String |   | 是 | 客服链接 |

## 示例代码

```js
wx.openCustomerServiceChat({
  extInfo: {url: ''},
  corpId: '',
  success(res) {}
})
```
