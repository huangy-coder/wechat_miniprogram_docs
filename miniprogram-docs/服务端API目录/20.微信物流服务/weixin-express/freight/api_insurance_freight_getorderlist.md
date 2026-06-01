# 拉取保单信息

> 官方文档：[拉取保单信息](https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_getorderlist.html)
> 所属分类：[微信物流服务](../../微信物流服务目录.md)
> 导航路径：微信物流服务 / 无忧退货 / 拉取保单信息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：insurance_freight_getorderlist

本接口用于拉取保单信息

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/business/insurance_freight/getorderlist?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：139
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.list(Array) Object Payload

保单列表

## 4. 枚举信息

### Body.status_list Enum

保单状态

### Body.sort_direct Enum

排序方式

### Res.list(Array).status Enum

保单状态

### Res.list(Array).is_home_pick_up Enum

是否上门取件

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

请求示例

```json
{
    "status_list": [
        2, 4, 5
    ],
    "offset": 0,
    "limit": 20
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "list": [
        {
            "order_no": "4200001197202103228672982584",
            "policy_no": "10288003264673876281",
            "report_no": "",
            "status": 2,
            "insurance_end_date": "2023-06-14 19:41:34",
            "premium": 20,
            "estimate_amount": 1200,
            "delivery_no": "delivery20230321001",
            "refund_delivery_no": "delivery20230322001",
            "is_home_pick_up": 1
        },
        {
            "order_no": "4200001197202103228672982585",
            "policy_no": "10288003264673876282",
            "report_no": "90581008120350195232",
            "status": 4,
            "insurance_end_date": "2023-06-20 16:36:54",
            "premium": 20,
            "estimate_amount": 1200,
            "delivery_no": "delivery20230322001",
            "refund_delivery_no": "delivery20230322001",
            "is_home_pick_up": 1
        }
    ],
    "total": 2
}
```

## 7. 错误码

此接口没有特殊错误码，可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。
