# 查询服务卡片状态

> 官方文档：[查询服务卡片状态](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_getusernotify.html)
> 所属分类：[消息相关](../../消息相关目录.md)
> 导航路径：消息相关 / 订阅消息 / 查询服务卡片状态
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getUserNotify

查询服务卡片状态

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/get_user_notify?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.notify_info Object Payload

卡片状态

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

### 5.1 成功返回

请求示例

```json
{
  "openid": "xxx",
  "notify_type": 1001,
  "notify_code": "xxx"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "notify_info": {
    "notify_type": 1001,
    "content_json": "{\"cur_status\":2,\"license_plate\":\"粤A·12345A\",\"arrival_time\":1679569348,\"wxa_path_query\":\"\"}",
    "code_state": 1,
    "code_expire_time": 1681906267
  }
}
```

### 5.2 异常返回

请求示例

```json
{
  "openid": "xxx",
  "notify_type": 1001,
  "notify_code": "xxx"
}
```

返回示例

```json
{
  "errcode": 85437,
  "errmsg": "invalid notify_code"
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
