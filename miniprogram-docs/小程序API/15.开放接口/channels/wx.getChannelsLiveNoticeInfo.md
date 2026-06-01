# wx.getChannelsLiveNoticeInfo(Object object)

> 官方文档：[wx.getChannelsLiveNoticeInfo(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.getChannelsLiveNoticeInfo.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 视频号 / wx.getChannelsLiveNoticeInfo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.19.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [视频号直播](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/channels-live.html)

## 功能描述

获取视频号直播预告信息

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| finderUserName | string |   | 是 | 视频号 id，以“sph”开头的id，可在视频号助手获取 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| noticeId | string | 预告 id |   |
| status | number | 预告状态：0可用 1取消 2已用 |   |
| startTime | string | 开始时间 |   |
| headUrl | string | 直播封面 |   |
| nickname | string | 视频号昵称 |   |
| reservable | boolean | 是否可预约 |   |
| otherInfos | Array.<Object> | 除最近的一条预告信息外，其他的预告信息列表（注意：每次最多返回按时间戳增序排列的15个预告信息，其中时间最近的那个预告信息会在接口其他的返回参数中展示，其余的预告信息会在该字段中展示）。 | [2.24.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
