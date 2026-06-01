# 查询账户余额

> 官方文档：[查询账户余额](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_getmchbalance.html)
> 所属分类：[B2b门店助手](../../B2b门店助手目录.md)
> 导航路径：B2b门店助手 / B2b支付 / 查询账户余额
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getMchBalance

查询B2b商户号下的余额

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/retail/B2b/getmchbalance?access_token=ACCESS_TOKEN&pay_sig=pay_sig
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：158
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.balance_list(Array) Object Payload

账户资金。商户号的账户资金

## 4. 枚举信息

### Res.balance_list(Array).balance_type Enum

资金类型。

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

请求示例

```json
{
    "mchid": "1230000109"
}
```

返回示例

```json
{
  "balance_list": [
    {
      "balance_type": "BALANCE_TYPE_AVAILABLE",
      "amount": "0.00",
      "currency": "CNY"
    },
    {
      "balance_type": "BALANCE_TYPE_FROZEN",
      "amount": "0.00",
      "currency": "CNY"
    }
  ],
  "errcode": 0,
  "errmsg": "OK"
}
```

## 7. 错误码

此接口没有特殊错误码，可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
