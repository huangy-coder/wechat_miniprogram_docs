# 获取稳定版接口调用凭据

> 官方文档：[获取稳定版接口调用凭据](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-access-token/api_getstableaccesstoken.html)
> 所属分类：[接口调用凭证](../接口调用凭证目录.md)
> 导航路径：接口调用凭证 / 获取稳定版接口调用凭据
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getStableAccessToken

本接口用于获取获取全局唯一后台接口调用凭据（Access Token），token 有效期为 7200 秒，但此接口和 [getAccessToken](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-access-token/api_getaccesstoken) 互相隔离，且比其更加稳定，推荐使用此接口替代。开发者需要进行妥善保存，使用注意事项请参考[此文档](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AccessToken.html)。

有两种调用模式:

1. 普通模式，`access_token` 有效期内重复调用该接口不会更新 `access_token`，绝大部分场景下使用该模式；
2. 强制刷新模式，会导致上次获取的 `access_token` 失效，并返回新的 `access_token`；

- 如使用[云开发](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/basis/getting-started.html)，可通过[云调用](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/guide/openapi/openapi.html)免维护 `access_token` 调用；
- 如使用[云托管](https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/basic/intro.html)，也可以通过[微信令牌/开放接口服务](https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/guide/weixin/open.html)免维护 `access_token` 调用；

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/stable_token
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

无

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1. 与 [getAccessToken](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-access-token/api_getaccesstoken) 获取的调用凭证完全隔离，互不影响。
2. 该接口仅支持 `POST` 形式的调用。
3. 该接口调用频率限制为 1 万次 每分钟，每天限制调用 50 万次。
4. `access_token` 存储空间至少保留 512 字符。
5. 强制刷新模式每天限用 20 次且需间隔 30 秒。
6. 普通模式下平台会提前 5 分钟更新 `access_token`。

## 5. 代码示例

### 5.1 不强制刷新获取Token（不传递force_refresh，默认值为false）

请求示例

```text
POST https://api.weixin.qq.com/cgi-bin/stable_token
```

```json
{
    "grant_type": "client_credential",
    "appid": "APPID",
    "secret": "APPSECRET"
}
```

返回示例

```json
{
    "access_token":"ACCESS_TOKEN",
    "expires_in":7200
}
```

### 5.2 不强制刷新获取Token（设置force_refresh为false）:

请求示例

```json
{
    "grant_type": "client_credential",
    "appid": "APPID",
    "secret": "APPSECRET",
    "force_refresh": false
} 
```

返回示例

```json
{
    "access_token":"ACCESS_TOKEN",
    "expires_in":345 // 如果仍然有效，会返回上次的 token，并给出所剩有效时间
} 
```

### 5.3 强制刷新模式，慎用，连续使用需要至少间隔30s

请求示例

```text
POST https://api.weixin.qq.com/cgi-bin/stable_token
```

```json
{
    "grant_type": "client_credential",
    "appid": "APPID",
    "secret": "APPSECRET",
    "force_refresh": true
} 
```

返回示例

```json
{
    "access_token":"ACCESS_TOKEN",
    "expires_in":7200
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
