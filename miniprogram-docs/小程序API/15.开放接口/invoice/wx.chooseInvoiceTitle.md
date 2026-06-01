# wx.chooseInvoiceTitle(Object object)

> 官方文档：[wx.chooseInvoiceTitle(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/invoice/wx.chooseInvoiceTitle.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 发票 / wx.chooseInvoiceTitle
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.5.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [2.16.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

选择用户的发票抬头。当前小程序必须关联一个公众号，且这个公众号是完成了[微信认证](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1496554031_RD4xe)的，才能调用 chooseInvoiceTitle。

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

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| type | string | 抬头类型 |
| title | string | 抬头名称 |
| taxNumber | string | 抬头税号 |
| companyAddress | string | 单位地址 |
| telephone | string | 手机号码 |
| bankName | string | 银行名称 |
| bankAccount | string | 银行账号 |
| errMsg | string | 错误信息 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 0 | 单位 |
| 1 | 个人 |

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/GJ4S9nmQ7x2E)

```js
wx.chooseInvoiceTitle({
  success(res) {}
})
```
