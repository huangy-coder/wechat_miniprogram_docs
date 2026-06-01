# wx.requestSubscribeMessage(Object object)

> 官方文档：[wx.requestSubscribeMessage(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/subscribe-message/wx.requestSubscribeMessage.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 订阅消息 / wx.requestSubscribeMessage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.4.4 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [3.4.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [小程序订阅消息](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message.html)

## 功能描述

调起客户端小程序订阅消息界面，返回用户订阅消息的操作结果。当用户勾选了订阅面板中的“总是保持以上选择，不再询问”时，模板消息会被添加到用户的小程序设置页，通过 [wx.getSetting](../setting/wx.getSetting.md) 接口可获取用户对相关模板消息的订阅状态。

## 注意事项

- 一次性模板 id 和永久模板 id 不可同时使用。
- 低版本基础库2.4.4~2.8.3 已支持订阅消息接口调用，仅支持传入一个一次性 tmplId / 永久 tmplId。
- [2.8.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 版本开始，用户发生点击行为或者发起支付回调后，才可以调起订阅消息界面。
- [2.10.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 版本开始，开发版和体验版小程序将禁止使用模板消息 formId。
- 一次授权调用里，每个tmplId对应的模板标题不能存在相同的，若出现相同的，只保留一个。
- [2.10.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 版本开始，支持订阅语音消息提醒，[详情](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message.html)

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| tmplIds | Array |   | 是 | 需要订阅的消息模板的id的集合，一次调用最多可订阅5条消息（注意：iOS客户端7.0.6版本、Android客户端7.0.7版本之后的一次性订阅/长期订阅才支持多个模板消息，iOS客户端7.0.5版本、Android客户端7.0.6版本之前的一次订阅只支持一个模板消息）消息模板id在[微信公众平台(mp.weixin.qq.com)-功能-订阅消息]中配置。每个tmplId对应的模板标题需要不相同，否则会被过滤。 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | String | 接口调用成功时errMsg值为'requestSubscribeMessage:ok' |
| [TEMPLATE_ID: string] | String | [TEMPLATE_ID]是动态的键，即模板id，值包括'accept'、'reject'、'ban'、'filter'。'accept'表示用户同意订阅该条id对应的模板消息，'reject'表示用户拒绝订阅该条id对应的模板消息，'ban'表示已被后台封禁，'filter'表示该模板因为模板标题同名被后台过滤。例如 { errMsg: "requestSubscribeMessage:ok", zun-LzcQyW-edafCVvzPkK4de2Rllr1fFpw2A_x0oXE: "accept"} 表示用户同意订阅zun-LzcQyW-edafCVvzPkK4de2Rllr1fFpw2A_x0oXE这条消息 |

#### object.fail 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | String | 接口调用失败错误信息 |
| errCode | Number | 接口调用失败错误码 |

## 错误码

| errCode | errMsg | 说明 |
| --- | --- | --- |
| 10001 | TmplIds can't be empty | 参数传空了 |
| 10002 | Request list fail | 网络问题，请求消息列表失败 |
| 10003 | Request subscribe fail | 网络问题，订阅请求发送失败 |
| 10004 | Invalid template id | 参数类型错误 |
| 10005 | Cannot show subscribe message UI | 无法展示 UI，一般是小程序这个时候退后台了导致的 |
| 20001 | No template data return, verify the template id exist | 没有模板数据，一般是模板 ID 不存在 或者和模板类型不对应 导致的 |
| 20002 | Templates type must be same | 模板消息类型 既有一次性的又有永久的 |
| 20003 | Templates count out of max bounds | 模板消息数量超过上限 |
| 20004 | The main switch is switched off | 用户关闭了主开关，无法进行订阅 |
| 20005 | This mini program was banned from subscribing messages | 小程序被禁封 |
| 20013 | Reject DeviceMsg Template | 不允许通过该接口订阅设备消息 |

## 示例代码

```js
wx.requestSubscribeMessage({
  tmplIds: [''],
  success (res) { }
})
```
