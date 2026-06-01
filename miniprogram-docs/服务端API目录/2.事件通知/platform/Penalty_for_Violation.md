# 小程序违规处罚信息通知

> 官方文档：[小程序违规处罚信息通知](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/platform/Penalty_for_Violation.html)
> 所属分类：[事件通知](../事件通知目录.md)
> 导航路径：事件通知 / 平台通知 / 小程序违规处罚信息通知
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 本文档描述服务器端接收的消息或事件，详细说明参见[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)。

事件英文名：Penalty_for_Violation

当小程序存在违规行为时，平台会通过消息推送服务器通知给小程序开发者，建议小程序开发者注意及时接收相关通知进行排查整改，此通知不影响已有站内信等通知方式。

## 1. 消息参数

### 请求体 Request Payload

## 2. 消息返回

### 返回体 Response Payload

回复 `success` 或空字符串（无需加密）

## 3. 枚举信息

### Body.Event Enum

事件名称

## 4. 注意事项

#### 违规处罚事件详情（detail详细释义）

- 当**event_type=1**时**detail**中的JSON字符串结构如下| 属性 类型 说明 warned_type number 警告类型。1 rectify_deadline number 警告的截止时间(UNIX时间戳) warned_function_names array<string> 警告要封禁的功能项列表，如需获取列表中每个功能项的封禁时长，可直接在warned_ban_days的对应索引处获得，warned_function_names和warned_ban_days总是一一对应。（该字段仅当warned_type=2时生效） warned_ban_days array<number> 警告封禁的天数列表。当warned_type=1时则该列表仅有一项，代表警告要封禁小程序账号的天数。当warned_type=2时列表中的每一项分别代表warned_function_names中对应索引处的功能项被警告要封禁的天数。当warned_type=3时则该列表仅有一项，代表警告要下架小程序的天数。注
- 当**event_type=2**时**detail**中的JSON字符串结构如下| 属性 类型 说明 banned_days array<number> 功能项被封禁的天数列表，列表中的每一项分别代表banned_function_names中对应索引处的功能项被封禁的天数。注 banned_function_names array<string> 被封禁的功能项列表，如需获取列表中每个功能项的封禁时长，可直接在banned_days的对应索引处获得，banned_days和banned_function_names总是一一对应。
- 当**event_type=3**时**detail**中的JSON字符串结构如下| 属性 类型 说明 suspended_days number 下架天数。注
- 当**event_type=4**时**detail**中的JSON字符串结构如下| 属性 类型 说明 banned_days number 账号封禁天数。注
- 当**event_type=5**时**detail**中的JSON字符串结构如下| 属性 类型 说明 path string 封禁的页面路径

## 5. 代码示例

### 5.1 当 event_type=1 并且 warned_type=1

请求示例

```json
{
    "ToUserName": "gh_1d6c1222test",
    "FromUserName": "oyeHc4i5LqBbWLVTfnhf-3TZ4BNk",
    "CreateTime": 1699803867,
    "MsgType": "event",
    "Event": "wxa_punish_event",
    "punish_id": "649557",
    "appid": "wx54a8eaa26606test",
    "punish_time": 1699803865,
    "illegal_reason": "存在诱导分享行为",
    "illegal_content": [
        "违规内容测试"
    ],
    "detail": "{\"warned_type\":1,\"rectify_deadline\":1699796571,\"warned_function_names\":[],\"warned_ban_days\":[3]}",
    "rule_url": "https://developers.weixin.qq.com/miniprogram/product/index.html#_5-1-滥用分享行为",
    "rule_name": "《微信小程序平台运营规范》5.行为规范-5.1滥用分享行为",
    "adjust_guide_url": "https://mp.weixin.qq.com/s/73rLZmwPeQ87Q89DYQcfkw",
    "event_type": 1
}
```

返回示例

```bash
success
```

### 5.2 当 event_type=1 并且 warned_type=2

请求示例

```json
{
    "ToUserName": "gh_1d6c1222test",
    "FromUserName": "oyeHc4pIdqHZwh80SufyUuIzSenw",
    "CreateTime": 1699795665,
    "MsgType": "event",
    "Event": "wxa_punish_event",
    "punish_id": "649551",
    "appid": "wx54a8eaa26606test",
    "punish_time": 1699795663,
    "illegal_reason": "存在诱导分享行为",
    "illegal_content": [
        "违规内容测试"
    ],
    "detail": "{\"warned_type\":2,\"rectify_deadline\":1699796571,\"warned_function_names\":[\"分享朋友圈\",\"客服消息接口\"],\"warned_ban_days\":[1,1]}",
    "rule_url": "https://developers.weixin.qq.com/miniprogram/product/index.html#_5-1-滥用分享行为",
    "rule_name": "《微信小程序平台运营规范》5.行为规范-5.1滥用分享行为",
    "adjust_guide_url": "https://mp.weixin.qq.com/s/73rLZmwPeQ87Q89DYQcfkw",
    "event_type": 1
}
```

返回示例

```bash
success
```

### 5.3 当 event_type=1 并且 warned_type=3

请求示例

```json
{
    "ToUserName": "gh_1d6c1222test",
    "FromUserName": "oyeHc4tGxCvPcXlKeFI5tU0jV_yw",
    "CreateTime": 1699795665,
    "MsgType": "event",
    "Event": "wxa_punish_event",
    "punish_id": "649551",
    "appid": "wx54a8eaa26606test",
    "punish_time": 1699795663,
    "illegal_reason": "存在诱导分享行为",
    "illegal_content": [
        "违规内容测试"
    ],
    "detail": "{\"warned_type\":3,\"rectify_deadline\":1699796571,\"warned_function_names\":[],\"warned_ban_days\":[1]}",
    "rule_url": "https://developers.weixin.qq.com/miniprogram/product/index.html#_5-1-滥用分享行为",
    "rule_name": "《微信小程序平台运营规范》5.行为规范-5.1滥用分享行为",
    "adjust_guide_url": "https://mp.weixin.qq.com/s/73rLZmwPeQ87Q89DYQcfkw",
    "event_type": 1
}
```

返回示例

```bash
success
```

### 5.4 当 event_type=2

请求示例

```json
 {
     "ToUserName": "gh_1d6c1222test",
     "FromUserName": "oyeHc4gSrT2S8jG2Ll1ZS16rwqQk",
     "CreateTime": 1699791600,
     "MsgType": "event",
     "Event": "wxa_punish_event",
     "punish_id": "13577492",
     "appid": "wx54a8eaa26606test",
     "punish_time": 1699791599,
     "illegal_reason": "存在诱导分享行为",
     "illegal_content": [
         "违规内容测试"
     ],
     "detail": "{\"banned_days\":[1,1],\"banned_function_names\":[\"分享朋友圈\",\"客服消息接口\"]}",
     "rule_url": "https://developers.weixin.qq.com/miniprogram/product/index.html#_5-1-滥用分享行为",
     "rule_name": "《微信小程序平台运营规范》5.行为规范-5.1滥用分享行为",
     "adjust_guide_url": "https://mp.weixin.qq.com/s/73rLZmwPeQ87Q89DYQcfkw",
     "event_type": 2
 }
```

返回示例

```bash
success
```

### 5.5 当 event_type=3

请求示例

```json
{
    "ToUserName": "gh_1d6c1222test",
    "FromUserName": "oyeHc4qHkaYV-0NYupPZBTBrBNuw",
    "CreateTime": 1699801563,
    "MsgType": "event",
    "Event": "wxa_punish_event",
    "punish_id": "13577869",
    "appid": "wx54a8eaa26606test",
    "punish_time": 1699801560,
    "illegal_reason": "存在诱导分享行为",
    "illegal_content": [
        "违规内容测试"
    ],
    "detail": "{\"suspended_days\":1}",
    "rule_url": "https://developers.weixin.qq.com/miniprogram/product/index.html#_5-1-滥用分享行为",
    "rule_name": "《微信小程序平台运营规范》5.行为规范-5.1滥用分享行为",
    "adjust_guide_url": "https://mp.weixin.qq.com/s/73rLZmwPeQ87Q89DYQcfkw",
    "event_type": 3
}
```

返回示例

```bash
success
```

### 5.6 当 event_type=4

请求示例

```json
{
    "ToUserName": "gh_1d6c1222test",
    "FromUserName": "oyeHc4jjAdCWq1klrk-puPMe0FC4",
    "CreateTime": 1699784111,
    "MsgType": "event",
    "Event": "wxa_punish_event",
    "punish_id": "9328325",
    "appid": "wx54a8eaa26606test",
    "punish_time": 1699784109,
    "illegal_reason": "存在诱导分享行为",
    "illegal_content": [
        "测试违规内容/证据"
    ],
    "detail": "{\"banned_days\":3}",
    "rule_url": "https://developers.weixin.qq.com/miniprogram/product/index.html#_5-1-滥用分享行为",
    "rule_name": "《微信小程序平台运营规范》5.行为规范-5.1滥用分享行为",
    "adjust_guide_url": "https://mp.weixin.qq.com/s/73rLZmwPeQ87Q89DYQcfkw",
    "event_type": 4
}
```

返回示例

```bash
success
```

### 5.7 当 event_type=10

请求示例

```json
{
   "ToUserName": "gh_1d6c1222test",
   "FromUserName": "oyeHc4n0I6U3A4Fq7tfOAqmAJy8E",
   "CreateTime": 1699802583,
   "MsgType": "event",
   "Event": "wxa_punish_event",
   "punish_id": "94185814",
   "appid": "wx54a8eaa266009d6a",
   "punish_time": 1699802425,
   "illegal_reason": "发布低俗、性暗示或色情信息",
   "illegal_content": [
       "测试证据"
   ],
   "detail": "{\"path\":\"pages/fengjin/fengjin\"}",
   "rule_url": "https://developers.weixin.qq.com/miniprogram/product/index.html#_6-2-色情低俗内容",
   "rule_name": "《微信小程序平台运营规范》6.信息内容规范-6.2色情低俗内容",
   "adjust_guide_url": "https://mp.weixin.qq.com/s/73rLZmwPeQ87Q89DYQcfkw",
   "event_type": 10
}
```

返回示例

```bash
success
```
