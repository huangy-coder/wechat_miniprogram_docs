# 文本内容安全识别

> 官方文档：[文本内容安全识别](https://developers.weixin.qq.com/miniprogram/dev/server/API/sec-center/sec-check/api_msgseccheck.html)
> 所属分类：[小程序安全](../../小程序安全目录.md)
> 导航路径：小程序安全 / 内容安全 / 文本内容安全识别
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：msgSecCheck

该接口用于检查一段文本是否含有违法违规内容。

应用场景：

- 用户个人资料违规文字检测；
- 媒体新闻类用户发表文章，评论内容检测；
- 游戏类用户编辑上传的素材(如答题类小游戏用户上传的问题及答案)检测等。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/msg_sec_check?access_token=ACCESS_TOKEN
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 调用方法：security.msgSecCheck
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.detail(Array) Object Payload

详细检测结果

### Res.result Object Payload

综合结果

## 4. 注意事项

-1.0 版本接口文档[【点击查看】](https://developers.weixin.qq.com/miniprogram/dev/framework/security.msgSecCheck-v1.html)，1.0版本在2021年9月1日停止更新，请尽快更新至2.0

- 频率限制：单个 appId 调用上限为 4000 次/分钟，2,000,000 次/天。

## 5. 代码示例

### 5.1 HTTPS调用

请求示例

```json
{
  "openid": "OPENID",
  "scene": 1,
  "version": 2,
  "content": "hello world!"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "suggest": "risky",
    "label": 20001
  },
  "detail": [
    {
      "strategy": "content_model",
      "errcode": 0,
      "suggest": "risky",
      "label": 20006,
      "prob": 90
    },
    {
      "strategy": "keyword",
      "errcode": 0,
      "suggest": "pass",
      "label": 20006,
      "level": 20,
      "keyword": "命中的关键词1"
    },
    {
      "strategy": "keyword",
      "errcode": 0,
      "suggest": "risky",
      "label": 20006,
      "level": 90,
      "keyword": "命中的关键词2"
    }
  ],
  "trace_id": "60ae120f-371d5872-7941a05b"
}
```

### 5.2 云函数调用

请求示例

```json
const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
})
exports.main = async (event, context) => {
  try {
    const result = await cloud.openapi.security.msgSecCheck({
        "openid": 'OPENID',
        "scene": 1,
        "version": 2,
        "content": 'hello world!'
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
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "suggest": "risky",
    "label": 20001
  },
  "detail": [
    {
      "strategy": "content_model",
      "errcode": 0,
      "suggest": "risky",
      "label": 20006,
      "prob": 90
    },
    {
      "strategy": "keyword",
      "errcode": 0,
      "suggest": "pass",
      "label": 20006,
      "level": 20,
      "keyword": "命中的关键词1"
    },
    {
      "strategy": "keyword",
      "errcode": 0,
      "suggest": "risky",
      "label": 20006,
      "level": 90,
      "keyword": "命中的关键词2"
    }
  ],
  "trace_id": "60ae120f-371d5872-7941a05b"
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
