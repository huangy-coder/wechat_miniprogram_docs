# 查询订单状态

> 官方文档：[查询订单状态](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/check_order_status.html)
> 所属分类：[事件通知](../../事件通知目录.md)
> 导航路径：事件通知 / 物流助手 / 运力方使用 / 查询订单状态
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 本文档描述服务器端接收的消息或事件，详细说明参见[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)。

事件英文名：waybill_notify_query

微信在收到运力方的消息推送请求后会反查一次当前单的状态，如果与请求一致时则会推送

## 1. 消息参数

### 请求体 Request Payload

## 2. 消息返回

### 返回体 Response Payload

### Res.Path(Array) Object Payload

所有物流轨迹

## 3. 注意事项

本事件无特殊注意事项

## 4. 代码示例

请求示例

```xml
<xml>
<ToUserName>gh_ea48699fb159</ToUserName>
<FromUserName>oHt_80DRclK4qjKfdYnPg6RxxsNI</FromUserName>
<MsgType>event</MsgType>
<Event>waybill_notify_query</Event>
<CreateTime>1600152165</CreateTime>
<WaybillId>557007127498128</WaybillId>
<SenderPhone>13763357711</SenderPhone>
<ReceiverPhone>13763357711</ReceiverPhone>
</xml>
```

返回示例

```xml
<xml>
<ToUserName>gh_ea48699fb159</ToUserName>
<FromUserName>oHt_80DRclK4qjKfdYnPg6RxxsNI</FromUserName>
<MsgType>event</MsgType>
<Event>waybill_notify_query</Event>
<CreateTime>1600152165</CreateTime>
<ResultCode>0</ResultCode>
<ResultMsg>OK</ResultMsg>
<WaybillCreateTime>1600000000</WaybillCreateTime>
<Path>
<ActionType>300001</ActionType>
<ActionTime>1600000000</ActionTime>
<ActionMsg>派送中</ActionMsg>
<DeliveryCourierName>张三</DeliveryCourierName>
<DeliveryCourierPhone>10086</DeliveryCourierPhone>
</Path>
<Path>
<ActionType>100001</ActionType>
<ActionTime>1600000000</ActionTime>
<ActionMsg>已取件</ActionMsg>
</Path>
</xml>
```
