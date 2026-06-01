# 运单轨迹更新事件

> 官方文档：[运单轨迹更新事件](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/logistics.onPathUpdate.html)
> 所属分类：[事件通知](../../事件通知目录.md)
> 导航路径：事件通知 / 物流助手 / 运力方使用 / 运单轨迹更新事件
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 本文档描述服务器端接收的消息或事件，详细说明参见[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)。

事件英文名：logistics.onPathUpdate

运单轨迹更新事件。当运单轨迹有更新时，会触发此事件并产生数据包。

## 1. 消息参数

### 请求体 Request Payload

### Body.Actions(Array) Object Payload

轨迹列表

## 2. 消息返回

### 返回体 Response Payload

回复 `success` 或空字符串（无需加密）

## 3. 枚举信息

### Body.Actions(Array).ActionType Enum

轨迹节点类型

## 4. 注意事项

本事件无特殊注意事项

## 5. 代码示例

### 5.1 XML 示例

请求示例

```xml
<xml>
  <ToUserName><![CDATA[toUser]]></ToUserName>
  <FromUserName><![CDATA[fromUser]]></FromUserName>
  <CreateTime>1546924844</CreateTime>
  <MsgType><![CDATA[event]]></MsgType>
  <Event><![CDATA[add_express_path]]></Event>
  <DeliveryID><![CDATA[SF]]></DeliveryID>
  <WayBillId><![CDATA[123456789]]></WayBillId>
  <OrderId><![CDATA[123456]]></OrderId>
  <Version>3</Version>
  <Count>3</Count>
  <Actions>
    <ActionTime>1546924840</ActionTime>
    <ActionType>100001</ActionType>
    <ActionMsg><![CDATA[小哥A揽件成功]]></ActionMsg>
  </Actions>
  <Actions>
    <ActionTime>1546924841</ActionTime>
    <ActionType>200001</ActionType>
    <ActionMsg><![CDATA[到达广州集包地]]></ActionMsg>
  </Actions>
  <Actions>
    <ActionTime>1546924842</ActionTime>
    <ActionType>200001</ActionType>
    <ActionMsg><![CDATA[运往目的地]]></ActionMsg>
  </Actions>
</xml>
```

返回示例

```text
success
```

### 5.2 JSON 示例

请求示例

```json
{
  "ToUserName": "toUser",
  "FromUserName": "fromUser",
  "CreateTime": 1546924844,
  "MsgType": "event",
  "Event": "add_express_path",
  "DeliveryID": "SF",
  "WayBillId": "123456789",
  "OrderId": "123456789",
  "Version": 2,
  "Count": 3,
  "Actions": [
    {
      "ActionTime": 1546924840,
      "ActionType": 100001,
      "ActionMsg": "小哥A揽件成功"
    },
    {
      "ActionTime": 1546924841,
      "ActionType": 200001,
      "ActionMsg": "到达广州集包地"
    },
    {
      "ActionTime": 1546924842,
      "ActionType": 200001,
      "ActionMsg": "运往目的地"
    }
  ]
}
```

返回示例

```text
success
```
