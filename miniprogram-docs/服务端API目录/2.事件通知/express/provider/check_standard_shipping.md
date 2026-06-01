# 通过收发件地址查询标准运费

> 官方文档：[通过收发件地址查询标准运费](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/express/provider/check_standard_shipping.html)
> 所属分类：[事件通知](../../事件通知目录.md)
> 导航路径：事件通知 / 物流助手 / 运力方使用 / 通过收发件地址查询标准运费
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 本文档描述服务器端接收的消息或事件，详细说明参见[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)。

事件英文名：query_single_waybill_fee

用户在下单页面选择收发货地址时进行查询

## 1. 消息参数

### 请求体 Request Payload

### Body.Sender Object Payload

发件人信息

### Body.Receiver Object Payload

收件人信息

### Body.GoodDetail Object Payload

物品详情

## 2. 消息返回

### 返回体 Response Payload

## 3. 枚举信息

### Body.GoodDetail.Special Enum

物品类型，见物品类型说明

## 4. 注意事项

本事件无特殊注意事项

## 5. 代码示例

本事件无代码示例
