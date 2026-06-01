# 查询购买资源包的用量情况

> 官方文档：[查询购买资源包的用量情况](https://developers.weixin.qq.com/miniprogram/dev/server/API/charge/api_getusagedetail.html)
> 所属分类：[付费管理](../付费管理目录.md)
> 导航路径：付费管理 / 查询购买资源包的用量情况
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getUsageDetail

小程序可通过本接口查询已购买资源包的用量情况。

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/wxa/charge/usage/get?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.detailList(Array) Object Payload

用量详情列表

## 4. 枚举信息

### Res.detailList(Array).status Enum

资源包状态

### Res.detailList(Array).source Enum

额度来源

## 5. 注意事项

# 其他说明

all字段具体含义：

每项付费能力正常收费期间：当前生效的资源包的总量（和原effectiveAll含义相同，原字段废弃）
每项付费能力预公告收费，但未正式计费期间：当前生效以及购买后未生效的资源包的总量

## 6. 代码示例

请求示例

```text
GET https://api.weixin.qq.com/wxa/charge/usage/get?access_token=ACCESS_TOKEN&spuId=10000001&offset=0&limit=10
```

返回示例

```json
{
  "errcode": 0,
  "all": "10",
  "effectiveAll": "10",
  "effectiveUse": "0",
  "startServiceTime": 1669129510,
  "endServiceTime": 1709450190,
  "total": 2,
  "detailList": [
    {
      "pkgId": "ZY2823973277692477440",
      "startTime": 1677914190,
      "endTime": 1709450190,
      "used": "0",
      "all": "4",
      "status": 1,
      "spuId": "10000057",
      "skuId": "20000059"
    },
    {
      "pkgId": "ZY2676590816357400576",
      "startTime": 1669129510,
      "endTime": 1700665510,
      "used": "0",
      "all": "6",
      "status": 1,
      "spuId": "10000057",
      "skuId": "20000060"
    }
  ]
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。
