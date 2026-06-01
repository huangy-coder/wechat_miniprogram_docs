# 查询订单发货状态

> 官方文档：[查询订单发货状态](https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_getorder.html)
> 所属分类：[小程序交易管理服务](../小程序交易管理服务目录.md)
> 导航路径：小程序交易管理服务 / 查询订单发货状态
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getOrder

可以通过交易单号或商户号+商户单号来查询该支付单的发货状态。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/order/get_order?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：wxa.sec.order.getOrder
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：142
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.order Object Payload

支付单信息。

### Res.order.shipping Object Payload

发货信息。

### Res.order.shipping.shipping_list(Array) Object Payload

物流信息列表，发货物流单列表，支持统一发货（单个物流单）和分拆发货（多个物流单）两种模式。

### Res.order.shipping.shipping_list(Array).contact Object Payload

联系方式。

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
    "transaction_id": "fake-transid-20221209132531-44",
    "merchant_id": "fake-mchid-123",
    "merchant_trade_no": "fake-tradeno-20221209132531-44"
}
```

返回示例

```json
{ 
    "errcode": 0,
    "errmsg": "ok",
    "order": {
        "transaction_id": "fake-transid-20221209132531-44",
        "merchant_trade_no": "fake-tradeno-20221209132531-44",
        "merchant_id": "fake-mchid-123",
        "sub_merchant_id": "",
        "description": "🍌*1",
        "paid_amount": 916,
        "openid": "ogqztkPsejM9MQAFfwCQSCi4oNg3",
        "trade_create_time": 1670563533,
        "pay_time": 1670563533,
        "in_complaint": false,
        "order_state": 2,
        "shipping": {
            "delivery_mode": 1,
            "logistics_type": 1,
            "finish_shipping": true,
            "finish_shipping_count": 1,
            "goods_desc": "🍌*1",
            "shipping_list": [
                {
                    "tracking_no": "JT1234567890",
                    "express_company": "JTSD",
                    "upload_time": 1670832735
                }
            ]
        }
    }
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
