# 设置扣费主体

> 官方文档：[设置扣费主体](https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_setpaymode.html)
> 所属分类：[微信物流服务](../../微信物流服务目录.md)
> 导航路径：微信物流服务 / 同城配送 / 设置扣费主体
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：intracity_setpaymode

默认扣费主体和充值主体都是门店，该接口可以让开发者设置门店的扣费主体，接口调用成功后，小程序的管理员会收到模板消息，点击模板消息确认更改门店扣费主体后，修改生效。目前支持的扣费主体有：服务商，小程序和门店，详细说明见下方其他说明中充值&扣费主体说明

如有开发问题或建议，可前往[微信开放社区-微信物流服务](https://developers.weixin.qq.com/community/minihome/mixflow/1792207662500118536) 发帖提问讨论，官方工作人员会及时回复。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/intracity/setpaymode?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：51
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

# 其他说明

### 充值&扣费主体说明

同城配送支持以服务商/小程序/门店维度进行充值，充值后名下所有门店都可以统一使充值的运费。

1. 服务商：小程序服务商。
2. 小程序：商家或品牌。
3. 门店：商家或品牌在不同地区的线下门店。该主体也是配送单发单主体。

## 5. 代码示例

请求示例

```json
{
    "appid":"wx539e0b4872f196d1",
    "pay_mode":"PAY_MODE_APP"
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
