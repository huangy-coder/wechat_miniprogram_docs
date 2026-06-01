# 开通流程

> 官方文档：[开通流程](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/store_assistant/api_retailbusinessapply.html)
> 所属分类：[B2b门店助手](../../B2b门店助手目录.md)
> 导航路径：B2b门店助手 / 门店认证授权 / 开通流程
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：retailBusinessApply

**方式1：小程序后台开通**

成功申请开通类目（商家自营-B2b(商品批发/门店管理)）的小程序，登录小程序后台（mp.weixin.qq.com），按照“侧边栏-功能-门店助手”的路径，申请开通门店助手功能权限。

**方式2：服务商代开通**

Step1、服务商需通过[三方平台账号](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/operation/authorization/authorization_management.html),获取小程序的门店助手功能[权限集](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/product/miniprogram_authority.html)（权限集ID：158，权限集名称：小程序B2b门店助手）

Step2、服务商获得权限集授权后，可通过使用[authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) 代商家调用。成功开通后，服务商即可代小程序开发所有门店助手相关功能。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/business/retailbusinessapply?access_token=ACCESS_TOKEN
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

1）该接口所属权限集 id 为 158

2）服务商获得权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken) 代商家调用

## 5. 代码示例

请求示例

```json
{
    "goods_type_list": ["食品", "其他"],
    "goods_sale_list": ["杂货店", "便利店", "超市"],
    "cover_num": "0-5千",
    "service_list": ["门店订货"],
    "description": "使用订货功能，线上下单、配送到店；小程序开发者可以通过消息能力，发送新品上线、活动消息等到小店，引导其跳转到小程序内查看活动信息或者订货",
    "contact_name": "张三",
    "contact_phone": "13712345678",
    "contact_email": "zhangsan@qq.com"
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

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
