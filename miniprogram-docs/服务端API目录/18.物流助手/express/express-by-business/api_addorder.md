# 生成运单

> 官方文档：[生成运单](https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_addorder.html)
> 所属分类：[物流助手](../../物流助手目录.md)
> 导航路径：物流助手 / 小程序使用 / 生成运单
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：addOrder

该接口用于生成运单。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/business/order/add?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：logistics.addOrder
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：45、71
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.sender Object Payload

发件人信息

### Body.receiver Object Payload

收件人信息

### Body.cargo Object Payload

包裹信息，将传递给快递公司

### Body.shop Object Payload

商品信息，会展示到物流服务通知和电子面单中

### Body.insured Object Payload

保价信息

### Body.service Object Payload

服务类型

### Body.cargo.detail_list(Array) Object Payload

货物总重量，单位是千克(kg)

### Body.shop.detail_list Object Payload

商品详情列表，适配多商品场景，用以消息落地页展示。（新规范，新接入商家建议用此字段）

## 3. 返回参数

### 返回体 Response Payload

### Res.waybill_data(Array) Object Payload

运单信息，下单成功时返回

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

### 5.1 下单成功的例子

请求示例

```json
{
  "add_source": 0,
  "order_id": "01234567890123456789",
  "openid": "oABC123456",
  "delivery_id": "SF",
  "biz_id": "xyz",
  "custom_remark": "易碎物品",
  "sender": {
    "name": "张三",
    "tel": "020-88888888",
    "mobile": "18666666666",
    "company": "公司名",
    "post_code": "123456",
    "country": "中国",
    "province": "广东省",
    "city": "广州市",
    "area": "海珠区",
    "address": "XX路XX号XX大厦XX栋XX"
  },
  "receiver": {
    "name": "王小蒙",
    "tel": "020-77777777",
    "mobile": "18610000000",
    "company": "公司名",
    "post_code": "654321",
    "country": "中国",
    "province": "广东省",
    "city": "广州市",
    "area": "天河区",
    "address": "XX路XX号XX大厦XX栋XX"
  },
  "shop": {
    "wxa_path": "/index/index?from=waybill&id=01234567890123456789",
    "detail_list": [
      {
        "goods_name": "微信气泡狗抱枕（小号）",
        "goods_img_url": "https://mmbiz.qpic.cn/mmbiz_png/OiaFLUqewuIDNQnTiaCInIG8ibdosYHhQHPbXJUrqYSNIcBL60vo4LIjlcoNG1QPkeH5GWWEB41Ny895CokeAah8A/640",
        "goods_desc": "40cm * 40cm尺寸"
      },
      {
        "goods_name": "微信气泡狗抱枕（中号）",
        "goods_img_url": "https://mmbiz.qpic.cn/mmbiz_png/OiaFLUqewuIDNQnTiaCInIG8ibdosYHhQHPbXJUrqYSNIcBL60vo4LIjlcoNG1QPkeH5GWWEB41Ny895CokeAah8A/640",
        "goods_desc": "50cm * 50cm尺寸"
      }
    ]
  },
  "cargo": {
    "count": 2,
    "weight": 5.5,
    "space_x": 30.5,
    "space_y": 20,
    "space_z": 20,
    "detail_list":[{
"name":"微信气泡狗抱枕（中号)",
"count":1
},{"name":"微信气泡狗（大号）"，
”count":1}]
  },
  "insured": {
    "use_insured": 1,
    "insured_value": 10000
  },
  "service": {
    "service_type": 0,
    "service_name": "标准快递"
  }
}
```

返回示例

```json
{
  "order_id": "01234567890123456789",
  "waybill_id": "123456789",
  "waybill_data": [
    {
      "key": "SF_bagAddr",
      "value": "广州"
    },
    {
      "key": "SF_mark",
      "value": "101- 07-03 509"
    }
  ]
}
```

### 5.2 下单失败的例子

请求示例

```json
{
  "add_source": 0,
  "order_id": "01234567890123456789",
  "openid": "oABC123456",
  "delivery_id": "SF",
  "biz_id": "xyz",
  "custom_remark": "易碎物品",
  "sender": {
    "name": "张三",
    "tel": "020-88888888",
    "mobile": "18666666666",
    "company": "公司名",
    "post_code": "123456",
    "country": "中国",
    "province": "广东省",
    "city": "广州市",
    "area": "海珠区",
    "address": "XX路XX号XX大厦XX栋XX"
  },
  "receiver": {
    "name": "王小蒙",
    "tel": "020-77777777",
    "mobile": "18610000000",
    "company": "公司名",
    "post_code": "654321",
    "country": "中国",
    "province": "广东省",
    "city": "广州市",
    "area": "天河区",
    "address": "XX路XX号XX大厦XX栋XX"
  },
  "shop": {
    "wxa_path": "/index/index?from=waybill&id=01234567890123456789",
    "detail_list": [
      {
        "goods_name": "微信气泡狗抱枕（小号）",
        "goods_img_url": "https://mmbiz.qpic.cn/mmbiz_png/OiaFLUqewuIDNQnTiaCInIG8ibdosYHhQHPbXJUrqYSNIcBL60vo4LIjlcoNG1QPkeH5GWWEB41Ny895CokeAah8A/640",
        "goods_desc": "40cm * 40cm尺寸"
      },
      {
        "goods_name": "微信气泡狗抱枕（中号）",
        "goods_img_url": "https://mmbiz.qpic.cn/mmbiz_png/OiaFLUqewuIDNQnTiaCInIG8ibdosYHhQHPbXJUrqYSNIcBL60vo4LIjlcoNG1QPkeH5GWWEB41Ny895CokeAah8A/640",
        "goods_desc": "50cm * 50cm尺寸"
      }
    ]
  },
  "cargo": {
    "count": 2,
    "weight": 5.5,
    "space_x": 30.5,
    "space_y": 20,
    "space_z": 20,
    "detail_list":[{
"name":"微信气泡狗抱枕（中号)",
"count":1
},{"name":"微信气泡狗（大号）"，
”count":1}]
  },
  "insured": {
    "use_insured": 1,
    "insured_value": 10000
  },
  "service": {
    "service_type": 0,
    "service_name": "标准快递"
  }
}
```

返回示例

```json
{
  "errcode": 9300501,
  "errmsg": "delivery logic fail",
  "delivery_resultcode": 10002,
  "delivery_resultmsg": "客户密码不正确"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口支持「小程序（仅认证）」账号类型调用。其他账号类型如无特殊说明，均不可调用。
