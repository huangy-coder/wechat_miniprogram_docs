# 重置登录态

> 官方文档：[重置登录态](https://developers.weixin.qq.com/miniprogram/dev/server/API/user-login/api_resetusersessionkey.html)
> 所属分类：[小程序登录](../小程序登录目录.md)
> 导航路径：小程序登录 / 重置登录态
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：ResetUserSessionKey

重置指定的登录态 session_key。为了保持 session_key 私密性，接口不明文传入 session_key，而是通过校验登录态签名完成。

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/wxa/resetusersessionkey?access_token=ACCESS_TOKEN
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

## 4. 注意事项

1. 重置用户session_key后，原有的session_key会失效。请注意接口调用时机，以免影响用户在小程序中的体验。
2. 重置后的session_key会继承原有的session_key的过期时间，重置操作不能为session_key续期。
3. 单个小程序appid请求量频率限制为 60000 次 / 分钟。
4. 不允许频繁重置同一个用户的登录态。

## 5. 代码示例

请求示例

```text
GET https://api.weixin.qq.com/wxa/resetusersessionkey?access_token=ACCESS_TOKEN&openid=OPENID&signature=SIGNATURE&sig_method=hmac_sha256
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "openid": "xxxxxxx",
  "session_key": "xxxxxxxx"
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
