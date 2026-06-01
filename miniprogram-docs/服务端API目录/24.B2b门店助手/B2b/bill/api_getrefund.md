# 查询退款

> 官方文档：[查询退款](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_getrefund.html)
> 所属分类：[B2b门店助手](../../B2b门店助手目录.md)
> 导航路径：B2b门店助手 / B2b支付 / 查询退款
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getRefund

该接口用于查询B2b退款单信息

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/retail/B2b/getrefund?access_token=ACCESS_TOKEN&pay_sig=pay_sig
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

### Res.amount Object Payload

金额信息。金额详细信息，仅支持人民币

### Res.refund_channel_info Object Payload

退款渠道信息，仅支付方式为微信支付且订单退款成功后返回

## 4. 注意事项

- 一笔订单最多支持部分退款50次。

## 5. 代码示例

请求示例

```json
{
  "mchid": "1230000109",
  "out_refund_no": "12177525012014070332321235"
}
或
{
  "mchid": "1230000109",
  "refund_id": "r202307281444591411763685"
}
```

返回示例

```json
{
  "refund_id": "r202307281444591411763685",
  "out_refund_no": "12177525012014070332321235",
  "order_id": "o202307291423123564754773",
  "out_trade_no": "1217752501201407033233368018",
  "create_time": "2023-07-30 17:04:23",
  "refund_time": "2023-07-30 17:04:28",
  "refund_status": "REFUND_SUCC",
  "amount": {
    "order_amount": 1300,
	"refund_amount": 100,
	"currency": "CNY"
  },
  "wxpay_refund_id": "1235481444591411763685",
  "reverse_sett_state": 3,
  "refund_channel_info": {
      "channel": "ORIGINAL",
      "user_received_account": "招商银行借记卡0000",
      "funds_account": "UNAVAILABLE"
  },
  "description":"",
  "errcode": 0,
  "errmsg": OK
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
