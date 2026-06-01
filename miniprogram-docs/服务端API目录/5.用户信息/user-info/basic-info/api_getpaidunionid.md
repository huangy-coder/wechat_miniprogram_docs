# 支付后获取Unionid

> 官方文档：[支付后获取Unionid](https://developers.weixin.qq.com/miniprogram/dev/server/API/user-info/basic-info/api_getpaidunionid.html)
> 所属分类：[用户信息](../../用户信息目录.md)
> 导航路径：用户信息 / 用户信息 / 支付后获取Unionid
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getPaidUnionid

该接口用于在用户支付完成后，获调用本接口前需要用户完成支付，用户支付完成后，取该用户的 UnionId，无需用户授权。本接口支付后的五分钟内有效。

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/wxa/getpaidunionid?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：auth.getPaidUnionId
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

## 4. 注意事项

- 调用前需要用户完成支付，且在支付后的五分钟内有效。
- 使用微信支付订单号（transaction_id）和微信支付商户订单号和微信支付商户号（out_trade_no 及 mch_id），二选一

## 5. 代码示例

### 5.1 使用微信支付订单号

请求示例

```bash
GET https://api.weixin.qq.com/wxa/getpaidunionid?access_token=ACCESS_TOKEN&openid=OPENID&transaction_id=TRANSACTION_ID
```

返回示例

```json
{
  "unionid": "oTmHYjg-tElZ68xxxxxxxxhy1Rgk",
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.2 使用微信支付商户订单号和微信支付商户号（out_trade_no 及 mch_id）

请求示例

```bash
GET https://api.weixin.qq.com/wxa/getpaidunionid?access_token=ACCESS_TOKEN&openid=OPENID&mch_id=MCH_ID&out_trade_no=OUT_TRADE_NO
```

返回示例

```json
{
  "unionid": "oTmHYjg-tElZ68xxxxxxxxhy1Rgk",
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.3 云函数示例

请求示例

```js
const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
})
exports.main = async (event, context) => {
  try {
    const result = await cloud.openapi.auth.getPaidUnionId({
        "openid": '',
        "transactionId": '',
        "mchId": '',
        "outTradeNo": ''
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
  "unionid": "oTmHYjg-tElZ68xxxxxxxxhy1Rgk",
  "errCode": 0,
  "errMsg": "openapi.auth.getPaidUnionId:ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口支持「小程序（仅认证）」账号类型调用。其他账号类型如无特殊说明，均不可调用。
