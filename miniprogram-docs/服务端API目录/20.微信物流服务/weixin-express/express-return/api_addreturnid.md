# 创建退货ID

> 官方文档：[创建退货ID](https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/express-return/api_addreturnid.html)
> 所属分类：[微信物流服务](../../微信物流服务目录.md)
> 导航路径：微信物流服务 / 退货组件 / 创建退货ID
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：addReturnId

商家在同意用户退货之后，通过本接口创建退货ID，shop_order_id和退货 ID 一一对应。平台根据退货 ID 下发模板消息给用户，提醒用户退货。“一个订单需要多次退货”的场景，可以在商家内部 1 个退货订单号映射多个shop_order_id。注：该接口中文相关的字段用UTF-8。

提醒退货通知：商家创建退货 ID 时，平台会自动下发模板消息给用户，提醒用户退货。

如有开发问题或建议，可前往[微信开放社区-微信物流服务](https://developers.weixin.qq.com/community/minihome/mixflow/1792207662500118536) 发帖提问讨论，官方工作人员会及时回复。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/delivery/no_worry_return/add?access_token=ACCESS_TOKEN
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

### Body.biz_addr Object Payload

商家退货地址

### Body.user_addr Object Payload

用户购物时的收货地址

### Body.goods_list(Array) Object Payload

退货商品list，一个元素为对象的数组,结构如下↓ 如投保时已传入订单商品信息，则以投保时传入的为准

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
    "shop_order_id": "xxx",//商家内部系统使用的退货编号
    "biz_addr": {  //商家退货地址，必填
        "name": "张三",
        "mobile": "13600000000",//仅支持输入一个联系方式
        "country": "中国",
        "province": "广东省",
        "city": "广州市",
        "area": "海珠区",
        "address": "xx路 xx 号"
    },
    "user_addr": { //用户购物时的收货地址，选填
        "name": "李四",
        "mobile": "13600000000",
        "country": "中国",
        "province": "广东省",
        "city": "广州市",
        "area": "海珠区",
        "address": "xx路 xx 号"
     },
     "openid":"xxx",//退货用户的openid，用于给用户下发模版消息，通过模版消息用户可以选择退货方式
	 "order_path":"xxx",//退货订单在商家小程序的path
	 "goods_list":[
		{
			"name":"xxx",//退货商品的名称
			"url":"xxx"//退货商品图片的url
		}
	 ],
	 "order_price":1//退货订单的价格
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "OK",
  "return_id": "1935761508265738242"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
