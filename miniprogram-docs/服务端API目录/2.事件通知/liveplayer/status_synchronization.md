# 长期订阅状态通知

> 官方文档：[长期订阅状态通知](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/liveplayer/status_synchronization.html)
> 所属分类：[事件通知](../事件通知目录.md)
> 导航路径：事件通知 / 小程序直播
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 本文档描述服务器端接收的消息或事件，详细说明参见[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)。

事件英文名：wxalive_follow_notify

用户订阅小程序直播后会触发事件通知

## 1. 消息参数

### 请求体 Request Payload

## 2. 消息返回

### 返回体 Response Payload

回复 `success` 或空字符串（无需加密）

## 3. 枚举信息

### Body.live_status Enum

阅或者取消订阅时直播间状态，取值：

### Body.action Enum

订阅行为

## 4. 注意事项

本事件无特殊注意事项

## 5. 代码示例

请求示例

```xml
<xml>
  <ToUserName><![CDATA[toUser]]></ToUserName>
  <FromUserName><![CDATA[fromUser]]></FromUserName>
  <CreateTime>1546924844</CreateTime>
  <MsgType><![CDATA[event]]></MsgType>
  <Event><![CDATA[wxalive_follow_notify]]></Event>
  <FollowNotify>
    <room_id>1</room_id>
    <user_openid>![CDATA[xxx]]</user_openid>
    <time>1546924844</time>
    <live_status>101</live_status>
    <action>![CDATA[add_follow]]</action>
  </FollowNotify>
 </xml>
```

返回示例

```json
SUCCESS
```
