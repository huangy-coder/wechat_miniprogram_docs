# 门店运费退款

> 官方文档：[门店运费退款](https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_store_refund.html)
> 所属分类：[微信物流服务](../../微信物流服务目录.md)
> 导航路径：微信物流服务 / 同城配送 / 门店运费退款
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：intracity_store_refund

该接口可以将门店指定运力的运费余额退还，如果门店有在途的配送订单，需要等配送完成或者取消配送订单之后才可以操作退款；操作退款后，退款金额五分钟内到账。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/intracity/storerefund?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：51
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Body.pay_mode Enum

充值/扣费主体，不传pay_mode默认pay_mode=PAY_MODE_STORE

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

请求示例

```json
{
    "wx_store_id":"4000000000000042001",
    "service_trans_id":"SFTC"
}
```

返回示例

```json
{
    "appid":"wx539e0b4872f196d1",
    "wx_store_id":"4000000000000042001"，
    "refund_amount":3000
}
```

## 7. 错误码

此接口没有特殊错误码，可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
