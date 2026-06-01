# wx.openSetting(Object object)

> 官方文档：[wx.openSetting(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/setting/wx.openSetting.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 设置 / wx.openSetting
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.1.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [2.10.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持
> **限制**：仅在点击行为时调用

> 相关文档: [授权](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/authorize.html)

## 功能描述

调起客户端小程序设置界面，返回用户设置的操作结果。**设置界面只会出现小程序已经向用户请求过的[权限](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/authorize.html)**。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| withSubscriptions | Boolean | false | 否 | 是否同时获取用户订阅消息的订阅状态，默认不获取。注意：withSubscriptions 只返回用户勾选过订阅面板中的“总是保持以上选择，不再询问”的订阅消息。 | [2.10.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| authSetting | [AuthSetting](AuthSetting.md) | 用户授权结果 |   |
| subscriptionsSetting | [SubscriptionsSetting](SubscriptionsSetting.md) | 用户订阅消息设置，接口参数`withSubscriptions`值为`true`时才会返回。 | [2.10.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

- 注意：[2.3.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 版本开始，用户发生点击行为后，才可以跳转打开设置页，管理授权信息。[详情](https://developers.weixin.qq.com/community/develop/doc/000cea2305cc5047af5733de751008)

## 示例代码

```js
wx.openSetting({
  success (res) {
    console.log(res.authSetting)
    // res.authSetting = {
    //   "scope.userInfo": true,
    //   "scope.userLocation": true
    // }
  }
})
```
