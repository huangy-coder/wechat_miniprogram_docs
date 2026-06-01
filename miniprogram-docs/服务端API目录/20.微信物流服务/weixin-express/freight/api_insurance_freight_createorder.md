# 发货时投保

> 官方文档：[发货时投保](https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_createorder.html)
> 所属分类：[微信物流服务](../../微信物流服务目录.md)
> 导航路径：微信物流服务 / 无忧退货 / 发货时投保
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：insurance_freight_createorder

本接口用于发货时投保

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/business/insurance_freight/createorder?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：139
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.delivery_place Object Payload

发货地址

> 以下参数也使用此结构：

> - Body.receipt_place ： 收货地址

### Body.product_info Object Payload

投保订单信息，用于微信下发投保和理赔通知给用户，用户点击可查看投保订单，点击订单可跳回商家小程序

### Body.product_info.goods_list(Array) Object Payload

投保商品list，一个元素为对象的数组

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
  "openid":"oZGTP5DwGDPfEf1EBBHH_oxHw2aU",
  "order_no": "4200001197202103228672982585",
  "pay_amount": 1,
  "pay_time": 1679473667,
  "delivery_place":{
      "province":"广东省",
      "city": "广州市",
      "county": "海珠区",
      "address": "创业园23号"
  },
  "receipt_place":{
      "province":"广东省",
      "city": "惠州市",
      "county": "惠普区",
      "address": "龙山村10-2"
  },
  "delivery_no": "d20230322001"
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "policy_no": "10288003264673876282",
    "insurance_end_date": "2023-06-20 16:36:54",
    "estimate_amount": 1200
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。
