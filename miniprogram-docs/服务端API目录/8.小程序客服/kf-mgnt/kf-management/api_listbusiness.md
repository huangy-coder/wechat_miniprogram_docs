# 客服子商户拉取多个商户信息

> 官方文档：[客服子商户拉取多个商户信息](https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-management/api_listbusiness.html)
> 所属分类：[小程序客服](../../小程序客服目录.md)
> 导航路径：小程序客服 / 客服子商户 / 客服子商户拉取多个商户信息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：listbusiness

本接口用于拉取多个「客服子商户」的信息。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/business/list?access_token=ACCESS_TOKEN
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

### Res.list(Array) Object Payload

商户信息列表

## 4. 注意事项

某一次请求的返回的数据量小于count数，说明请求的数据已经到了末端

## 5. 代码示例

请求示例

```json
{
    "offset": 0,
    "count": 100
}
```

返回示例

```json
{
    "list": [
        {
            "business_id": 1,
            "account_name": "apple",
            "nickname":"苹果",
            "icon_url":"icon_url"
        },
        {
            "business_id": 2,
            "account_name": "apple",
            "nickname":"苹果",
            "icon_url":"icon_url"
        }
    ]
}
```

## 6. 错误码

此接口没有特殊错误码，可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
