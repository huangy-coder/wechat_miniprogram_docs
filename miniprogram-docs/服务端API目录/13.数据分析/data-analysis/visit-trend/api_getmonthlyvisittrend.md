# 获取用户访问小程序数据月趋势

> 官方文档：[获取用户访问小程序数据月趋势](https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/visit-trend/api_getmonthlyvisittrend.html)
> 所属分类：[数据分析](../../数据分析目录.md)
> 导航路径：数据分析 / 访问趋势 / 获取用户访问小程序数据月趋势
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getMonthlyVisitTrend

该接口用于获取用户访问小程序数据月趋势(能查询到的最新数据为上一个自然月的数据)。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/datacube/getweanalysisappidmonthlyvisittrend?access_token=ACCESS_TOKEN
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 调用方法：analysis.getMonthlyVisitTrend
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

限定查询一个自然月的数据，时间必须按照自然月的方式输入： 如：20170301, 20170331

## 5. 代码示例

### 5.1 HTTPS调用

请求示例

```json
{
  "begin_date": "20170301",
  "end_date": "20170331"
}
```

返回示例

```json
{
  "list": [
    {
      "ref_date": "201703",
      "session_cnt": 126513,
      "visit_pv": 426113,
      "visit_uv": 48659,
      "visit_uv_new": 6726,
      "stay_time_session": 56.4112,
      "visit_depth": 2.0189
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
    const result = await cloud.openapi.analysis.getMonthlyVisitTrend({
        "beginDate": '20170301',
        "endDate": '20170331'
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
  "list": [
    {
      "refDate": "201703",
      "sessionCnt": 126513,
      "visitPv": 426113,
      "visitUv": 48659,
      "visitUvNew": 6726,
      "stayTimeSession": 56.4112,
      "visitDepth": 2.0189
    }
  ],
  "errMsg": "openapi.analysis.getMonthlyVisitTrend:ok"
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
