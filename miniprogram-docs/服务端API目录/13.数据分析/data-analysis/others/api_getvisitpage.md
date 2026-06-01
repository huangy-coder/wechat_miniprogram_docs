# 获取访问页面数据

> 官方文档：[获取访问页面数据](https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/others/api_getvisitpage.html)
> 所属分类：[数据分析](../../数据分析目录.md)
> 导航路径：数据分析 / 其他 / 获取访问页面数据
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getVisitPage

该接口用于访问页面。目前只提供按 page_visit_pv 排序的 top200。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/datacube/getweanalysisappidvisitpage?access_token=ACCESS_TOKEN
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 调用方法：analysis.getVisitPage
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.list(Array) Object Payload

数据列表

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

### 5.1 HTTPS调用

请求示例

```json
{
  "begin_date": "20170313",
  "end_date": "20170313"
}
```

返回示例

```json
{
  "ref_date": "20170313",
  "list": [
    {
      "page_path": "pages/main/main.html",
      "page_visit_pv": 213429,
      "page_visit_uv": 55423,
      "page_staytime_pv": 8.139198,
      "entrypage_pv": 117922,
      "exitpage_pv": 61304,
      "page_share_pv": 180,
      "page_share_uv": 166
    },
    {
      "page_path": "pages/linedetail/linedetail.html",
      "page_visit_pv": 155030,
      "page_visit_uv": 42195,
      "page_staytime_pv": 35.462395,
      "entrypage_pv": 21101,
      "exitpage_pv": 47051,
      "page_share_pv": 47,
      "page_share_uv": 42
    },
    {
      "page_path": "pages/search/search.html",
      "page_visit_pv": 65011,
      "page_visit_uv": 24716,
      "page_staytime_pv": 6.889634,
      "entrypage_pv": 1811,
      "exitpage_pv": 3198,
      "page_share_pv": 0,
      "page_share_uv": 0
    },
    {
      "page_path": "pages/stationdetail/stationdetail.html",
      "page_visit_pv": 29953,
      "page_visit_uv": 9695,
      "page_staytime_pv": 7.558508,
      "entrypage_pv": 1386,
      "exitpage_pv": 2285,
      "page_share_pv": 0,
      "page_share_uv": 0
    },
    {
      "page_path": "pages/switch-city/switch-city.html",
      "page_visit_pv": 8928,
      "page_visit_uv": 4017,
      "page_staytime_pv": 9.22659,
      "entrypage_pv": 748,
      "exitpage_pv": 1613,
      "page_share_pv": 0,
      "page_share_uv": 0
    }
  ]
}
```

### 5.2 云函数调用

请求示例

```json
const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
})
exports.main = async (event, context) => {
  try {
    const result = await cloud.openapi.analysis.getVisitPage({
        "beginDate": '20170313',
        "endDate": '20170313'
      })
    return result
  } catch (err) {
    return err
  }
}
```

返回示例

```json
{
  "refDate": "20170313",
  "list": [
    {
      "pagePath": "pages/main/main.html",
      "pageVisitPv": 213429,
      "pageVisitUv": 55423,
      "pageStaytimePv": 8.139198,
      "entrypagePv": 117922,
      "exitpagePv": 61304,
      "pageSharePv": 180,
      "pageShareUv": 166
    },
    {
      "pagePath": "pages/linedetail/linedetail.html",
      "pageVisitPv": 155030,
      "pageVisitUv": 42195,
      "pageStaytimePv": 35.462395,
      "entrypagePv": 21101,
      "exitpagePv": 47051,
      "pageSharePv": 47,
      "pageShareUv": 42
    },
    {
      "pagePath": "pages/search/search.html",
      "pageVisitPv": 65011,
      "pageVisitUv": 24716,
      "pageStaytimePv": 6.889634,
      "entrypagePv": 1811,
      "exitpagePv": 3198,
      "pageSharePv": 0,
      "pageShareUv": 0
    },
    {
      "pagePath": "pages/stationdetail/stationdetail.html",
      "pageVisitPv": 29953,
      "pageVisitUv": 9695,
      "pageStaytimePv": 7.558508,
      "entrypagePv": 1386,
      "exitpagePv": 2285,
      "pageSharePv": 0,
      "pageShareUv": 0
    },
    {
      "pagePath": "pages/switch-city/switch-city.html",
      "pageVisitPv": 8928,
      "pageVisitUv": 4017,
      "pageStaytimePv": 9.22659,
      "entrypagePv": 748,
      "exitpagePv": 1613,
      "pageSharePv": 0,
      "pageShareUv": 0
    }
  ],
  "errMsg": "openapi.analysis.getVisitPage:ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

- ✔：该账号可调用此接口。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
