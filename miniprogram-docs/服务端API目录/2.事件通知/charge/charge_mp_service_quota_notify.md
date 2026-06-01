# 付费管理订单用量告警事件

> 官方文档：[付费管理订单用量告警事件](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/charge/charge_mp_service_quota_notify.html)
> 所属分类：[事件通知](../事件通知目录.md)
> 导航路径：事件通知 / 付费管理
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 本文档描述服务器端接收的消息或事件，详细说明参见[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)。

事件英文名：charge_mp_service_quota_notify

小程序开发者在付费管理所购买的订单，在配置消息推送地址后，可以接收到所购买的订单的用量告警事件。

此事件消息的推送时机：所购SPU的余量为 `20%`、`10%`、`5%`、`0%`。

## 1. 消息参数

### 请求体 Request Payload

## 2. 消息返回

### 返回体 Response Payload

回复 `success` 或空字符串（无需加密）

## 3. 注意事项

本事件无特殊注意事项

## 4. 代码示例

本事件无代码示例
