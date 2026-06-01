# 获取小程序性能数据

> 官方文档：[获取小程序性能数据](https://developers.weixin.qq.com/miniprogram/dev/server/API/data-analysis/others/api_getperformancedata.html)
> 所属分类：[数据分析](../../数据分析目录.md)
> 导航路径：数据分析 / 其他 / 获取小程序性能数据
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getPerformanceData

该接口用于获取小程序启动性能，运行性能等数据

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/business/performance/boot?access_token=ACCESS_TOKEN
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 调用方法：analysis.getPerformanceData
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.time Object Payload

开始和结束日期的时间戳，时间跨度不能超过30天

### Body.params(Array) Object Payload

查询条件，比如机型，网络类型等等

## 3. 返回参数

### 返回体 Response Payload

### Res.data Object Payload

返回的性能数据

### Res.data.body Object Payload

返回的性能数据

### Res.data.body.tables(Array) Object Payload

返回的数据数组

### Res.data.body.tables(Array).lines Object Payload

按时间排列的性能数据

### Res.data.body.tables(Array).lines .fields Object Payload

单天的性能数据

## 4. 注意事项

## 其他说明

### module 的合法值

| 值 | 说明 |
| --- | --- |
| 10016 | 打开率, params字段可传入网络类型和机型 |
| 10017 | 启动各阶段耗时，params字段可传入网络类型和机型 |
| 10021 | 页面切换耗时，params数组字段可传入机型 |
| 10022 | 内存指标，params数组字段可传入机型 |
| 10023 | 内存异常，params数组字段可传入机型 |

### field 的合法值

| 值 | 说明 |
| --- | --- |
| networktype | 网络类型作为查询条件，value=“-1,3g,4g,wifi”分别表示 全部网络类型，3G，4G，WIFI,不传networktype默认为全部网络类型 |
| device_level | 机型作为查询条件，此时value=“-1,1,2,3”分别表示 全部机型，高档机，中档机，低档机,不传device_level默认为全部机型 |
| device | 平台作为查询条件，此时value="-1,1,2"分别表示 全部平台，IOS平台，安卓平台,不传device默认为全部平台 |

## 5. 代码示例

### 5.1 HTTPS调用

请求示例

```json
{
  "time": {
    "end_timestamp": 1609689600,
    "begin_timestamp": 1609603200
  },
  "module": "10022",
  "params": [
    {
      "field": "networktype",
      "value": "wifi"
    },
    {
      "field": "device_level",
      "value": "1"
    },
    {
      "field": "device",
      "value": "1"
    }
  ]
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "body": {
      "tables": [
        {
          "id": "memorydiff",
          "lines": [
            {
              "fields": [
                {
                  "refdate": "20210103",
                  "value": "70.7778"
                },
                {
                  "refdate": "20210104",
                  "value": "72.0446"
                }
              ]
            }
          ],
          "zh": "内存增长均值"
        },
        {
          "id": "memory",
          "lines": [
            {
              "fields": [
                {
                  "refdate": "20210103",
                  "value": "314"
                },
                {
                  "refdate": "20210104",
                  "value": "302.3218"
                }
              ]
            }
          ],
          "zh": "内存均值"
        }
      ],
      "count": 2
    }
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
    const result = await cloud.openapi.analysis.getPerformanceData({
        "time": {
          "endTimestamp": 1609689600,
          "beginTimestamp": 1609603200
        },
        "module": '10022',
        "params": [
          {
            "field": 'networktype',
            "value": 'wifi'
          },
          {
            "field": 'device_level',
            "value": '1'
          },
          {
            "field": 'device',
            "value": '1'
          }
        ]
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
  "errCode": 0,
  "errMsg": "openapi.analysis.getPerformanceData:ok",
  "data": {
    "body": {
      "tables": [
        {
          "id": "memorydiff",
          "lines": [
            {
              "fields": [
                {
                  "refdate": "20210103",
                  "value": "70.7778"
                },
                {
                  "refdate": "20210104",
                  "value": "72.0446"
                }
              ]
            }
          ],
          "zh": "内存增长均值"
        },
        {
          "id": "memory",
          "lines": [
            {
              "fields": [
                {
                  "refdate": "20210103",
                  "value": "314"
                },
                {
                  "refdate": "20210104",
                  "value": "302.3218"
                }
              ]
            }
          ],
          "zh": "内存均值"
        }
      ],
      "count": 2
    }
  }
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
