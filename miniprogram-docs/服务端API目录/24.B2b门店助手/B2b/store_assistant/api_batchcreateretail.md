# 预录入门店信息

> 官方文档：[预录入门店信息](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/store_assistant/api_batchcreateretail.html)
> 所属分类：[B2b门店助手](../../B2b门店助手目录.md)
> 导航路径：B2b门店助手 / 门店认证授权 / 预录入门店信息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：batchcreateretail

通过本API可提前预录入门店信息。

场景说明：对于已提前预录入门店信息的用户，在登录小程序进行门店认证授权流程时，会默认拉起展示预录入的门店信息，用户一键确认即可完成认证授权，减少用户操作成本，提示认证授权成功率。


## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/business/batchcreateretail?access_token=ACCESS_TOKEN
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

### Body.retail_info_list(Array) Object Payload

门店信息列表。每次调用最多可导入 100 个门店

## 3. 返回参数

### 返回体 Response Payload

### Res.failure_record_list(Array) Object Payload

failure_record_list

## 4. 枚举信息

### Res.failure_record_list(Array).failure_code Enum

failure_code

## 5. 注意事项

# 常见QA

1、预录入门店信息后，调取信息完成认证正确方式，以及为什么会出现报错情况？

答：①品牌帮预录入门店信息：假设手机A被品牌预录入门店信息，任何微信号都可以登录手机A+验证码获取门店信息。一旦门店信息被调取，就需要用最初登录手机A调取门店信息的微信号继续完成认证，否则使用其他微信号会报错。

②门店自行预录入门店信息：假设微信号A登录手机B+验证码预录入过门店部分信息后退出插件，后面使用别的微信号登录手机B+验证码调取之前预录入信息继续完成认证是会报错的，需要用最初微信号A登录手机号B＋验证码方可调取。

注：无论是哪种预录入情况，完成门店认证流程并认证成功，任何微信都可以调取同一个手机号+验证码获取已认证门店信息和进行门店信息修改

## 6. 代码示例

请求示例

```json
{
    "retail_info_list": [
        {
            "mobile_phone": "12345678910",
            "retail_name": "张三烧烤店",
            "retail_type": "餐饮店",
            "address_province": "广东省",
            "address_city": "广州市",
            "address_region": "海珠区",
            "address_street": "新港中路397号TIT创意园",
            "longitude": 113.32531,
            "latitude": 23.0996132
        },
        {
            "mobile_phone": "a123456789",
            "retail_type": "便利店",
            "address_province": "广东省",
            "address_city": "广州市",
            "address_region": "海珠区",
            "address_street": "新港中路397号TIT创意园",
            "registration_number": "xxxxx",
            "biz_name": "xxxxx",
            "corporation_name": "xxxxx"
        }
    ]
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "num_success": 1,
    "num_failure": 1,
    "failure_record_list": [
        {
            "mobile_phone": "a123456789",
            "registration_number": "",
            "failure_code": 6
        }
    ]
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
