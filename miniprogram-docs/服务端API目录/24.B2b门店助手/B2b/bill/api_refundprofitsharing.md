# 请求分账回退

> 官方文档：[请求分账回退](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_refundprofitsharing.html)
> 所属分类：[B2b门店助手](../../B2b门店助手目录.md)
> 导航路径：B2b门店助手 / B2b支付 / 请求分账回退
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：refundProfitSharing

已分账订单，在完成退款后，通过调用此接口，可将已分账的资金从分账接收方的账户回退给分账方。单笔退款单对单个分账接收方只能回退一次。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/retail/B2b/refundprofitsharing?access_token=ACCESS_TOKEN&pay_sig=pay_sig
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

## 4. 注意事项

- 目前单笔退款单，对单个收款方（之前分账时的分账接收方），只支持发起一次回退。
- 不支持回退给自己，分账回退出资商户不允许和接收商户相同
- 不支持“分账给个人”的分账单发起分账回退。

# 发起分账的支付单的退款规则说明

| 订单分账状态 | 申请退款金额 | 退款前提 | 退款出款账户 |
| --- | --- | --- | --- |
| 订单标记为需要分账 | 申请全额退款 | 1、需要先调“完成分账”接口，将订单剩余冻结资金从“待结算金额”账户全部解冻至“可提现金额”账户 <br>2、“可提现金额”账户余额≥申请退款金额，支付单扣除手续费将在退款成功后返还 | “可提现金额”账户 |
|   | 申请部分退款 | 当申请退款金额≤订单未分账冻结金额，直接可退 | “待结算金额”账户 |
|   |   | 1、当申请退款金额＞订单未分账冻结金额，需要先调“完成分账”接口，将订单剩余冻结资金从“待结算金额”账户全部解冻至“可提现金额”账户 <br> 2、“可提现金额”账户余额≥申请退款金额，支付单扣除手续费将在退款成功后返还 | “可提现金额”账户 |
| 订单已完结分账 | 申请全额/部分退款 | “可提现金额”账户余额≥申请退款金额，支付单扣除手续费将在退款成功后返还 | “可提现金额”账户 |

## 5. 代码示例

请求示例

```json
{
  "out_trade_no": "40012891249207515929",
  "out_refund_no": "4001289124357515929",
  "payee_type": "PAYEE_TYPE_EXTERNAL_MERCHANT",
  "payee_id": "165406451",
  "mchid": "166321431"
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
