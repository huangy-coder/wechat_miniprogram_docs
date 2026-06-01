# 取消配送单

> 官方文档：[取消配送单](https://developers.weixin.qq.com/miniprogram/dev/server/API/immediate-delivery/deliver-by-business/api_cancellocalorder.html)
> 所属分类：[即时配送](../../即时配送目录.md)
> 导航路径：即时配送 / 小程序使用 / 取消配送单
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：cancelLocalOrder

该接口用于取消配送单。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/local/business/order/cancel?access_token=ACCESS_TOKEN
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

调用本接口可向配送公司请求取消配送单，各家取消规则如下：

- 顺丰同城急送：配送完成前任意节点可取消配送单
- 闪送：配送完成前任意节点可取消配送单
- 美团配送：配送完成前任意节点可取消配送单
- 达达：骑手取货之前可取消配送单

## 其他说明

### cancel_reason_id 取消原因Id的合法值

| 值 | 说明 |
| --- | --- |
| 1 | 暂时不需要邮寄 |
| 2 | 价格不合适 |
| 3 | 订单信息有误，重新下单 |
| 4 | 骑手取货不及时 |
| 5 | 骑手配送不及时 |
| 6 | 其他原因( 如果选择6，需要填写取消原因，否则不需要填写 ) |

#### 商家接入准备

1. 小程序进行微信认证
2. 开通事件推送，设置事件地址：登录[小程序后台](https://mp.weixin.qq.com)，开发->开发设置->消息推送->启用
3. 消息加密方式使用安全模式，数据格式选JSON
4. 如果授权给第三方，则不需要步骤2
5. 在配送公司注册账号，并在小程序后台进行授权绑定

#### 名称解释

1. appkey: 一般为商家在登录配送公司开放平后分配的相应的appkey值
2. AppSecret: 一般为商家在登录配送公司开放平后分配的相应的秘钥
3. shopid：微信平台字段，对应配送公司的appkey
4. shop_no：商家对不同门店进行的编号，需要在配送公司系统有过登记，比如商家自己门店系统中有100个门店，编号是1-100，在顺丰同城的系统中有登记过这100个门店，且在顺丰同城登记的编号也是1-100，那么下单的时候传shop_no=1，就是编号为1 的门店下的配送单
5. shop：下单请求的一个字段，商家信息，会展示到物流通知消息中，如下图所示
6. 下单请求的取货码和收货码：取货码是指骑手在商家这里取货时，商家出示取货码，骑手才能完成取货；收货码指骑手送达给用户时，用户出示收货码，骑手才算配送完成。商家可在配送公司开放平台设置是否需要开启取货码和收货码

#### 调用api接口说明

1. 编码方式：UTF-8
2. 数据格式：JSON
3. 提交方式：POST
4. 下单需要使用绑定的shopid和AppSecret，其中shopid即配送公司账号的appkey，AppSecret即配送公司账号对应的秘钥
5. resultcode错误码和resultmsg错误描述由运力方定义，微信侧负责透传，只统一定义code=0表示成功
6. 除了平台本身的加解密和签名，和订单相关的请求还需要带上运力侧签名delivery_sign，签名规则为
7. 如果接口请求里有字段shop_order_id ，则delivery_sign=SHA1(shopid + shop_order_id + AppSecret)，其中shopid对应运力侧的appkey，shop_order_id对应订单id，AppSecret即配送公司账号对应的秘钥
8. 如果请求里没有字段shop_order_id ，则delivery_sign=SHA1(shopid + AppSecret)，其中shopid对应运力侧的appkey，AppSecret即配送公司账号对应的秘钥
9. 示例：shopid=“test_shop_id”，shop_order_id =“test_shop_order_id”， AppSecret=“test_app_secrect”，则delivery_sign=“a93d8d6bae9a9483c1b1d4e8670e7f6226ec94cb”

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
