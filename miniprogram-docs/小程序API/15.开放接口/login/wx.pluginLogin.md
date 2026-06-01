# wx.pluginLogin(Object args)

> 官方文档：[wx.pluginLogin(Object args)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.pluginLogin.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 登录 / wx.pluginLogin
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [2.20.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

**该接口仅在小程序插件中可调用**，调用接口获得插件用户标志凭证（code）。插件可以此凭证换取用于识别用户的标识 openpid。用户不同、宿主小程序不同或插件不同的情况下，该标识均不相同，即当且仅当同一个用户在同一个宿主小程序中使用同一个插件时，openpid 才会相同。

## 参数

### Object args

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### args.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| code | string | 用于换取 openpid 的凭证（有效期五分钟）。插件开发者可以用此 code 在开发者服务器后台调用 [getPluginOpenPId](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/(getPluginOpenPId)) 换取 openpid。 |
