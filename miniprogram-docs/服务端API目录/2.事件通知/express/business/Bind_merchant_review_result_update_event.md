# logistics.onBindResultUpdate

> 官方文档：[logistics.onBindResultUpdate](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/business/Bind_merchant_review_result_update_event.html)
> 所属分类：[事件通知](../../事件通知目录.md)
> 导航路径：事件通知 / 物流助手 / 小程序方使用
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 本文档描述服务器端接收的消息或事件，详细说明参见[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)。

绑定商户审核结果更新事件。收到事件之后，回复`success`或者空串即可。

### 消息参数

### OnBindResultUpdateData

### 消息数据包示例

XML 格式

```xml
<xml>
  <ToUserName><![CDATA[toUser]]></ToUserName>
  <FromUserName><![CDATA[fromUser]]></FromUserName>
  <CreateTime>1546924844</CreateTime>
  <MsgType><![CDATA[event]]></MsgType>
  <Event><![CDATA[update_business_bind_result]]></Event>
  <errcode>0</errcode>
  <errmsg><![CDATA[ok]]></errmsg>
  <delivery_id><![CDATA[EMS]]></delivery_id>
  <biz_id><![CDATA[1234567]]></biz_id>
</xml>
```

JSON 格式

```json
{
  "ToUserName": "toUser",
  "FromUserName": "fromUser",
  "CreateTime": 1546924844,
  "MsgType": "event",
  "Event": "update_business_bind_result",
  "errcode": 0,
  "errmsg": "ok",
  "delivery_id": "EMS",
  "biz_id": "1234567",
}
```

```text

```
