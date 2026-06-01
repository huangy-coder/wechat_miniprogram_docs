# GlobalPayment wx.createGlobalPayment(Object object)

> 官方文档：[GlobalPayment wx.createGlobalPayment(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.createGlobalPayment.html)
> 所属分类：[支付](支付目录.md)
> 导航路径：支付 / wx.createGlobalPayment
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.7.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

创建全球支付方式的对象。一旦用户选定支付方式后，不可更改。如需重新选择支付方式，需创建新对象。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| mchRegion | string |   | 是 | 根据每笔订单实际的交易地区，提供地区编码，不同地区可能匹配不同的支付方式，参考 ISO3166二位字母代码标准，大写。 |
| isSandbox | string | false | 否 | true为开发环境，false为生产环境。不传入该参数，则默认为false，即生产环境。 |

## 返回值

### GlobalPayment
