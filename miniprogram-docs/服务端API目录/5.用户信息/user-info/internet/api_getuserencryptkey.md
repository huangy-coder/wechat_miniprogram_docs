# 获取用户encryptKey

> 官方文档：[获取用户encryptKey](https://developers.weixin.qq.com/miniprogram/dev/server/API/user-info/internet/api_getuserencryptkey.html)
> 所属分类：[用户信息](../../用户信息目录.md)
> 导航路径：用户信息 / 网络 / 获取用户encryptKey
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getUserEncryptKey

该接口用于获取用户encryptKey。 会获取用户最近3次的key，每个key的存活时间为3600s

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/wxa/business/getuserencryptkey?access_token=ACCESS_TOKEN&openid=OPENID&signature=SIGNATURE&sig_method=SIG_METHOD
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

无

## 3. 返回参数

### 返回体 Response Payload

### Res.key_info_list(Array) Object Payload

用户最近三次的加密key列表

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```text
GET https://api.weixin.qq.com/wxa/business/getuserencryptkey?access_token=OsAoOMw4niuuVbfSxxxxxxxxxxxxxxxxxxx&signature=fefce01bfba4670c85b228e6ca2b493c90971e7c442f54fc448662eb7cd72509&openid=oGZUI0egBJY1zhBYw2KhdUfwVJJE&sig_method=hmac_sha256
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "key_info_list": [
    {
      "encrypt_key": "VI6BpyrK9XH4i4AIGe86tg==",
      "version": 10,
      "expire_in": 3597,
      "iv": "6003f73ec441c386",
      "create_time": 1616572301
    },
    {
      "encrypt_key": "aoUGAHltcliiL9f23oTKHA==",
      "version": 9,
      "expire_in": 0,
      "iv": "7996656384218dbb",
      "create_time": 1616504886
    },
    {
      "encrypt_key": "MlZNQNnRQz3zXHHcr6A3mA==",
      "version": 8,
      "expire_in": 0,
      "iv": "58a1814f88883024",
      "create_time": 1616488061
    }
  ]
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
