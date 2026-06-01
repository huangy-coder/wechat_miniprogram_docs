# 激活与更新服务卡片

> 官方文档：[激活与更新服务卡片](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_setusernotify.html)
> 所属分类：[消息相关](../../消息相关目录.md)
> 导航路径：消息相关 / 订阅消息 / 激活与更新服务卡片
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：setUserNotify

激活与更新服务卡片

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/set_user_notify?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

服务卡片详细介绍可参考[文章](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message-2.html)。

## check_json定义

| 参数 | 是否必填 | 类型 | 说明 | 格式要求 |
| --- | --- | --- | --- | --- |
| pay_amount | 是 | uint32 | 订单支付金额。若订单有优惠，支持传入下单金额或实际支付金额。若为合单支付的子订单号，可传入子单的下单金额、子单的实际支付金额、合单的下单金额或合单的实际支付金额。 | 单位为 |
| pay_time | 是 | uint32 | 支付时间 | 秒级时间戳 |
| pay_channel | 否 | uint32 | 订单渠道，0：普通微信支付，1001：支付分 |   |

## 5. 代码示例

### 5.1 通过前端获取code的卡片：激活与更新示例

请求示例

```json
{
  "notify_type": 1001,
  "openid": "xxx",
  "notify_code": "xxx",
  "content_json": "{\"cur_status\":2,\"license_plate\":\"粤A12345A\",\"arrival_time\":1679569348,\"wxa_path_query\":\"\"}"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.2 使用微信支付订单号作为code的卡片：激活示例

请求示例

```json
{
  "notify_type": 2001,
  "openid": "xxx",
  "notify_code": "xxx",
  "check_json": "{\"pay_amount\":1005,\"pay_time\": 1683525070}",
  "content_json": "{\"cur_status\":1,\"product_count\": 1,\"product_list\":{\"info_list\":[{\"product_img\":\"https://res.wx.qq.com/op_res/DiSd8fVjXuHr5K9U73oRr74fMqnT5r9_GmI3mbfLOn2RpC_aENIPjYPPhPN_YnNKnUhyuAy8yLqNRAlh_JCsWQ\",\"product_name\":\"阿白\",\"product_path_query\":\"pages/index/index\"}]},\"wxa_path_query\":\"pages/index/index\"}"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.3 使用微信支付订单号作为code的卡片：更新示例

请求示例

```json
{
  "notify_type": 2001,
  "openid": "xxx",
  "notify_code": "xxx",
  "content_json": "{\"cur_status\":2,\"product_count\": 1,\"product_list\":{\"info_list\":[{\"product_img\":\"https://res.wx.qq.com/op_res/DiSd8fVjXuHr5K9U73oRr74fMqnT5r9_GmI3mbfLOn2RpC_aENIPjYPPhPN_YnNKnUhyuAy8yLqNRAlh_JCsWQ\",\"product_name\":\"阿白\",\"product_path_query\":\"pages/index/index\"}]},\"send_time\": 1696157643,\"wxa_path_query\":\"pages/index/index\"}"
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

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

- ✔：该账号可调用此接口。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
