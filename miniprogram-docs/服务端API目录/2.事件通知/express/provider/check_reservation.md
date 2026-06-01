# 查询所在城市的预约时间段

> 官方文档：[查询所在城市的预约时间段](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/check_reservation.html)
> 所属分类：[事件通知](../../事件通知目录.md)
> 导航路径：事件通知 / 物流助手 / 运力方使用 / 查询所在城市的预约时间段
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 本文档描述服务器端接收的消息或事件，详细说明参见[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)。

事件英文名：waybill_query_expect_time_range

当用户查询所在城市的预约时间段时，推送此事件。

## 1. 消息参数

### 请求体 Request Payload

## 2. 消息返回

### 返回体 Response Payload

### Res.ValidTimeRange(Array) Object Payload

可预约时间段

### Res.Asap Object Payload

是否可下单后2小时内上门，无此参数返回表示不支持

## 3. 注意事项

本事件无特殊注意事项

## 4. 代码示例

本事件无代码示例
