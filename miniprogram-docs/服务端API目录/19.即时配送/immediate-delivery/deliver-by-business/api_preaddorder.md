# 预下配送单

> 官方文档：[预下配送单](https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_preaddorder.html)
> 所属分类：[即时配送](../../即时配送目录.md)
> 导航路径：即时配送 / 小程序使用 / 预下配送单
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：preAddOrder

#### 使用场景描述

- 在用户提交外卖订单时，商家可调用本接口查询配送公司是否可接单、预计多久接单、运费预估等。预估运费可作为展示给用户的运费参考值。
- 举个例子：商家通过预下配送单接口返回的预估运费是8元，商家可决定前端顾客下外卖单时展示给顾客看的运费是真实的8元，还是其他商家指定的金额。
- 说明：本接口非必须调用接口，若不需要获取配送公司是否可接单、预计多久接单、运费预估等，也可不调用本接口，直接下配送单。
- 顺丰同城可返回配送费用、配送距离、预计骑手接单时间，不支持返回delivery_token。
- 闪送可返回配送费用、配送距离、预计骑手接单时间，不支持返回delivery_token。
- 美团配送返回0时表示校验通过，不支持返回配送费用、配送距离、预计骑手接单时间和delivery_token。
- 达达支持预下单查询配送费用、配送距离、预计骑手接单时间和delivery_token(有效期3分钟)

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/local/business/order/pre_add?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：51、71
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.sender Object Payload

发件人信息，闪送、顺丰同城急送必须填写，美团配送、达达，若传了shop_no的值可不填该字段

### Body.receiver Object Payload

收件人信息

### Body.cargo Object Payload

货物信息

### Body.order_info Object Payload

订单信息

### Body.shop Object Payload

商品信息，会展示到物流通知消息中

### Body.cargo.goods_detail Object Payload

货物详情，最长不超过10240个字符

### Body.cargo.goods_detail.goods(Array) Object Payload

货物列表

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Body.cargo.cargo_first_class Enum

品类一级类目,

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

### 6.1 HTTPS调用成功返回

请求示例

```json
{
   "cargo": {
       "cargo_first_class": "美食夜宵",
       "cargo_second_class": "零食小吃",
       "goods_detail": {
           "goods": [
               {
                   "good_count": 1,
                   "good_name": "水果",
                   "good_price": 10,
                   "good_unit": "元"
               },
               {
                   "good_count": 2,
                   "good_name": "蔬菜",
                   "good_price": 20,
                   "good_unit": "元"
               }
           ]
       },
       "goods_height": 1,
       "goods_length": 3,
       "goods_value": 5,
       "goods_weight": 1,
       "goods_width": 2
   },
   "delivery_id": "SFTC",
   "delivery_sign": "01234567890123456789",
   "openid": "oABC123456",
   "order_info": {
       "delivery_service_code": "",
       "expected_delivery_time": 0,
       "is_direct_delivery": 0,
       "is_finish_code_needed": 1,
       "is_insured": 0,
       "is_pickup_code_needed": 1,
       "note": "test_note",
       "order_time": 1555220757,
       "order_type": 0,
       "poi_seq": "1111",
       "tips": 0
   },
   "receiver": {
       "address": "xxx地铁站",
       "address_detail": "2号楼202",
       "city": "北京市",
       "coordinate_type": 0,
       "lat": 40.1529600000,
       "lng": 116.5060300000,
       "name": "老王",
       "phone": "18512345678"
   },
   "sender": {
       "address": "xx大厦",
       "address_detail": "1号楼101",
       "city": "北京市",
       "coordinate_type": 0,
       "lat": 40.4486120000,
       "lng": 116.3830750000,
       "name": "刘一",
       "phone": "13712345678"
   },
   "shop": {
       "goods_count": 2,
       "goods_name": "宝贝",
       "img_url": "https://mmbiz.qpic.cn/mmbiz_png/xxxxxxxxx/0?wx_fmt=png",
       "wxa_path": "/page/index/index"
   },
   "shop_no": "12345678",
   "sub_biz_id": "sub_biz_id_1",
   "shop_order_id": "SFTC_001",
   "shopid": "122222222",
}
```

返回示例

```json
{
  "resultcode": 0,
  "resultmsg": "ok",
  "fee": 10,
  "deliverfee": 10,
  "couponfee": 0,
  "tips": 0,
  "insurancfee": 0,
  "distance": 1000,
  "dispatch_duration": 300,
  "delivery_token": "1111111"
}
```

### 6.2 HTTPS调用失败返回

请求示例

```json
{
   "cargo": {
       "cargo_first_class": "美食夜宵",
       "cargo_second_class": "零食小吃",
       "goods_detail": {
           "goods": [
               {
                   "good_count": 1,
                   "good_name": "水果",
                   "good_price": 10,
                   "good_unit": "元"
               },
               {
                   "good_count": 2,
                   "good_name": "蔬菜",
                   "good_price": 20,
                   "good_unit": "元"
               }
           ]
       },
       "goods_height": 1,
       "goods_length": 3,
       "goods_value": 5,
       "goods_weight": 1,
       "goods_width": 2
   },
   "delivery_id": "SFTC",
   "delivery_sign": "01234567890123456789",
   "openid": "oABC123456",
   "order_info": {
       "delivery_service_code": "",
       "expected_delivery_time": 0,
       "is_direct_delivery": 0,
       "is_finish_code_needed": 1,
       "is_insured": 0,
       "is_pickup_code_needed": 1,
       "note": "test_note",
       "order_time": 1555220757,
       "order_type": 0,
       "poi_seq": "1111",
       "tips": 0
   },
   "receiver": {
       "address": "xxx地铁站",
       "address_detail": "2号楼202",
       "city": "北京市",
       "coordinate_type": 0,
       "lat": 40.1529600000,
       "lng": 116.5060300000,
       "name": "老王",
       "phone": "18512345678"
   },
   "sender": {
       "address": "xx大厦",
       "address_detail": "1号楼101",
       "city": "北京市",
       "coordinate_type": 0,
       "lat": 40.4486120000,
       "lng": 116.3830750000,
       "name": "刘一",
       "phone": "13712345678"
   },
   "shop": {
       "goods_count": 2,
       "goods_name": "宝贝",
       "img_url": "https://mmbiz.qpic.cn/mmbiz_png/xxxxxxxxx/0?wx_fmt=png",
       "wxa_path": "/page/index/index"
   },
   "shop_no": "12345678",
   "sub_biz_id": "sub_biz_id_1",
   "shop_order_id": "SFTC_001",
   "shopid": "122222222",
}
```

返回示例

```json
{
  "resultcode": 1010,
  "resultmsg": "收件人信息不正确"
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
