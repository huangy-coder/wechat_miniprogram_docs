# 客服子商户创建商户

> 官方文档：[客服子商户创建商户](https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-management/api_registerbusiness.html)
> 所属分类：[小程序客服](../../小程序客服目录.md)
> 导航路径：小程序客服 / 客服子商户 / 客服子商户创建商户
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：registerbusiness

一个小程序账号可为平台内的商户创建多个子商户账号，创建后在小程序客服组件唤起子商户单独的会话。

多个子商户会话独立，可为用户提供更优质的客服体验。

只对【电商平台】类目小程序开放，详情查看[介绍文档](https://developers.weixin.qq.com/miniprogram/introduction/custom)

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/business/register?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
    "account_name": "apple",
    "nickname": "苹果",
    "icon_media_id":"media_id"
    "transfer_to_commkf": true
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "",
    "business_id": 1
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
