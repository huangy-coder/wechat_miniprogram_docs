# 消息通路发消息

> 官方文档：[消息通路发消息](https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/basic/api_cityservice_sendmsgdata.html)
> 所属分类：[城市服务](../../城市服务目录.md)
> 导航路径：城市服务 / 基础能力 / 消息通路发消息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：cityservice_sendmsgdata

接入微信城市服务，业务方需确保功能的闭环服务体验，需接入消息通路。[点击此处查看城市服务消息通路说明](https://developers.weixin.qq.com/community/business/doc/000a86762f86b093c8e9ec0205b80d)。

模板申请成功后，将会分配`biz_template_id`，并根据模板推送渠道不同分别提供样式ID：`result_page_style_id`、`deal_msg_style_id`、`card_style_id`。

1. 通过公众号提供服务时，需使用公众号用户 openid，获取openid方式请 [点击此处查看](https://developers.weixin.qq.com/doc/service/guide/h5/auth.html)。
2. 通过小程序提供服务时，需使用小程序用户 openid ，并使用与小程序关联的、且申请了“消息通路”的公众号的 access_token

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cityservice/sendmsgdata?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：22、105
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

`result_page_url` 页面报错提示

| 提示信息 | 说明 |
| --- | --- |
| 中文显示错误 | 字符集未用utf8 |
| 参数错误 | json参数错误 |
| 非本人，页面打开失败 | 非本人openid；或登录态获取失败 |
| 请在微信内打开 | 需在微信内打开页面 |
| 系统错误 | 其他错误 |

## 5. 代码示例

请求示例

```json
{
   "openid":"OPENID",
   "biz_template_id":"ngqIpbwh8bUfcSsECmogfXcV14J0tQlEpBO27izEYtY",
   "result_page_style_id":"cUjfPSEtwasWQFsJ5PXo218PexBaHy5jg_peVDe4WkY",
   "deal_msg_style_id":"cUjfPSEtwasWQFsJ5PXo24LeNjWbwMObXSHPNjVZ0uQ",
   "card_style_id":"cUjfPSEtwasWQFsJ5PXo2z8LSM0Q6FH05DCerWEVkDs",
   "order_no":"ORDER_NO",
   "url":"http://weixin.qq.com/download",
   "data":{
       "first": {
           "value":"恭喜你购买成功！",
           "color":"#173177"
       },
       "keynote1":{
           "value":"巧克力",
           "color":"#173177"
       },
       "keynote2": {
           "value":"39.8元",
           "color":"#173177"
       },
       "keynote3": {
           "value":"2014年9月22日",
           "color":"#173177"
       },
       "remark":{
           "value":"欢迎再次购买！",
           "color":"#173177"
       }
   }
}
```

返回示例

```json
{
  "errcode":0,
  "errmsg":"ok",
  "result_page_url":"https://city.weixin.qq.com/static/resultpagenew.html?openid=ont-9vjAcIdSU-LgB7ubALAVJO9U&biz_template_id=ngqIpbwh8bUfcSsECmogfXcV14J0tQlEpBO27izEYtY #wechat_redirect"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
