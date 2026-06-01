# 商户号进件

> 官方文档：[商户号进件](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_retailregistermch.html)
> 所属分类：[B2b门店助手](../../B2b门店助手目录.md)
> 导航路径：B2b门店助手 / B2b支付 / 商户号进件
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：retailRegisterMch

可以通过 api 方式进行商户号的进件。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/retail/B2b/retailregistermch?access_token=ACCESS_TOKEN
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

### Body.id_card_info Object Payload

经营者/法人身份证信息。当id_doc_type_num为0和1时必填

### Body.id_doc_info Object Payload

经营者/法人其他类型证件信息。当id_doc_type_num不为0和1时必填

### Body.account_info Object Payload

结算银行账户

### Body.contact_info Object Payload

超级管理员信息

### Body.business_license Object Payload

营业执照

### Body.qualification Object Payload

行业特殊资质资料。

### Body.ext_register_info Object Payload

补充信息

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Body.ext_register_info.merchant_scale Enum

企业规模，枚举值

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

请求示例

```json
{
  "id_doc_type_num": 1,
  "id_card_info": {
    "id_card_copy": "V1_xxxxxxx",
    "id_card_national": "V1_xxxxxx",
    "id_card_name": "小明",
    "id_card_number": "440000199001011111",
    "id_card_valid_time": "2041-01-01",
    "id_card_address": "北京市朝阳区等等等",
    "id_card_valid_time_begin": "2021-01-01"
  },
  "account_info": {
    "bank_account_type": "74",
    "account_bank": "招商银行",
    "bank_name": "招商银行xx支行",
    "account_name": "北京食品有限公司",
    "bank_address_code": "123",
    "account_number": "123"
  },
  "contact_info": {
    "contact_type": "65",
    "contact_name": "小明",
    "contact_id_card_number": "440000199001011111",
    "mobile_phone": "12345678911",
    "contact_email": "test@qq.com"
  },
  "business_license": {
    "business_license_copy": "V1_xxxx",
    "business_license_number": "ABC123",
    "merchant_name": "北京食品有限公司",
    "legal_person": "小明"
  },
  "merchant_shortname": "北京食品",
  "organization_type": 1,
  "ignore_same_entity": true,
  "launch_poll_task": true,
  "qualification": {
    "qualification_type": "食品生鲜"
  },
  "open_type": 1,
  "ext_register_info": {
    "door_head_file_id": "V1_xxxxxxx",
    "store_file_id": "V1_xxxxxxx",
    "online_pay_file_id": "V1_xxxxxxx",
    "merchant_scale": "LARGE"
  },
  "client_ip": "127.0.0.0"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "OK",
  "order_no": "regorder123"
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
