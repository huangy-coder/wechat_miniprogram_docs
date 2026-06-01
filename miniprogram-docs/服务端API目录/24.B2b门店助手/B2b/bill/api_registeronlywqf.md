# 申请开通银行转账

> 官方文档：[申请开通银行转账](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_registeronlywqf.html)
> 所属分类：[B2b门店助手](../../B2b门店助手目录.md)
> 导航路径：B2b门店助手 / B2b支付 / 申请开通银行转账
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：registerOnlyWqf

在微信支付开通成功、但未开通银行转账的情况下，商户可以申请开通银行转账支付方式。

**页面端方式：**

登录 [mp后台](https://mp.weixin.qq.com/)，进入小程序后台页面，在 "B2b门店助手-支付管理" 栏目，点击 "去开通" 申请开通银行转账。


**接口端方式：**

可以通过此 api 方式进行银行转账的开通申请。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/retail/B2b/registeronlywqf?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：158
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

## 查询银行转账开通情况

银行转账开通状态查询 API 同[商户号开通状态查询](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_retailgetmchorder)，这里重点关注请求响应中的 wqf_register_statement 字段。

### wqf_register_statement

| 返回参数 | 参数名 | 类型 | 必填 | 描述 | 枚举值 |
| --- | --- | --- | --- | --- | --- |
| 银行转账开通状态 | wqf_register_state | uint32 | 是 | 银行转账开通状态 | 0: 未开通；1: 开通中；2: 开通成功；3: 开通失败，可尝试重新申请开通银行转账；4: 申请驳回，商户需跳转银行转账页面，完善信息后重新提交；5: 申请开通中（已开通微信支付，申请开通银行转账的场景）；6: 申请开通失败（已开通微信支付，申请开通银行转账的场景） |
| 银行转账开通状态描述 | wqf_register_state_desc | string | 是 | 银行转账开通状态描述 | 示例值: "待完善信息" |
| 银行转账开通单号 | request_no | string | 否 | 银行转账开通单号，仅当银行转账进入开通状态（开通中、开通成功、开通失败、申请驳回）时返回，可用于获取跳转链接 | 示例值: "MSE123" |

以下为各状态详细说明：

1. 成功调用申请开通银行转账接口后，状态扭转为“申请开通中”，对应枚举值 5。
2. 若申请开通失败，状态扭转为“申请开通失败”，对应枚举值 6。可尝试重新调用银行转账开通接口进行申请。
3. 若申请开通成功，将正式进入银行转账开通流程，wqf_register_statement 里会携带银行转账开通单号 request_no。此时有四种可能状态： 1）开通中 - 1，详细情况将在 wqf_register_state_desc 里返回： 2）开通成功 - 2。 3）开通失败 - 3，可尝试重新调用银行转账开通接口进行申请。 4）申请驳回 - 4，商户需[跳转银行转账页面](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_createwqflink)，修改资料后重新提交。
  1. 待完善信息：商户需[跳转银行转账页面](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_createwqflink)，完善信息后重新提交。
  2. 待用户签约：商户需[跳转银行转账页面](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_createwqflink)，完成银行转账签约。
  3. 资料校验中：无需操作。
  4. 系统审核中：无需操作。

## 5. 代码示例

请求示例

```json
{
    "out_registration_id": "regorder000"
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

此接口没有特殊错误码，可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
