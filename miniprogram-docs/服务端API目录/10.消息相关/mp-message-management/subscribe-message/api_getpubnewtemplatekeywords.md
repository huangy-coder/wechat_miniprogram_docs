# 获取模板中的关键词

> 官方文档：[获取模板中的关键词](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_getpubnewtemplatekeywords.html)
> 所属分类：[消息相关](../../消息相关目录.md)
> 导航路径：消息相关 / 订阅消息 / 获取模板中的关键词
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getpubnewtemplatekeywords

该接口用于获取模板标题下的关键词列表。

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/wxaapi/newtmpl/getpubtemplatekeywords?access_token=ACCESS_TOKEN&tid=TID
```

### 云调用

- 调用方法：officialAccount.newtmpl.getPubTemplateKeywords
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18、89
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

无

## 3. 返回参数

### 返回体 Response Payload

### Res.data(Array) Object Payload

关键词列表

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

### 5.1 HTTPS请求示例

请求示例

```bash
https://api.weixin.qq.com/wxaapi/newtmpl/getpubtemplatekeywords?access_token=ACCESS_TOKEN&tid=99
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "kid": 1,
      "name": "物品名称",
      "example": "名称",
      "rule": "thing"
    }
  ]
}
```

### 5.2 云函数调用示例

请求示例

```js
const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
})
exports.main = async (event, context) => {
  try {
    const result = await cloud.openapi.subscribeMessage.getPubTemplateKeyWordsById({
        "tid": ''
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
  "errMsg": "openapi.subscribeMessage.getPubTemplateKeyWordsById:ok",
  "data": [
    {
      "kid": 1,
      "name": "物品名称",
      "example": "名称",
      "rule": "thing"
    }
  ]
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

- ✔：该账号可调用此接口。
- 仅认证：表示仅允许企业主体已认证账号调用，未认证或不支持认证的账号无法调用。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
