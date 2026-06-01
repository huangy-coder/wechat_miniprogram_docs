# 发起订阅扣款

> 官方文档：[发起订阅扣款](https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_submit_subscribe_pay_order.html)
> 所属分类：[虚拟支付](../虚拟支付目录.md)
> 导航路径：虚拟支付 / 发起订阅扣款
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：submit_subscribe_pay_order

本接口用于发起订阅扣款

受理后扣款，返回成功仅代表受理成功，不代表扣款成功。扣款成功后再通过xpay_goods_deliver_notify通知

如受理成功后，通知/查询到扣款失败，可在【t日～t+6日】发起重试，同一用户、同一道具，一个小时内仅可以重试一次。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/xpay/submit_subscribe_pay_order?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：157
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
    "openid": "",
    "offer_id": "",
    "buy_quantity": 0,
    "env": 0,
    "currency_type": "",
    "product_id": "",
    "deduct_price": 0,
    "order_id": "",
    "attach": ""
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": ""
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
