# 查询js错误详情

> 官方文档：[查询js错误详情](https://developers.weixin.qq.com/miniprogram/dev/server/API/operation/api_getjserrdetail.html)
> 所属分类：[运维中心](../运维中心目录.md)
> 导航路径：运维中心 / 查询js错误详情
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getJsErrDetail

该接口用于查询JS错误详情

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxaapi/log/jserr_detail?access_token=ACCESS_TOKEN
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 调用方法：operation.getJsErrDetail
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

### Res.data(Array) Object Payload

错误列表

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
  "startTime": "2021-01-25",
  "endTime": "2021-01-26",
  "errorMsgMd5": "f2fb4f8cd638466ad0e7607b01b7d0ca",
  "errorStackMd5": "795a63b70ce5755c7103611d93077603",
  "appVersion": "0",
  "sdkVersion": "0",
  "osName": "2",
  "clientVersion": "0",
  "openid": "",
  "offset": 0,
  "limit": 10,
  "desc": "0"
}
```

返回示例

```json
{
  "success": true,
  "openid": "",
  "data": [
    {
      "Count": "1",
      "sdkVersion": "2.14.1",
      "ClientVersion": "7.0.21",
      "errorStackMd5": "e371cd9cae821969c855f9f461327dac",
      "TimeStamp": "2021-01-25 16:36:39",
      "appVersion": "2.6.16",
      "errorMsgMd5": "53b4825ec4a41d966f88c298c718de80",
      "errorMsg": "errCode: -404012 polling exceed max timeout retry | errMsg: cloud.callFunction:fail polling exceed max timeout retry (callId: 1611553677669-0.2531087324274228) (trace: 13:47:57 start->13:48:12 timeout, retry->13:48:18 app hide->13:48:27 timeout, retry->13:48:42 timeout, abort); at cloud.callFunction api; ",
      "errorStack": "Error: errCode: -404012 polling exceed max timeout retry | errMsg: cloud.callFunction:fail polling exceed max timeout retry (callId: 1611553677669-0.2531087324274228) (trace: 13:47:57 start->13:48:12 timeout, retry->13:48:18 app hide->13:48:27 timeout, retry->13:48:42 timeout, abort); at cloud.callFunction api; \n    at new t (https://usr/app-service.js:2:320930)\n    at c (https://usr/app-service.js:2:321660)\n    at l (https://usr/app-service.js:2:321755)\n    at https://usr/app-service.js:2:297192\n    at https://usr/app-service.js:2:76398\n    at Object.next (https://usr/app-service.js:2:76503)\n    at s (https://usr/app-service.js:2:75234)",
      "Ds": "2021-01-25",
      "OsName": "1",
      "openId": "o-0YS0ZNM_bzkm13NKNUSwbrEkYU",
      "pluginversion": "0",
      "appId": "wxcff7381e631cf54e",
      "DeviceModel": "Redmi Note 5Aarm64-v8a",
      "source": "",
      "route": "",
      "Uin": "",
      "nickname": ""
    }
  ],
  "totalCount": 1,
  "errcode": 0
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
