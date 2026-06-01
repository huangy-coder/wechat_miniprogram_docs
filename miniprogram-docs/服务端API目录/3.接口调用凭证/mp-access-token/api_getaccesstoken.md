# 获取接口调用凭据

> 官方文档：[获取接口调用凭据](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-access-token/api_getaccesstoken.html)
> 所属分类：[接口调用凭证](../接口调用凭证目录.md)
> 导航路径：接口调用凭证 / 获取接口调用凭据
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getAccessToken

本接口用于获取获取全局唯一后台接口调用凭据（Access Token），token 有效期为 7200 秒，开发者需要进行妥善保存，使用注意事项请参考[此文档](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AccessToken)。

推荐使用 [获取稳定版接口调用凭据](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-access-token/api_getstableaccesstoken)

- 如使用[云开发](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/basis/getting-started.html)，可通过[云调用](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/guide/openapi/openapi.html)免维护 access_token 调用。
- 如使用[云托管](https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/basic/intro.html)，也可以通过[微信令牌/开放接口服务](https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/guide/weixin/open.html)免维护 access_token 调用。

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/cgi-bin/token?appid=AppID&secret=AppSecret&grant_type=client_credential
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

无

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1. 不同的应用类型的 `Access Token` 是互相隔离的，且仅支持调用应用类型的接口
2. `AppSecret` 是账号使用后台 `API` 接口的密钥，请开发者妥善保管，避免因泄露造成账号被其他人冒用等风险。
3. 如长期无 `AppSecret` 的使用需求，开发者可以使用对 `AppSeceret` 进行冻结，提高账号的安全性。
4. `AppSecret` 冻结后，开发者无法使用 `AppSecret` 获取 `Access token`（接口返回错误码 40243），不影响账号基本功能的正常使用，不影响通过第三方授权调用后台接口，不影响云开发调用后台接口。
5. 开发者可以随时对 `AppSecret` 进行解冻。

关于如何获取 Appid 和 AppSecret 信息，以及如何冻结/解冻AppSecret，请参考 [此文档](https://developers.weixin.qq.com/doc/oplatform/developers/dev/appid)

## 5. 代码示例

请求示例

```bash
GET https://api.weixin.qq.com/cgi-bin/token?appid=AppID&secret=AppSecret&grant_type=client_credential
```

返回示例

```json
{
  "access_token": "ACCESS_TOKEN",
  "expires_in": 7200
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

| 小程序 | 公众号 | 服务号 | 小游戏 | 微信小店 | 联盟带货机构 | 带货助手 | 小店供货商 | 移动应用 | 网站应用 | 视频号助手 | 多端应用 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

- ✔：该账号可调用此接口。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
