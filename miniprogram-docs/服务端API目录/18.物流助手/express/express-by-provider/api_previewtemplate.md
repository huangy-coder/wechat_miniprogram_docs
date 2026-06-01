# 预览面单模板

> 官方文档：[预览面单模板](https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-provider/api_previewtemplate.html)
> 所属分类：[物流助手](../../物流助手目录.md)
> 导航路径：物流助手 / 运力方使用 / 预览面单模板
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：previewTemplate

该接口用于预览面单模板。以及用于调试面单模板使用。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/delivery/template/preview?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：logistics.previewTemplate
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.custom Object Payload

商户下单数据，格式是商户侧下单[addOrder](https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_addorder) 接口中的请求体

### Body.custom.sender Object Payload

发件人信息

### Body.custom.receiver Object Payload

收件人信息

### Body.custom.cargo Object Payload

包裹信息，将传递给快递公司

### Body.custom.cargo.detail_list(Array) Object Payload

货物总重量，单位是千克(kg)

### Body.custom.shop Object Payload

商品信息，会展示到物流服务通知和电子面单中

### Body.custom.insured Object Payload

保价信息

### Body.custom.service Object Payload

服务类型

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

#### 模板渲染语法

1. 所有渲染语法由`##`开始，可参考[示例](https://res.wx.qq.com/wxdoc/dist/assets/media/template_demo.f1eb7e63.zip)。
2. `##VAR(key)` 用参数key对应的值填充。支持的参数如下表格所示

| key | value |
| --- | --- |
| sys.waybillid | 运单 ID |
| sys.wxaappid | 商户小程序 APPID |
| waybilldata.* | [下单事件](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/Request_an_order_event)返回中的WaybillData，快递侧自定义的数据 |
| custom.* | 是[商户侧下单](https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_addorder) API 中传入的字段 |
| custom.order_id | 唯一标识订单的 ID，由商户传入 |
| custom.custom_remark | 快递备注，会打印到面单的自定义区，比如"易碎物品" |
| custom.sender.name | 发件人名字 |
| custom.sender.tel | 发件人座机号码 |
| custom.sender.mobile | 发件人手机号码 |
| custom.sender.company | 发件人公司名 |
| custom.sender.post_code | 发件人邮编 |
| custom.sender.country | 发件人所在国家 |
| custom.sender.province | 发件人省份 |
| custom.sender.city | 发件人地区/市 |
| custom.sender.area | 发件人区/县 |
| custom.sender.address | 发件人详细地址 |
| custom.receiver.name | 收件人名字 |
| custom.receiver.tel | 收件人座机号码 |
| custom.receiver.mobile | 收件人手机号码 |
| custom.receiver.company | 收件人公司名 |
| custom.receiver.post_code | 收件人邮编 |
| custom.receiver.country | 收件人所在国家 |
| custom.receiver.province | 收件人省份 |
| custom.receiver.city | 收件人地区/市 |
| custom.receiver.area | 收件人区/县 |
| custom.receiver.address | 收件人详细地址 |
| custom.cargo.count | 包裹数量 |
| custom.cargo.weight | 包裹总重量，单位是千克(kg) |
| custom.cargo.space_x | 包裹长度，单位是厘米(cm) |
| custom.cargo.space_y | 包裹宽度，单位是厘米(cm) |
| custom.cargo.space_z | 包裹高度，单位是厘米(cm) |
| custom.shop.goods_name | 商品名称 |
| custom.shop.goods_count | 商品数量 |
| custom.insured.use_insured | 是否使用保价 |
| custom.insured.insured_value | 报价金额，单位是分 |
| custom.service.service_type | 服务类型 ID |
| custom.service.service_name | 服务名称 |

1. `##TIME(DATE)` 用日期填充当前位置，格式为`%Y/%m/%d`，比如`2018/11/22`。
2. `##TIME(TIME)` 用时间填充当前位置，格式为`%H:%M:%S`，比如`17:54:06`。
3. `##TIME(FULL)` 用日期时间填充当前位置，格式为`%Y/%m/%d %H:%M:%S`，比如`2018/11/22 17:54:06`。
4. `##STRBLOAT(VAR(sys.waybillid))` 获取运单 ID，然后在每个字符间填充空格。
5. `##CODE128(VAR(sys.waybillid))` 获取运单 ID，然后转换成CODE128条码，图片为base64编码。
6. `##QRCODE(VAR(sys.waybillid))` 获取运单 ID，然后转换为二维码，图片为base64编码。
7. `##WXASUNCODE(VAR(sys.wxaappid))` 获取商户的小程序码，图片为base64编码。

举例，如果想在面单上打印一个集包地信息的条形码，可以在面单中增加：

```html
<img src="data:image/jpeg;base64, ##CODE128(VAR(waybilldata.ZTO_bagAddr))" class="block_5__barCode">
```

## 5. 代码示例

### 5.1 HTTPS调用

请求示例

```json
{
  "waybill_id": "1234567890123",
  "waybill_data": "##ZTO_mark##11-22-33##ZTO_bagAddr##广州##",
  "waybill_template": "PGh0bWw+dGVzdDwvaHRtbD4=",
  "custom": {
    "order_id": "012345678901234567890123456789",
    "openid": "oABC123456",
    "delivery_id": "ZTO",
    "biz_id": "xyz",
    "custom_remark": "易碎物品",
    "sender": {
      "name": "张三",
      "tel": "18666666666",
      "mobile": "020-88888888",
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
      "tel": "18610000000",
      "mobile": "020-77777777",
      "company": "公司名",
      "post_code": "654321",
      "country": "中国",
      "province": "广东省",
      "city": "广州市",
      "area": "天河区",
      "address": "XX路XX号XX大厦XX栋XX"
    },
    "shop": {
      "wxa_path": "/index/index?from=waybill",
      "img_url": "https://mmbiz.qpic.cn/mmbiz_png/KfrZwACMrmwbPGicysN6kibW0ibXwzmA3mtTwgSsdw4Uicabduu2pfbfwdKicQ8n0v91kRAUX6SDESQypl5tlRwHUPA/640",
      "goods_name": "一千零一夜钻石包&爱马仕柏金钻石包",
      "goods_count": 2
    },
    "cargo": {
      "count": 2,
      "weight": 5.5,
      "space_x": 30.5,
      "space_y": 20,
      "space_z": 20,
      "detail_list": [
        {
          "name": "一千零一夜钻石包",
          "count": 1
        },
        {
          "name": "爱马仕柏金钻石包",
          "count": 1
        }
      ]
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
}
```

返回示例

```json
{
  "waybill_id": "1234567890123",
  "rendered_waybill_template": "PGh0bWw+dGVzdDwvaHRtbD4="
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
    const result = await cloud.openapi.logistics.previewTemplate({
        "custom": {
          "openid": 'oABC123456',
          "sender": {
            "name": '张三',
            "tel": '18666666666',
            "mobile": '020-88888888',
            "company": '公司名',
            "country": '中国',
            "province": '广东省',
            "city": '广州市',
            "area": '海珠区',
            "address": 'XX路XX号XX大厦XX栋XX',
            "postCode": '123456'
          },
          "receiver": {
            "name": '王小蒙',
            "tel": '18610000000',
            "mobile": '020-77777777',
            "company": '公司名',
            "country": '中国',
            "province": '广东省',
            "city": '广州市',
            "area": '天河区',
            "address": 'XX路XX号XX大厦XX栋XX',
            "postCode": '654321'
          },
          "shop": {
            "wxaPath": '/index/index?from=waybill',
            "imgUrl": 'https://mmbiz.qpic.cn/mmbiz_png/KfrZwACMrmwbPGicysN6kibW0ibXwzmA3mtTwgSsdw4Uicabduu2pfbfwdKicQ8n0v91kRAUX6SDESQypl5tlRwHUPA/640',
            "goodsName": '一千零一夜钻石包&爱马仕柏金钻石包',
            "goodsCount": 2
          },
          "cargo": {
            "count": 2,
            "weight": 5.5,
            "spaceX": 30.5,
            "spaceY": 20,
            "spaceZ": 20,
            "detailList": [
              {
                "name": '一千零一夜钻石包',
                "count": 1
              },
              {
                "name": '爱马仕柏金钻石包',
                "count": 1
              }
            ]
          },
          "insured": {
            "useInsured": 1,
            "insuredValue": 10000
          },
          "service": {
            "serviceType": 0,
            "serviceName": '标准快递'
          },
          "orderId": '012345678901234567890123456789',
          "deliveryId": 'ZTO',
          "bizId": 'xyz',
          "customRemark": '易碎物品'
        },
        "waybillId": '1234567890123',
        "waybillData": '##ZTO_mark##11-22-33##ZTO_bagAddr##广州##',
        "waybillTemplate": 'PGh0bWw+dGVzdDwvaHRtbD4='
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
  "waybill_id": "1234567890123",
  "rendered_waybill_template": "PGh0bWw+dGVzdDwvaHRtbD4="
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
