# wx.openStoreCouponDetail(Object object)

> 官方文档：[wx.openStoreCouponDetail(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/store/wx.openStoreCouponDetail.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 微信小店 / wx.openStoreCouponDetail
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.8.5 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：不支持

> 相关文档: [微信小店指引](https://developers.weixin.qq.com/doc/store/API/basics/component.html)

## 功能描述

打开微信小店优惠券详情页

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| couponId | string |   | 是 | 优惠券id，可以通过[小店后台](https://store.weixin.qq.com/shop/marketing/coupon)获取 |   |
| shopAppid | string |   | 是 | 小店appid，可以通过[小店后台](https://store.weixin.qq.com/shop/setting/home)获取 |   |
| promoterShareLink | string |   | 是 | 推客参数，可以通过[接口](https://developers.weixin.qq.com/doc/store/leagueheadsupplier/API/promotion/content/coupon/getcouponpromotersharelink.html)获取。 | [3.8.11](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

#### object.fail 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| message | string | 错误信息 |
| code | number | 错误码 |
