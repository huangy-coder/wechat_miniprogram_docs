# wx.getChannelsShareKey(Object object)

> 官方文档：[wx.getChannelsShareKey(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.getChannelsShareKey.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 视频号 / wx.getChannelsShareKey
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.22.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

获取视频号直播卡片/视频卡片的分享来源，仅当卡片携带了分享信息、同时用户已授权该小程序获取视频号分享信息且启动场景值为 1177、1184、1195、1208 时可用。

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
| sharerOpenId | string | 分享者 openid |
| promoter | Object | 推广员 |

补充表：
| 结构属性 | 类型 | 说明 |
| --- | --- | --- |
| finderNickname | string | 推广员昵称 |
| promoterId | string | 推广员 id |
| promoterOpenId | string | 推广员 openid |
