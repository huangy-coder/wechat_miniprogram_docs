# 消息跳转路径设置

> 官方文档：[消息跳转路径设置](https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_setmsgjumppath.html)
> 所属分类：[小程序交易管理服务](../小程序交易管理服务目录.md)
> 导航路径：小程序交易管理服务 / 消息跳转路径设置
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：setMsgJumPpath

如你已经在小程序内接入平台提供的确认收货组件，可以通过该接口设置发货消息及确认收货消息的跳转动作，用户点击发货消息时会直接进入你的小程序订单列表页面或详情页面进行确认收货，进一步优化用户体验。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/order/set_msg_jump_path?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：wxa.sec.order.setMsgJumpPath
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1. 如设置为空路径或小程序中不存在的路径，将仍然跳转平台默认的确认收货页面，不会进入你的小程序。
2. 平台会在路径后面增加支付单的 transaction_id、merchant_id、merchant_trade_no 作为query参数，如果存在二级商户号则还会再增加 sub_merchant_id 参数,开发者可以在小程序中通过onLaunch等方式获取。
3. 如你需要在path中携带自定义的query参数，请注意与上面的参数进行区分。

## 5. 代码示例

请求示例

```json
{
    "path": "pages/order/detail"
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
