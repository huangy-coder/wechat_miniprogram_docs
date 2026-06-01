# wx.getChannelsLiveInfo(Object object)

> 官方文档：[wx.getChannelsLiveInfo(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.getChannelsLiveInfo.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 视频号 / wx.getChannelsLiveInfo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.15.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [视频号直播](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/channels-live.html)

## 功能描述

获取视频号直播信息

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| finderUserName | string |   | 是 | 视频号 id，以“sph”开头的id，可在视频号助手获取 |   |
| startTime | number |   | 否 | 起始时间，筛选指定时间段的直播。若上传了endTime，未上传startTime，则startTime默认为0 | [2.29.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| endTime | number |   | 否 | 结束时间，筛选指定时间段的直播。若上传了startTime，未上传endTime，则endTime默认取当前时间 | [2.29.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| feedId | string | 直播 feedId |   |
| nonceId | string | 直播 nonceId |   |
| description | string | 直播主题 |   |
| status | number | 直播状态 |   |
| headUrl | string | 视频号头像 |   |
| nickname | string | 视频号昵称 |   |
| replayStatus | string | 直播回放状态 | [2.29.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| otherInfos | Array.<Object> | 除最近的一条直播外，其他的直播列表（注意：每次最多返回按时间戳增序排列的15个直播信息，其中时间最近的那个直播会在接口其他的返回参数中展示，其余的直播会在该字段中展示）。 | [2.29.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 1 | 直播状态不存在（针对未开过直播的主播） |
| 2 | 直播中 |
| 3 | 直播已结束 |
| 4 | 直播准备中（未开播） |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 0 | 未生成 |
| 1 | 已生成 |
| 3 | 生成中 |
| 6 | 已过期 |

## 常见错误码说明

100008 视频号需要认证
40097 入参异常
1416104 视频号获取到的数据为空
1416100 非法的视频号id
