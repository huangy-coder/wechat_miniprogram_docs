# 选用模板

> 官方文档：[选用模板](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_addwxanewtemplate.html)
> 所属分类：[消息相关](../../消息相关目录.md)
> 导航路径：消息相关 / 订阅消息 / 选用模板
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：addwxanewtemplate

从公共模板库中选用模板到私有模板库

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxaapi/newtmpl/addtemplate?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：officialAccount.newtmpl.addTemplate
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18、89
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1.模板标题 id可通过接口获取或后台查看
2.关键词组合需2-5个
3.服务场景描述限制15字

## 5. 代码示例

### 5.1 选用模板

请求示例

```json
{
  "tid": "401",
  "kidList": [
    1,
    2
  ],
  "sceneDesc": "测试数据"
}
```

返回示例

```json
{
  "errmsg": "ok",
  "errcode": 0,
  "priTmplId": "9Aw5ZV1j9xdWTFEkqCpZ7jWySL7aGN6rQom4gXINfJs"
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
    const result = await cloud.openapi({ convertCase: false }).subscribeMessage.addTemplate({
        "tid": '401',
        "kidList": [
          1,
          2
        ],
        "sceneDesc": '测试数据'
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
  "errMsg": "openapi.subscribeMessage.addTemplate:ok",
  "errCode": 0,
  "priTmplId": "9Aw5ZV1j9xdWTFEkqCpZ7jWySL7aGN6rQom4gXINfJs"
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
