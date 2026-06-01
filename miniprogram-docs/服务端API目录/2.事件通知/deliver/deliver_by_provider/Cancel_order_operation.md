# immediateDelivery.onOrderCancel

> 官方文档：[immediateDelivery.onOrderCancel](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/deliver/deliver_by_provider/Cancel_order_operation.html)
> 所属分类：[事件通知](../../事件通知目录.md)
> 导航路径：事件通知 / 即时配送 / 运力方使用 / 取消订单操作
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 本文档描述服务器端接收的消息或事件，详细说明参见[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)。

取消订单操作，取消逻辑参照各配送公司取消规则）

### 消息参数

### Object

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ToUserName | string | 快递公司小程序 UserName |
| FromUserName | string | 微信团队的 OpenID （固定值） |
| CreateTime | number | 事件时间，Unix时间戳 |
| MsgType | string | 消息类型，固定为 event |
| Event | string | 事件类型，固定为 transport_cancel_order，不区分大小写 |
| shopid | string | 商家id， 由配送公司分配，可以是dev_id或者appkey |
| shop_order_id | string | 唯一标识订单的 ID，由商户生成 |
| shop_no | string | 商家门店编号， 在配送公司侧登记 |
| waybill_id | string | 配送单id |
| delivery_sign | string | 用配送公司侧提供的appSecret加密的校验串 |
| cancel_reason_id | number | 取消原因id |
| cancel_reason | string | 取消原因 |

**cancel_reason_id 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | 暂时不需要邮寄 |   |
| 2 | 价格不合适 |   |
| 3 | 订单信息有误，重新下单 |   |
| 4 | 骑手取货不及时 |   |
| 5 | 骑手配送不及时 |   |
| 6 | 其他原因( 如果选择6，需要填写取消原因，否则不需要填写 ) |   |

### 消息返回

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ToUserName | string |   | 是 | 原样返回请求中的 FromUserName |
| FromUserName | string |   | 是 | 快递公司小程序 UserName |
| CreateTime | number |   | 是 | 事件时间，Unix时间戳 |
| MsgType | string |   | 是 | 消息类型，固定为 event |
| Event | string |   | 是 | 事件类型，固定为 transport_cancel_order，不区分大小写 |
| resultcode | number |   | 是 | 错误码 |
| resultmsg | string |   | 是 | 错误描述 |
| deduct_fee | number |   | 是 | 扣除的违约金(单位：元)，可能没有 |
| desc | string |   | 是 | 扣费说明 |

```text

```
