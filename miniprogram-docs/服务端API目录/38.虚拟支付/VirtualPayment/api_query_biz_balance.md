# 查询商家账户可提现余额

> 官方文档：[查询商家账户可提现余额](https://developers.weixin.qq.com/miniprogram/dev/server/API/VirtualPayment/api_query_biz_balance.html)
> 所属分类：[虚拟支付](../虚拟支付目录.md)
> 导航路径：虚拟支付 / 查询商家账户可提现余额
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：query_biz_balance

查询商家账户里的可提现余额

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/xpay/query_biz_balance?access_token=ACCESS_TOKEN&pay_sig=PAY_SIG
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：157
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.balance_available Object Payload

可提现余额

## 4. 注意事项

使用支付签名

#### 支付签名

签名参数为 `pay_sig`，加在 `query` 后面

例如接口地址是：`https://api.weixin.qq.com/xpay/query_user_balance?access_token=xxxx`

加上签名后则需要传 `https://api.weixin.qq.com/xpay/query_user_balance?access_token=xxxx&pay_sig=xxx`

## 5. 代码示例

本接口无代码示例

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
