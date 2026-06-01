# 评价管理差评通知事件

> 官方文档：[评价管理差评通知事件](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/guarantee/negative.html)
> 所属分类：[事件通知](../事件通知目录.md)
> 导航路径：事件通知 / 小程序评价
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 本文档描述服务器端接收的消息或事件，详细说明参见[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)。

事件英文名：wxa_comment_bad_score

使用[微信小程序客服消息能力](https://developers.weixin.qq.com/miniprogram/introduction/custom#二、下发条件说明)的开发者，针对用户差评，平台提供了「差评客服会话」能力，开发者可使用该能力主动下发一条客服消息给差评用户；当用户回复后，开发者可继续用小程序客服消息能力与用户沟通。

使用流程：

1. 用户发起差评
2. 微信服务器会推送此事件，通知开发者
3. 开发者可以选择调用重置客服quota的api，详情可看[重置Api客服quota](https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/comment/api_resetapikfquota)
4. 重置客服quota后，可以直接使用[微信小程序客服的api能力](https://developers.weixin.qq.com/miniprogram/introduction/custom#二、下发条件说明)去下发客服消息

## 1. 消息参数

### 请求体 Request Payload

### Body.result Object Payload

结果对象

## 2. 消息返回

### 返回体 Response Payload

回复 `success` 或空字符串（无需加密）

## 3. 注意事项

本事件无特殊注意事项

## 4. 代码示例

### 4.1 JSON 示例

请求示例

```json
{
    "ToUserName": "gh_abcdefg",
    "FromUserName": "oABCD",
    "CreateTime": 1704038400,
    "MsgType": "event",
    "Event": "wxa_comment_bad_score",
    "result": {
        "comment_id": "2272502024443330610"
    }
}
```

返回示例

```json
SUCCESS
```

### 4.2 XML 示例

请求示例

```xml
<xml>
    <ToUserName><![CDATA[gh_abcdefg]]></ToUserName> 
    <FromUserName><![CDATA[oABCD]]></FromUserName> 
    <CreateTime>1704038400</CreateTime>
    <MsgType><![CDATA[event]]></MsgType> 
    <Event><![CDATA[wxa_comment_bad_score]]></Event>
    <result>
        <comment_id>2272502024443330610</comment_id>
    </result>
</xml>
```

返回示例

```json
SUCCESS
```
