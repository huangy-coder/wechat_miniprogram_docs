# 批量获取运单数据

> 官方文档：[批量获取运单数据](https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_batchgetorder.html)
> 所属分类：[物流助手](../../物流助手目录.md)
> 导航路径：物流助手 / 小程序使用 / 批量获取运单数据
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：batchGetOrder

该接口用于批量获取运单数据。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/business/order/batchget?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：logistics.batchGetOrder
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：45、71
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.order_list(Array) Object Payload

订单列表, 最多不能超过100个

## 3. 返回参数

### 返回体 Response Payload

### Res.order_list(Array) Object Payload

运单列表

### Res.order_list(Array).waybill_data Object Payload

运单信息

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

### 5.1 HTTPS调用

请求示例

```json
{
  "order_list": [
    {
      "order_id": "01234567890123456789",
      "delivery_id": "SF",
      "waybill_id": "123456789"
    },
    {
      "order_id": "01234567890123456789",
      "delivery_id": "SF",
      "waybill_id": "123456789"
    }
  ]
}
```

返回示例

```json
{
  "order_list": [
    {
      "errcode": 0,
      "errmsg": "ok",
      "order_id": "01234567890123456789",
      "delivery_id": "SF",
      "waybill_id": "123456789",
      "print_html": "jh7DjipP4ul4CQYUh69cniskrQZuOPwa1inAbXIqKbU0t71c0s65Au54cdWBZW0QJY4LYeofdM",
      "waybill_data": [
        {
          "key": "SF_bagAddr",
          "value": "广州"
        },
        {
          "key": "SF_mark",
          "value": "101- 07-03 509"
        }
      ],
      "order_status": 0
    },
    {
      "errcode": 0,
      "errmsg": "ok",
      "order_id": "01234567890123456789_2",
      "delivery_id": "SF",
      "waybill_id": "123456789_2",
      "print_html": "jh7DjipP4ul4CQYUh69cniskrQZuOPwa1inAbXIqKbU0t71c0s65Au54cdWBZW0QJY4LYeofdM",
      "waybill_data": [
        {
          "key": "SF_bagAddr",
          "value": "广州"
        },
        {
          "key": "SF_mark",
          "value": "101- 07-03 509"
        }
      ],
      "order_status": 0
    }
  ]
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
    const result = await cloud.openapi.logistics.batchGetOrder({
        "orderList": [
          {
            "orderId": '01234567890123456789',
            "deliveryId": 'SF',
            "waybillId": '123456789'
          },
          {
            "orderId": '01234567890123456789',
            "deliveryId": 'SF',
            "waybillId": '123456789'
          }
        ]
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
  "orderList": [
    {
      "errcode": 0,
      "errmsg": "ok",
      "orderId": "01234567890123456789",
      "deliveryId": "SF",
      "waybillId": "123456789",
      "printHtml": "jh7DjipP4ul4CQYUh69cniskrQZuOPwa1inAbXIqKbU0t71c0s65Au54cdWBZW0QJY4LYeofdM",
      "waybillData": [
        {
          "key": "SF_bagAddr",
          "value": "广州"
        },
        {
          "key": "SF_mark",
          "value": "101- 07-03 509"
        }
      ],
      "orderStatus": 0
    },
    {
      "errcode": 0,
      "errmsg": "ok",
      "orderId": "01234567890123456789_2",
      "deliveryId": "SF",
      "waybillId": "123456789_2",
      "printHtml": "jh7DjipP4ul4CQYUh69cniskrQZuOPwa1inAbXIqKbU0t71c0s65Au54cdWBZW0QJY4LYeofdM",
      "waybillData": [
        {
          "key": "SF_bagAddr",
          "value": "广州"
        },
        {
          "key": "SF_mark",
          "value": "101- 07-03 509"
        }
      ],
      "orderStatus": 0
    }
  ],
  "errMsg": "openapi.logistics.batchGetOrder:ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口支持「小程序（仅认证）」账号类型调用。其他账号类型如无特殊说明，均不可调用。
