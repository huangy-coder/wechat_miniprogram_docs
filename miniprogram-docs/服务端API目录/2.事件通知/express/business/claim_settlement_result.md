# 理赔结果推送

> 官方文档：[理赔结果推送](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/business/claim_settlement_result.html)
> 所属分类：[事件通知](../../事件通知目录.md)
> 导航路径：事件通知 / 物流助手 / 小程序方使用 / 理赔结果推送
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 本文档描述服务器端接收的消息或事件，详细说明参见[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)。

事件英文名：wxainsurance_claim_result

如果无忧退理赔有结果，将推送此事件。

## 1. 消息参数

### 请求体 Request Payload

## 2. 消息返回

### 返回体 Response Payload

回复 `success` 或空字符串（无需加密）

## 3. 枚举信息

### Body.Status Enum

保单状态

## 4. 注意事项

本事件无特殊注意事项

## 5. 代码示例

请求示例

```xml
<xml>
    <ToUserName>gh_abcdefg</ToUserName>
    <FromUserName>oABCD</FromUserName>
    <CreateTime>1234455555</CreateTime>
    <MsgType>event</MsgType>
    <Event>wxainsurance_claim_result</Event>
    <upload_event>
        <OrderNo><![CDATA[42000021662024041000000000000]]></OrderNo>
        <Status>5</Status>
        <FinishTime>1234455555</FinishTime>
    </upload_event>
</xml>
```

返回示例

```json
SUCCESS
```
