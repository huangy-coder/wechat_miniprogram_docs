# 获取微信API服务器IP

> 官方文档：[获取微信API服务器IP](https://developers.weixin.qq.com/miniprogram/dev/server/API/openApi-mgnt/api_getapidomainip.html)
> 所属分类：[openApi管理](../openApi管理目录.md)
> 导航路径：openApi管理 / 获取微信API服务器IP
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getApiDomainIp

该接口用于获取微信 api 服务器 ip 地址（开发者服务器主动访问 api.weixin.qq.com 的远端地址）

如果开发者基于安全等考虑，需要获知微信服务器的IP地址列表，以便进行相关限制，可以通过该接口获得微信服务器IP地址列表或者IP网段信息。

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/cgi-bin/get_api_domain_ip?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台使用 [component_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/ComponentAccessToken) 自己调用，同时还支持代商家调用。
- 服务商获得任意权限集授权后，即可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

无

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1. 由于出口 IP 及入口 IP 可能存在变动，建议用户每天请求接口1次，以便于及时更新IP列表。为了避免造成单点故障，强烈建议用户不要长期使用旧的 IP 列表作为 `api.weixin.qq.com` 的访问入口。
2. 使用固定IP访问 `api.weixin.qq.com` 时，请开发者注意运营商适配，跨运营商访问可能会存在高峰期丢包问题。
3. 由于出口 IP 及入口 IP 可能存在变动，建议用户每天请求接口 1 次，以便于及时更新 IP 列表。为了避免造成单点故障，强烈建议用户不要长期使用旧的IP列表作为 `api.weixin.qq.com` 的访问入口。

## 5. 代码示例

### 5.1 成功响应

请求示例

```json
{}
```

返回示例

```json
{
  "ip_list": [
    "101.89.47.18",
    "101.91.34.103"
  ]
}
```

### 5.2 错误响应

请求示例

```json
{}
```

返回示例

```json
{
  "errcode": 40013,
  "errmsg": "invalid appid"
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
