# 查询scheme码

> 官方文档：[查询scheme码](https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/url-scheme/api_queryscheme.html)
> 所属分类：[小程序码与小程序链接](../../小程序码与小程序链接目录.md)
> 导航路径：小程序码与小程序链接 / URL Scheme / 查询scheme码
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：queryScheme

该接口用于查询小程序 scheme 码，包括加密 scheme 和明文 scheme

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/queryscheme?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：urlscheme.query
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：88
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.scheme_info Object Payload

scheme 信息

### Res.quota_info Object Payload

quota 配置

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

### 5.1 查询加密 scheme

请求示例

```json
{
  "scheme": "weixin://dl/business/?t=XTSkBZlzqmn&cq=a=hello",
  "query_type": 0
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "scheme_info": {
    "appid": "appid",
    "path": "",
    "query": "a=hello",
    "create_time": 611928113,
    "expire_time": 0,
    "env_version": "release"
  }
}
```

### 5.2 查询明文 scheme

请求示例

```json
{
  "scheme": "weixin://dl/business/?appid=xxx&path=xxx&query=a=1&b=2&env_version=release",
  "query_type": 0
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "scheme_info": {
    "appid": "appid",
    "path": "xxx",
    "query": "a=1&b=2",
    "env_version": "release"
  }
}
```

### 5.3 查询剩余访问次数

请求示例

```json
{
  "query_type": 1
}
```

返回示例

{
"errcode": 0,
"errmsg": "ok",
"quota_info": {
"remain_visit_quota": 1000000
}
}
}

### 5.4 云函数调用示例

请求示例

```json
const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
})
exports.main = async (event, context) => {
  try {
    const result = await cloud.openapi.urlscheme.query({
        "scheme": 'weixin://dl/business/?t=XTSkBZlzqmn'
      })
    return result
  } catch (err) {
    return err
  }
}
```

返回示例

```json
{
  "errCode": 0,
  "errMsg": "ok",
  "schemeInfo": {
    "appid": "appid",
    "path": "",
    "query": "",
    "createTime": 611928113,
    "expireTime": 0,
    "envVersion": "release"
  }
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
