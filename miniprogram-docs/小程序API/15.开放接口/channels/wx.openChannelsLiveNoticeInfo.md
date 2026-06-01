# wx.openChannelsLiveNoticeInfo(Object object)

> 官方文档：[wx.openChannelsLiveNoticeInfo(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.openChannelsLiveNoticeInfo.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 视频号 / wx.openChannelsLiveNoticeInfo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.13.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：不支持

> 相关文档: [视频号直播](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/channels-live.html)

## 功能描述

打开视频号直播预告半屏

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| finderUserName | string |   | 是 | 视频号 id，以"sph"开头的id，可在视频号助手获取 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |
