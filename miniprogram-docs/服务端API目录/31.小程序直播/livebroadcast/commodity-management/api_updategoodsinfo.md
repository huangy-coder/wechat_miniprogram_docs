# 更新商品

> 官方文档：[更新商品](https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/commodity-management/api_updategoodsinfo.html)
> 所属分类：[小程序直播](../../小程序直播目录.md)
> 导航路径：小程序直播 / 商品管理 / 更新商品
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：updateGoodsinfo

调用此接口可以更新商品信息，审核通过的商品仅允许更新价格类型与价格，审核中的商品不允许更新，未审核的商品允许更新所有字段， 只传入需要更新的字段。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxaapi/broadcast/goods/update?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：liveBroadcast.goodsUpdate
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：52
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.goodsInfo Object Payload

商品信息

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

{

```
"goodsInfo": {        
    // 需要更新哪个字段就传入哪个字段，goodsId 必传        
    "coverImgUrl": "ZuYVNKk9sMP1X4m7FXdcDCKra251KDZTjS502UTV7gwalgLZXcrOhG6oNYX6c7AR",        
    "name":"TIT茶杯",        
    "priceType":1,
    "price":99.5,
    // "price2": 150.5, priceType为2或3时必填
    "url": "pages/index/index",       
    "goodsId": 9     
}
```

}

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
