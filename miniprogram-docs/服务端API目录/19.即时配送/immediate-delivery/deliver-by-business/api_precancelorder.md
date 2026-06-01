# 预取消配送单

> 官方文档：[预取消配送单](https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_precancelorder.html)
> 所属分类：[即时配送](../../即时配送目录.md)
> 导航路径：即时配送 / 小程序使用 / 预取消配送单
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：preCancelOrder

#### 使用场景描述

- 在正式取消配送单前，商家可调用本接口查询该订单是否可以取消，取消订单配送公司需要扣除的费用是多少。各家取消规则如下：
- 顺丰同城急送：配送完成前任意节点可取消配送单
- 闪送：配送完成前任意节点可取消配送单
- 美团配送：配送完成前任意节点可取消配送单
- 达达：骑手取货之前可取消配送单

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/local/business/order/precancel?access_token=ACCESS_TOKEN
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

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
  "shopid": "123456",
  "shop_order_id": "123456",
  "waybill_id": "123456",
  "delivery_id": "123456",
  "cancel_reason_id": 1,
  "cancel_reason": "",
  "delivery_sign": "123456",
  "shop_no": "shop_no_111"
}
```

返回示例

```json
{
  "resultcode": 0,
  "resultmsg": "ok",
  "deduct_fee": 5,
  "desc": "blabla"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
