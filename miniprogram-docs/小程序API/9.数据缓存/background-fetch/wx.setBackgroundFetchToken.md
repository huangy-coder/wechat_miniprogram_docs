# wx.setBackgroundFetchToken(object object)

> 官方文档：[wx.setBackgroundFetchToken(object object)](https://developers.weixin.qq.com/miniprogram/dev/api/storage/background-fetch/wx.setBackgroundFetchToken.html)
> 所属分类：[数据缓存](../数据缓存目录.md)
> 导航路径：数据缓存 / 数据预拉取和周期性更新 / wx.setBackgroundFetchToken
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.8.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [周期性更新](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/background-fetch.html)、[数据预拉取](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/pre-fetch.html)

## 功能描述

设置自定义登录态，在周期性拉取数据时带上，便于第三方服务器验证请求合法性

## 参数

### object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| token | String |   | 是 | 自定义的登录态。上限 1024 字符。 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |
