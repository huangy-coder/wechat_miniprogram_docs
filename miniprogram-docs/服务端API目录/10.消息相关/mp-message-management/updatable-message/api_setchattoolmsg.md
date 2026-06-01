# 修改小程序聊天工具的动态卡片消息

> 官方文档：[修改小程序聊天工具的动态卡片消息](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/updatable-message/api_setchattoolmsg.html)
> 所属分类：[消息相关](../../消息相关目录.md)
> 导航路径：消息相关 / 动态消息 / 修改小程序聊天工具的动态卡片消息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：setChatToolMsg

该接口用于修改被分享的小程序聊天工具的动态卡片消息。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/message/wxopen/chattoolmsg/send?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：chattoolmsg.send
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.participator_info_list(Array) Object Payload

更新后的聊天室成员状态

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
"activity_id": "966_NGiqxxxxxxxxxx...xxxxxxxxE33BlwX", 
"target_state": 1, 
"template_id": "4A68CBB88A92B0A9311848DBA1E94A199B166463",
"version_type": 0,
"participator_info_list": [
{"group_openid": "aaaaaaaaaa", 
"state": 1}, 
{"group_openid": "bbbbbbbbb", 
"state": 1}, 
] 
}
```

返回示例

```json
{
"errcode": 0, 
"errmsg": "ok", 
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

- ✔：该账号可调用此接口。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
