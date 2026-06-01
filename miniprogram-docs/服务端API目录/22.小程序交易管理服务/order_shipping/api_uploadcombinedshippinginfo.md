# 发货信息合单录入

> 官方文档：[发货信息合单录入](https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_uploadcombinedshippinginfo.html)
> 所属分类：[小程序交易管理服务](../小程序交易管理服务目录.md)
> 导航路径：小程序交易管理服务 / 发货信息合单录入
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：uploadCombinedShippingInfo

用户交易后，默认资金将会进入冻结状态，开发者在发货后，需要在小程序平台录入相关发货信息，平台会将发货信息以消息的形式推送给购买的微信用户。

如果你已经录入发货信息，在用户尚未确认收货的情况下可以通过该接口修改发货信息，但一个支付单只能更新一次发货信息，请谨慎操作。

如暂时没有完成相关API的对接开发工作，你也可以登陆小程序的后台，通过发货信息录入页面手动录入发货信息。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/order/upload_combined_shipping_info?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：wxa.sec.order.uploadCombinedShippingInfo
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：142
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.order_key Object Payload

合单订单，需要上传物流详情的合单订单，根据订单类型二选一

### Body.sub_orders(Array) Object Payload

子单物流详情

### Body.payer Object Payload

支付者，支付者信息

### Body.sub_orders(Array).order_key Object Payload

需要上传物流详情的子单订单，订单类型与合单订单保持一致

### Body.sub_orders(Array).shipping_list Object Payload

子单物流信息列表 多重性: [1, 15]

### Body.sub_orders(Array).shipping_list .contact Object Payload

联系方式，当发货的物流公司为顺丰时，联系方式为必填，收件人或寄件人联系方式二选一

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1.根据指定的订单单号类型，采用不同参数给指定订单上传物流信息，注意子单和主单的订单单号类型必须一致：

(1). 商户侧单号形式（枚举值1），通过下单商户号和商户侧单号确定一笔订单。

(2). 微信支付单号形式（枚举值2），通过微信支付单号确定一笔订单。

2.发货模式根据具体发货情况选择：

(1). 统一发货（枚举值1），一笔订单统一发货，只有一个物流单号。

(2). 分拆发货（枚举值2），一笔订单分拆发货，包括多个物流单号。

3.物流公司编码，参见[获取运力 id 列表get_delivery_list](https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-msg/api_get_delivery_list)。

4.上传时间，用于标识请求的先后顺序，如果要更新物流信息，上传时间必须比之前的请求更新，请按照RFC 3339格式填写。

5.分拆发货仅支持使用物流快递发货，一笔支付单最多分拆成 15 个包裹。

6.以下情况将视为重新发货，每笔支付单仅有一次重新发货机会。

(1). 对已完成发货的支付单再次调用该 API。

(2). 使用该 API 修改发货模式或物流模式。

## 5. 代码示例

请求示例

```json
{
    "order_key": {
        "order_number_type": 1,
        "mchid": "fake-mchid-123",
        "out_trade_no": "fake-tradeno-20221214190427-0"
    },
    "sub_orders": [
        {
            "order_key": {
                "order_number_type": 1,
                "mchid": "fake-mchid-123",
                "out_trade_no": "fake-tradeno-20221214190427-01"
            },
            "delivery_mode": 2,
            "logistics_type": 1,
            "is_all_delivered": true,
            "shipping_list": [
                {
                    "tracking_no": "fake-trackingno-202212141904271",
                    "express_company": "YD",
                    "item_desc": "微信气泡狗零钱包*1",
                    "contact": {
                        "consignor_contact": "021-**34-12"
                    }
                },
                {
                    "tracking_no": "fake-trackingno-202212141904272",
                    "express_company": "DHL",
                    "item_desc": "微信黄脸布艺胸针*1；微信气泡狗零钱包*1",
                    "contact": {
                        "consignor_contact": "021-**34-12"
                    }
                }
            ]
        },
        {
            "order_key": {
                "order_number_type": 1,
                "mchid": "fake-mchid-321",
                "out_trade_no": "fake-tradeno-20221214190427-02"
            },
            "delivery_mode": 1,
            "logistics_type": 1,
            "shipping_list": [
                {
                    "tracking_no": "fake-trackingno-202212141904273",
                    "express_company": "YTO",
                    "item_desc": "微信气泡狗双面钥匙扣*1",
                    "contact": {
                        "receiver_contact": "+86-123****4321"
                    }
                }
            ]
        }
    ],
    "upload_time": "2022-12-15T13:29:35.120+08:00",
    "payer": {
        "openid": "ogqztkPsejM9MQAFfwCQSCi4oNg3"
    }
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
