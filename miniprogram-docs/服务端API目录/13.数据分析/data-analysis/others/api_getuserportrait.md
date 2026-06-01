# 获取小程序用户画像分布

> 官方文档：[获取小程序用户画像分布](https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/others/api_getuserportrait.html)
> 所属分类：[数据分析](../../数据分析目录.md)
> 导航路径：数据分析 / 其他 / 获取小程序用户画像分布
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getUserPortrait

该接口用于获取小程序新增或活跃用户的画像分布数据。时间范围支持昨天、最近7天、最近30天。其中，新增用户数为时间范围内首次访问小程序的去重用户数，活跃用户数为时间范围内访问过小程序的去重用户数。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/datacube/getweanalysisappiduserportrait?access_token=ACCESS_TOKEN
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 调用方法：analysis.getUserPortrait
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

### Res.visit_uv_new Object Payload

新用户画像

### Res.visit_uv Object Payload

活跃用户画像

### Res.visit_uv_new.province(Array) Object Payload

省份，如北京、广东等

### Res.visit_uv_new.city(Array) Object Payload

城市，如北京、广州等

### Res.visit_uv_new.genders(Array) Object Payload

性别，包括男、女、未知

### Res.visit_uv_new.platforms(Array) Object Payload

平台类型，包括 Android、iOS 等

### Res.visit_uv_new.devices(Array) Object Payload

终端类型，包括 iPhone，android，其他

### Res.visit_uv_new.ages(Array) Object Payload

年龄，包括17岁以下、18-24岁等区间

### Res.visit_uv.province(Array) Object Payload

省份，如北京、广东等

### Res.visit_uv.city(Array) Object Payload

城市，如北京、广州等

### Res.visit_uv.genders(Array) Object Payload

性别，包括男、女、未知

### Res.visit_uv.platforms(Array) Object Payload

平台类型，包括 Android、iOS 等

### Res.visit_uv.devices(Array) Object Payload

终端类型，包括 iPhone，android，其他

### Res.visit_uv.ages(Array) Object Payload

年龄，包括17岁以下、18-24岁等区间

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

### 5.1 HTTPS调用

请求示例

```json
{
  "begin_date": "20170611",
  "end_date": "20170617"
}
```

返回示例

```json
{
  "ref_date": "20170611",
  "visit_uv_new": {
    "province": [
      {
        "id": 31,
        "name": "广东省",
        "value": 215
      }
    ],
    "city": [
      {
        "id": 3102,
        "name": "广州",
        "value": 78
      }
    ],
    "genders": [
      {
        "id": 1,
        "name": "男",
        "value": 2146
      }
    ],
    "platforms": [
      {
        "id": 1,
        "name": "iPhone",
        "value": 27642
      }
    ],
    "devices": [
      {
        "name": "OPPO R9",
        "value": 61
      }
    ],
    "ages": [
      {
        "id": 1,
        "name": "17岁以下",
        "value": 151
      }
    ]
  },
  "visit_uv": {
    "province": [
      {
        "id": 31,
        "name": "广东省",
        "value": 1341
      }
    ],
    "city": [
      {
        "id": 3102,
        "name": "广州",
        "value": 234
      }
    ],
    "genders": [
      {
        "id": 1,
        "name": "男",
        "value": 14534
      }
    ],
    "platforms": [
      {
        "id": 1,
        "name": "iPhone",
        "value": 21750
      }
    ],
    "devices": [
      {
        "name": "OPPO R9",
        "value": 617
      }
    ],
    "ages": [
      {
        "id": 1,
        "name": "17岁以下",
        "value": 3156
      }
    ]
  }
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
    const result = await cloud.openapi.analysis.getUserPortrait({
        "beginDate": '20170611',
        "endDate": '20170617'
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
  "refDate": "20170611",
  "visitUvNew": {
    "province": [
      {
        "id": 31,
        "name": "广东省",
        "value": 215
      }
    ],
    "city": [
      {
        "id": 3102,
        "name": "广州",
        "value": 78
      }
    ],
    "genders": [
      {
        "id": 1,
        "name": "男",
        "value": 2146
      }
    ],
    "platforms": [
      {
        "id": 1,
        "name": "iPhone",
        "value": 27642
      }
    ],
    "devices": [
      {
        "name": "OPPO R9",
        "value": 61
      }
    ],
    "ages": [
      {
        "id": 1,
        "name": "17岁以下",
        "value": 151
      }
    ]
  },
  "visitUv": {
    "province": [
      {
        "id": 31,
        "name": "广东省",
        "value": 1341
      }
    ],
    "city": [
      {
        "id": 3102,
        "name": "广州",
        "value": 234
      }
    ],
    "genders": [
      {
        "id": 1,
        "name": "男",
        "value": 14534
      }
    ],
    "platforms": [
      {
        "id": 1,
        "name": "iPhone",
        "value": 21750
      }
    ],
    "devices": [
      {
        "name": "OPPO R9",
        "value": 617
      }
    ],
    "ages": [
      {
        "id": 1,
        "name": "17岁以下",
        "value": 3156
      }
    ]
  },
  "errMsg": "openapi.analysis.getUserPortrait:ok"
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
