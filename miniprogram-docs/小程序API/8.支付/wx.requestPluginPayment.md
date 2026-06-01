# wx.requestPluginPayment(Object object)

> 官方文档：[wx.requestPluginPayment(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestPluginPayment.html)
> 所属分类：[支付](支付目录.md)
> 导航路径：支付 / wx.requestPluginPayment
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.22.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [2.22.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [插件支付功能页](https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/functional-pages/request-payment.html)

## 功能描述

插件中发起支付。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| version | string |   | 是 | 插件版本 |
| fee | number |   | 是 | 需要显示在页面中的金额，单位为分 |
| paymentArgs | Object |   | 是 | 任意数据，传递给功能页中的响应函数 |
| currencyType | string | CNY | 否 | 需要显示在页面中的货币符号的代码 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

补充表：
| 合法值 | 说明 |
| --- | --- |
| develop | 开发版 |
| trial | 体验版 |
| release | 正式版 |

## Tip

1. `tip`: 小程序与插件绑定在同一个open平台账号上且小程序与插件均为open账号的同主体/关联主体时，调用此接口将直接拉起支付收银台。
2. `tip`: 这个接口本身可以在开发者工具中使用，但功能页的跳转目前不支持在开发者工具中调试，请在真机上测试。
3. `tip`: 跳转支付功能页需要在 `app.json` 中配置 `"functionalPages": true`

## 示例代码

具体用法及参数说明可参考 [插件支付文档](https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/functional-pages/request-payment.html)

```js
wx.requestPluginPayment({
  version: 'release',
  fee: 1,
  paymentArgs: {},
  currencyType: 'CNY',
  success (res) { },
  fail (res) { }
})
```
