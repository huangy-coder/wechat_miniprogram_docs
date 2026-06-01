# 查询小程序是否已完成交易结算管理确认

> 官方文档：[查询小程序是否已完成交易结算管理确认](https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_istrademanagementconfirmationcompleted.html)
> 所属分类：[小程序交易管理服务](../小程序交易管理服务目录.md)
> 导航路径：小程序交易管理服务 / 查询小程序是否已完成交易结算管理确认
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：isTradeManagementConfirmationCompleted

调用该接口可查询小程序账号是否已完成交易结算管理确认（即对小程序已关联的所有商户号都完成了订单管理授权或解绑）。已完成订单管理授权的商户号，产生的订单均需要通过发货信息管理服务进行发货

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/order/is_trade_management_confirmation_completed?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18、142
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

服务商被授权了 18 或 142 权限集时才能进行查询。

## 5. 代码示例

请求示例

```json
{
    "appid": "wx0123456789abcdef"
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "completed": true
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
