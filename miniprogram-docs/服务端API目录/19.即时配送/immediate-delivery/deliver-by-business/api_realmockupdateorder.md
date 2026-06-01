# 模拟更新配送单状态

> 官方文档：[模拟更新配送单状态](https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_realmockupdateorder.html)
> 所属分类：[即时配送](../../即时配送目录.md)
> 导航路径：即时配送 / 小程序使用 / 模拟更新配送单状态
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：realMockUpdateOrder

该接口用于模拟配送公司更新配送单状态，可进行测试账户下的单，将请求转发到运力测试环境。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/local/business/realmock_update_order?access_token=ACCESS_TOKEN
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

- 该接口只能用于测试,请求会转发到运力测试环境, 目前支持顺丰同城和达达。

1、顺丰同城测试号

- shopid: 1534713176
- appsecret: d80400f91e156f63b38886e616d84590
- shopno: 3243279847393
- 支持变更状态: 102 202 202 302

2、达达测试号

- shopid: dadaaee18818d97e236
- appsecret: 1c6f40492d6d89caaad80b85f7d31670
- shopno: 77071-47913
- 支持变更状态: 102 201 202 301 302 304 305

## 5. 代码示例

请求示例

```json
{
   "shopid": "xxxxxxx",
   "shop_order_id": "xxxxxxxxxxx",
   "action_time": 1584145981,
   "order_status": 101,
   "action_msg": "",
   "delivery_sign": "xxxxxxx",
}
```

返回示例

```json
{
  "resultcode": 0,
  "resultmsg": "ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
