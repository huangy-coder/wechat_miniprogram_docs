# 添加小费

> 官方文档：[添加小费](https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_addtips.html)
> 所属分类：[即时配送](../../即时配送目录.md)
> 导航路径：即时配送 / 小程序使用 / 添加小费
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：addTips

该接口可以对待接单状态的订单增加小费。需要注意：订单的小费，以最新一次加小费动作的金额为准，故下一次增加小费额必须大于上一次小费额。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/local/business/order/addtips?access_token=ACCESS_TOKEN
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

#### 使用场景

调用本接口，可以给待接单状态的订单增加小费，各家配送公司增加消费的规则如下：

| 配送公司 | 加小费规则 |
| --- | --- |
| 顺丰同城急送 | 支持加小费，小费规则：骑手接单前可加小费，上限10次，200元封顶 |
| 闪送 | 支持加小费，小费规则：骑手接单前可加小费，需按固定档位加小费，档位为2、3、5、10、15、20、50、100 |
| 美团配送 | 不支持加小费 |
| 达达配送 | 支持加小费，小费规则：骑手接单前可加小费，小费金额以最新一次为准，同一单新增的小费额须大于上一次的小费额，小费不可以超过货值，上限30元 |

## 5. 代码示例

请求示例

```json
{
  "shopid": "123456",
  "shop_order_id": "123456",
  "waybill_id": "123456",
  "tips": 5,
  "remark": "gogogo",
  "delivery_sign": "123456",
  "shop_no": "shop_no_111"
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
