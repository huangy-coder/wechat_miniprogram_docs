# 拉取充值订单信息

> 官方文档：[拉取充值订单信息](https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/freight/api_insurance_freight_getpayorderlist.html)
> 所属分类：[微信物流服务](../../微信物流服务目录.md)
> 导航路径：微信物流服务 / 无忧退货 / 拉取充值订单信息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：insurance_freight_getpayorderlist

本接口用于拉取充值订单信息

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/business/insurance_freight/getpayorderlist?access_token=ACCESS_TOKEN
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

充值订单列表

## 4. 枚举信息

### Body.status_list Enum

订单状态

### Res.list(Array).order_status Enum

订单状态

### Res.list(Array).refund_status Enum

退款状态

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

请求示例

```json
{
    "status_list": [
        2, 3, 4, 5, 6
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
            "order_id": 2850151276313431996,
            "order_status": 5,
            "total_price": 1000,
            "create_time": 1678966793,
            "pay_time": 1678966880,
            "can_refund": true,
            "refund_time": 0,
            "refund_status": 1
        }
    ],
    "total": 1
}
```

## 7. 错误码

此接口没有特殊错误码，可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。
