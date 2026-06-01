# 查询API调用额度

> 官方文档：[查询API调用额度](https://developers.weixin.qq.com/miniprogram/dev/server/API/openApi-mgnt/api_getapiquota.html)
> 所属分类：[openApi管理](../openApi管理目录.md)
> 导航路径：openApi管理 / 查询API调用额度
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getApiQuota

本接口用于查询服务端接口的的每日调用接口的额度，调用次数，频率限制。

适用账号类型：公众号/服务号/小程序/小游戏/微信小店/带货助手/视频号助手/联盟带货机构/移动应用/网站应用/多端应用/第三方平台等接口

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/openapi/quota/get?access_token=ACCESS_TOKEN
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台使用 [component_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/ComponentAccessToken) 自己调用，同时还支持代商家调用。
- 服务商获得任意权限集授权后，即可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.quota Object Payload

quota详情

### Res.rate_limit Object Payload

普通调用频率限制

### Res.component_rate_limit Object Payload

代调用频率限制

## 4. 注意事项

1、如果查询的api属于公众号的接口，则需要用公众号的 access_token；如果查询的api属于小程序的接口，则需要用[小程序的access_token](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-access-token/api_getaccesstoken)；如果查询的接口属于第三方平台的接口，则需要用[第三方平台的component_access_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getcomponentaccesstoken)；如此类推。

2、如果查询的接口属于第三方平台接口但用于公众号/小程序，则需要用第三方平台的[authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken)

2、如果是第三方服务商代公众号/服务号/小程序/微信小店/带货助手/视频号助手查询的接口，则需要用[authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken)

3、每个接口都有调用次数限制，请开发者合理调用接口。

4、”/xxx/sns/xxx“这类接口不支持使用该接口，会出现76022报错。

5、如果接口文档中有单独的说明接口的特殊的 quota 数量以及逻辑，则以每个接口的接口文档的描述为准。

## 5. 代码示例

请求示例

```json
{
  "cgi_path": "/wxa/gettemplatedraftlist"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "quota": {
    "daily_limit": 0,
    "used": 0,
    "remain": 0
  }
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

| 小程序 | 公众号 | 服务号 | 小游戏 | 微信小店 | 联盟带货机构 | 带货助手 | 小店供货商 | 第三方平台 | 移动应用 | 网站应用 | 视频号助手 | 多端应用 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | 〇 | ✔ | ✔ | ✔ | ✔ |

- ✔：该账号可调用此接口。
- 〇：第三方平台可使用 [component_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/ComponentAccessToken) 调用，是否支持代商家调用需看本文档 [调用方式](#apicalltype) 部分。
