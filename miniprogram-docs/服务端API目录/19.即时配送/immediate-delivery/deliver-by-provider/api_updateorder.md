# 更新配送单状态

> 官方文档：[更新配送单状态](https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-provider/api_updateorder.html)
> 所属分类：[即时配送](../../即时配送目录.md)
> 导航路径：即时配送 / 运力方使用 / 更新配送单状态
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：updateOrder

该接口用于配送公司更新配送单状态。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/local/delivery/update_order?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.agent Object Payload

骑手信息, 骑手接单时需返回

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Body.order_status Enum

订单状态

## 5. 注意事项

#### 关于 order_status 枚举值说明

1. 最终状态包括成功状态302，失败状态: 103,203,204,205,401,501,502。
2. 当状态更新时，我们会在关键节点给收件用户推送服务通知，告知配送状态，同一配送单常态下会收到三条通知，即【骑手已接单】、【骑手已取货，配送中】、【配送已完成】，配送异常时会下发【配送异常】服务通知。

#### 不同服务通知对应的 order_status 枚举值为

| 服务通知 | 对应的order_status值 |
| --- | --- |
| 骑手已接单 | 102 |
| 骑手已取货，配送中 | 202或301 |
| 配送已完成 | 302 |
| 配送异常 | 203、204、205、303、304、305、501、502 |

## 6. 代码示例

请求示例

```json
{
  "wx_token": "",
  "shopid": 0,
  "shop_order_id": "C1638702836167U4v252",
  "shop_no": "6261889268017",
  "waybill_id": "3436608931550646273",
  "action_time": 1638703215,
  "order_status": 202,
  "action_msg": "",
  "agent": {
    "name": "李x利",
    "phone": "1358xxxx",
    "lng": 112.224839,
    "lat": 22.690728
  },
  "wxa_path": "pages/index/index",
  "expected_delivery_time": 1638705236
}
```

返回示例

```json
{
  "resultcode": 0,
  "resultmsg": "ok"
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
