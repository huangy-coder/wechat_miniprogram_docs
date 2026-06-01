# 获取小程序交易体验分违规记录

> 官方文档：[获取小程序交易体验分违规记录](https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/basic/api_getpenaltylist.html)
> 所属分类：[交易保障](../../交易保障目录.md)
> 导航路径：交易保障 / 基础能力 / 获取小程序交易体验分违规记录
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：GetPenaltyList

获取小程序交易体验分违规记录

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/wxaapi/wxamptrade/get_penalty_list?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：151
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.appealList(Array) Object Payload

记录列表

## 4. 枚举信息

### Res.appealList(Array).status Enum

扣分记录状态

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

请求示例

```text
GET https://api.weixin.qq.com/wxaapi/wxamptrade/get_penalty_list?access_token=xxx&offset=0&limit=10
```

返回示例

```json
{
    "appealList": [
        {
            "illegalOrderId": "12345",
            "complaintOrderId": "54321",
            "illegalWording": "质量缺陷",
            "status": 6,
            "illegalTime": 1656658706,
            "orderId": "payorder@567897862897364928374",
            "minusScore": 2,
            "updateTime": 1656907435
        },
        {
            "illegalOrderId": "61577",
            "complaintOrderId": "1360130",
            "illegalWording": "骚扰/辱骂他人",
            "status": 5,
            "illegalTime": 1656658601,
            "orderId": "payorder@_4200001450202207012836130249",
            "minusScore": 20,
            "updateTime": 1656659715
        }
    ],
    "currentScore": 55,
    "totalNum": 2,
    "errcode": 0
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。
