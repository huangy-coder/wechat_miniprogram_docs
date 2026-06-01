# 仿原生跳转

> 官方文档：[仿原生跳转](https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/basic/api_transportcode_getbusinessview.html)
> 所属分类：[城市服务](../../城市服务目录.md)
> 导航路径：城市服务 / 基础能力 / 仿原生跳转
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：transportcode_getbusinessview

根据需求不同跳转不同的微信仿原生页面实现不同的功能需求。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/intp/transportcode/getbusinessview?access_token=ACCESS_TOKEN
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

## 4. 枚举信息

### Body.path_type Enum

需要跳转的页面

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

请求示例

```json
{
    "path_type": 1
}
```

返回示例

```json
{
    "errcode":0,
    "errmsg":"ok",
    "business_type":"wxCity",
    "query_string":"addr=pages%2Froute%2Fmain&amp;business_view_token=a52f6d30814a8d7d5717d004a0c38894",
    "expire_at":1576838728
}
```

## 7. 错误码

此接口没有特殊错误码，可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
