# 查询商户余额

> 官方文档：[查询商户余额](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/Query_merchant_balance_events.html)
> 所属分类：[事件通知](../../事件通知目录.md)
> 导航路径：事件通知 / 物流助手 / 运力方使用 / 查询商户余额事件
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 本文档描述服务器端接收的消息或事件，详细说明参见[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)。

事件英文名：logistics.onGetQuota

查询商户余额事件

## 1. 消息参数

### 请求体 Request Payload

## 2. 消息返回

### 返回体 Response Payload

## 3. 枚举信息

### Res.ResultCode Enum

处理结果错误码

## 4. 注意事项

本事件无特殊注意事项

## 5. 代码示例

### 5.1 XML 格式

请求示例

```xml
<xml>
    <ToUserName><![CDATA[gh_abcdefg]]></ToUserName>
    <FromUserName><![CDATA[oABCD]]></FromUserName>
    <CreateTime>1533042556</CreateTime>
    <MsgType><![CDATA[event]]></MsgType>
    <Event><![CDATA[get_quota]]></Event>
    <BizID><![CDATA[xyz]]></BizID>
    <BizPwd><![CDATA[xyz123]]></BizPwd>
    <ShopAppID><![CDATA[wxABCD]]></ShopAppID>
</xml>
```

返回示例

```xml
<xml>
    <ToUserName><![CDATA[oABCD]]></ToUserName>
    <FromUserName><![CDATA[gh_abcdefg]]></FromUserName>
    <CreateTime>1533042556</CreateTime>
    <MsgType><![CDATA[event]]></MsgType>
    <Event><![CDATA[get_quota]]></Event>
    <BizID><![CDATA[xyz]]></BizID>
    <ResultCode>0</ResultCode>
    <ResultMsg><![CDATA[success]]></ResultMsg>
    <Quota>0</Quota>
</xml>
```

### 5.2 JSON 格式

请求示例

```json
{
  "ToUserName": "gh_abcdefg",
  "FromUserName": "oABCD",
  "CreateTime": 1533042556,
  "MsgType": "event",
  "Event": "get_quota",
  "BizID": "xyz",
  "BizPwd": "xyz123",
  "ShopAppID": "wxABCD"
}
```

返回示例

```json
{
  "ToUserName": "oABCD",
  "FromUserName": "gh_abcdefg",
  "CreateTime": 1533042556,
  "MsgType": "event",
  "Event": "get_quota",
  "BizID": "xyz",
  "ResultCode": 0,
  "ResultMsg": "success",
  "Quota": 0
}
```
