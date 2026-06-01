# 品牌申请

> 官方文档：[品牌申请](https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_famousbrandapply.html)
> 所属分类：[小程序交易管理服务](../小程序交易管理服务目录.md)
> 导航路径：小程序交易管理服务 / 品牌申请
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：famousBrandApply

本接口用于小程序品牌申请。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/famousbrand/apply?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：142
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.Application Object Payload

申请品牌信息

### Body.Application.audit_info Object Payload

申请品牌信息，当申请类型为知名品牌时必填

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Body.Application.apply_for Enum

品牌申请类型枚举值

### Body.Application.audit_info.brand_type Enum

品牌类型

## 5. 注意事项

1. `Content-Type` 需要指定为 `application/json`。

## 6. 代码示例

请求示例

```json
{
    "Application": {
        "apply_for": 2,
        "audit_info": {
            "brand_name": "我的小店",
            "brand_type": 4,
            "flagship_in_which_ec_platform": "淘宝",
            "ec_platform_proof_list": [
                "R7oH3VuVWboktgKh3QABx2UqbeNoUDJzLdDjLVvi4kLEOtkCTAGmX9g8-xxxxxx"
            ],
            "other_material_list": [
                "R7oH3VuVWboktgKh3QABx2UqbeNoUDJzLdDjLVvi4kLEOtkCTAGmX9g8-xxxxxx"
            ],
            "authority_certified_proof_list": [
                "R7oH3VuVWboktgKh3QABx2UqbeNoUDJzLdDjLVvi4kLEOtkCTAGmX9g8-xxxxxx"
            ]
        }
    }
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。
