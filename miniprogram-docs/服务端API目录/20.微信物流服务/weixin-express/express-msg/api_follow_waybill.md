# 传运单

> 官方文档：[传运单](https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-msg/api_follow_waybill.html)
> 所属分类：[微信物流服务](../../微信物流服务目录.md)
> 导航路径：微信物流服务 / 消息组件 / 传运单
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：follow_waybill

商户使用此接口向微信提供某交易单号对应的运单号。微信后台会跟踪运单的状态变化，在关键物流节点给下单用户推送消息通知。

如有开发问题或建议，可前往[微信开放社区-微信物流服务](https://developers.weixin.qq.com/community/minihome/mixflow/1792207662500118536) 发帖提问讨论，官方工作人员会及时回复。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/delivery/open_msg/follow_waybill?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：45
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.goods_info Object Payload

商品信息

### Body.goods_info.detail_list(Array) Object Payload

商品信息

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
  "openid":"ovtZW4yB7DIj3CxOb6ii-nk4HhFo",
  "waybill_id":"WXTESTEXPRESS0000014",
  "sender_phone":"12345678901" ,
  "receiver_phone":"123456566" ,
  "goods_info":{
  	"detail_list":[
     {
       "goods_name":"测试名字",
       "goods_img_url":"www.qq.com"
     },
     {
       "goods_name":"测试名字2",
       "goods_img_url":"www.qq.com"
     }
    ]
  }
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "waybill_token": "o_ARWHaxIxzWHmdui-AIw9KBr8qNnbmc08V0KhDyXE-IMLo6AcOqJkPsNLcLzfTb"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
