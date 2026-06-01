# 查询订单列表

> 官方文档：[查询订单列表](https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_getorderlist.html)
> 所属分类：[小程序交易管理服务](../小程序交易管理服务目录.md)
> 导航路径：小程序交易管理服务 / 查询订单列表
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getOrderList

可以通过支付时间、支付者openid或订单状态来查询订单列表。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/order/get_order_list?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：wxa.sec.order.getOrderList
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.pay_time_range Object Payload

支付时间所属范围。

## 3. 返回参数

### 返回体 Response Payload

### Res.order_list Object Payload

支付单信息列表。

### Res.order_list.shipping Object Payload

发货信息。

### Res.order_list.shipping.shipping_list(Array) Object Payload

物流信息列表，发货物流单列表，支持统一发货（单个物流单）和分拆发货（多个物流单）两种模式。

### Res.order_list.shipping.shipping_list(Array).contact Object Payload

联系方式。

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
    "pay_time_range": {
        "begin_time": 1670563531,
        "end_time": 1670563531
    },
    "page_size": 2
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "order_list": [
        {
            "transaction_id": "fake-transid-20221209132531-0",
            "merchant_trade_no": "fake-tradeno-20221209132531-0",
            "merchant_id": "fake-mchid-123",
            "sub_merchant_id": "",
            "description": "",
            "paid_amount": 4353,
            "openid": "ogqztkPsejM9MQAFfwCQSCi4oNg3",
            "trade_create_time": 1670563531,
            "pay_time": 1670563531,
            "order_state": 1,
            "in_complaint": false,
            "shipping": {}
        },
        {
            "transaction_id": "fake-transid-20221209132531-1",
            "merchant_trade_no": "fake-tradeno-20221209132531-1",
            "merchant_id": "fake-mchid-123",
            "sub_merchant_id": "",
            "description": "",
            "paid_amount": 29767,
            "openid": "ogqztkPsejM9MQAFfwCQSCi4oNg3",
            "trade_create_time": 1670563531,
            "pay_time": 1670563531,
            "order_state": 1,
            "in_complaint": false,
            "shipping": {}
        }
    ],
    "last_index": "092dd3cecbc6926301",
    "has_more": true
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
