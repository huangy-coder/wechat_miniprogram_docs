# 查询商户号开通状态

> 官方文档：[查询商户号开通状态](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_retailgetmchorder.html)
> 所属分类：[B2b门店助手](../../B2b门店助手目录.md)
> 导航路径：B2b门店助手 / B2b支付 / 查询商户号开通状态
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：retailGetMchOrder

可以通过api方式查询商户号进件订单（包含状态信息等）。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/retail/B2b/retailgetmchorder?access_token=ACCESS_TOKEN
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

### Res.list(Array) Object Payload

订单列表

### Res.list(Array).inner_resp Object Payload

inner_resp

### Res.list(Array).inner_resp.sub_merchant_registration_status Object Payload

申请状态

### Res.list(Array).inner_resp.sub_merchant_registration_status.account_validation Object Payload

汇款账户验证信息。当申请状态为 ACCOUNT_NEED_VERIFY 时有返回。可根据指引汇款，完成账户验证。

### Res.list(Array).inner_resp.sub_merchant_registration_status.audit_detail Object Payload

驳回原因详情。各项资料的审核情况。当申请状态为 REJECTED 或 FROZEN 时才返回。

### Res.list(Array).wqf_register_statement Object Payload

银行转账开通状态，仅开通银行转账（即 open_type = 1）时返回

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
    "out_registration_id": "",
    "page_index": 0,
    "page_size": 0
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "list": [
        {
            "status": 0,
            "inner_resp": {
                "sub_merchant_registration_status": {
                    "applyment_state": "",
                    "applyment_state_desc": "",
                    "sign_state": "",
                    "sign_url": "",
                    "sub_mchid": "",
                    "account_validation": {
                        "account_name": "",
                        "account_no": "",
                        "pay_amount": 0,
                        "destination_account_number": "",
                        "destination_account_name": "",
                        "destination_account_bank": "",
                        "city": "",
                        "remark": "",
                        "deadline": ""
                    },
                    "audit_detail": [
                        {
                            "param_name": "",
                            "reject_reason": ""
                        }
                    ],
                    "legal_validation_url": ""
                }
            },
            "wqf_register_statement": {
                "wqf_register_state": 0,
                "wqf_register_state_desc": "",
                "request_no": ""
            },
            "wx_pay_rate": 0,
            "wqf_certified_rate": 0,
            "bind_scene_status": 0
        }
    ],
    "total": 0
}
```

## 6. 错误码

此接口没有特殊错误码，可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
