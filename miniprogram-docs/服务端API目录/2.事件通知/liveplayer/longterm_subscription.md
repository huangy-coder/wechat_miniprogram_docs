# 长期订阅群发结果通知

> 官方文档：[长期订阅群发结果通知](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/liveplayer/longterm_subscription.html)
> 所属分类：[事件通知](../事件通知目录.md)
> 导航路径：事件通知 / 小程序直播 / 长期订阅群发结果通知
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 本文档描述服务器端接收的消息或事件，详细说明参见[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)。

事件英文名：wxalive_push_message_notify

异步返回长期订阅群发最终结果

## 1. 消息参数

### 请求体 Request Payload

## 2. 消息返回

### 返回体 Response Payload

回复 `success` 或空字符串（无需加密）

## 3. 注意事项

本事件无特殊注意事项

## 4. 代码示例

请求示例

```xml
<xml>
   <ToUserName><![CDATA[xxx]]></ToUserName>
   <FromUserName><![CDATA[xxx]]></FromUserName>
   <CreateTime>1606273828</CreateTime>
   <MsgType><![CDATA[event]]></MsgType>
   <Event><![CDATA[wxalive_push_message_notify]]></Event>
   <PushMessageApiNotify>
      <message_id><![CDATA[1622047360795164672]]></message_id>
      <room_id>xxx</room_id>
      <total_count>xxx</total_count>
      <success_count>xxx</success_count>
      <openid_error_count>xxx</openid_error_count>
      <relation_error_count>xxx</relation_error_count>
      <user_recv_limit_count>xxx</user_recv_limit_count>
      <internal_error_count>xxx</internal_error_count>
   </PushMessageApiNotify>
</xml>
```

返回示例

```json
SUCCESS
```
