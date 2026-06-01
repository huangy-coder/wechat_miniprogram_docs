# 调用服务市场接口

> 官方文档：[调用服务市场接口](https://developers.weixin.qq.com/miniprogram/dev/server/API/wx-service-market/api_invokeservice.html)
> 所属分类：[微信服务市场](../微信服务市场目录.md)
> 导航路径：微信服务市场 / 调用服务市场接口
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：invokeService

该接口用于调用服务平台上架的api，适用于公众号、小程序和第三方平台调用，区别仅仅在于access_token的生成而已。

##### 服务ID和接口名

可通过如下方式找到服务id和接口名称


## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/servicemarket?access_token=ACCESS_TOKEN
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 调用方法：serviceMarket.invokeService
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：66-67
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

### 5.1 HTTPS同步调用

请求示例

```json
{
  "service" : "wx79ac3de8be320b71",
  "api" : "OcrAllInOne",
  "data" : {
    "img_url": "http://mmbiz.qpic.cn/mmbiz_jpg/7UFjuNbYxibu66xSqsQqKcuoGBZM77HIyibdiczeWibdMeA2XMt5oibWVQMgDibriazJSOibLqZxcO6DVVcZMxDKgeAtbQ/0",
    "data_type": 3,
    "ocr_type": 1
  },
  "client_msg_id" : "id123"
}
```

返回示例

```json
{
 "errcode": 0,
 "errmsg": "ok",
 "data": "{\"idcard_res\":{\"type\":0,\"name\":{\"text\":\"abc\",\"pos\"…0312500}}},\"image_width\":480,\"image_height\":304}}"
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
    const result = await cloud.openapi({ convertCase: false }).serviceMarket.invokeService({
        "service": 'wx79ac3de8be320b71',
        "api": 'OcrAllInOne',
        "data": {
          "img_url": 'http://mmbiz.qpic.cn/mmbiz_jpg/7UFjuNbYxibu66xSqsQqKcuoGBZM77HIyibdiczeWibdMeA2XMt5oibWVQMgDibriazJSOibLqZxcO6DVVcZMxDKgeAtbQ/0',
          "data_type": 3,
          "ocr_type": 1
        },
        "client_msg_id": 'id123'
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
  "errMsg": "openapi.serviceMarket.invokeService:ok",
  "data": "{\"idcard_res\":{\"type\":0,\"name\":{\"text\":\"abc\",\"pos\"…0312500}}},\"image_width\":480,\"image_height\":304}}"
}
```

### 5.3 HTTPS异步调用

请求示例

```json
 {
    "service" : "wxee446d7507c68b11",
    "api" : "SecCheckAsync",
    "data" : {
     "BusinessType": 1,
       "MediaType": 1,
       "TextContent": "hello",
        "MediaUrl": "http://example.com/example.jpg"
    },
    "client_msg_id" : "random_id_456",
    "async" : true,
    "client_msg_id" : "id123"
}
```

返回示例

```json
{
 "errcode": 0,
 "errmsg": "ok",
 "request_id": "MLwFmCkCxNOthxteVMf3UFWRmb9VPwTMTuxJUAUD-svS-6AqBC9tbzZzDyHFglQ5_aI"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

| 小程序 | 公众号 | 服务号 | 小游戏 | 移动应用 | 视频号助手 |
| --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

- ✔：该账号可调用此接口。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
