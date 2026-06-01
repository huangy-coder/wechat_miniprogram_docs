# 查询门店

> 官方文档：[查询门店](https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_querystore.html)
> 所属分类：[微信物流服务](../../微信物流服务目录.md)
> 导航路径：微信物流服务 / 同城配送 / 查询门店
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：intracity_querystore

获取本小程序所创建的门店，不传wx_store_id和out_store_id则返回本小程序所有门店信息

如有开发问题或建议，可前往[微信开放社区-微信物流服务](https://developers.weixin.qq.com/community/minihome/mixflow/1792207662500118536) 发帖提问讨论，官方工作人员会及时回复。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/intracity/querystore?access_token=ACCESS_TOKEN
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

### Res.store_list(Array) Object Payload

门店信息列表，在请求成功时返回

### Res.store_list(Array).address_info Object Payload

门店地址信息

## 4. 注意事项

# 其他说明

### 物品类型列表

| 物品类型 | 类型名称 |
| --- | --- |
| 1 | 快餐 |
| 2 | 药品 |
| 3 | 百货 |
| 6 | 生鲜 |
| 8 | 酒品 |
| 12 | 文件 |
| 13 | 蛋糕 |
| 14 | 鲜花 |
| 15 | 数码 |
| 16 | 服装 |
| 17 | 汽配 |
| 18 | 珠宝 |
| 32 | 饮料 |
| 36 | 证照 |
| 55 | 宠物用品 |
| 56 | 母婴用品 |
| 57 | 美妆用品 |
| 58 | 家居建材 |
| 99 | 其他 |

### 运力列表

| 运力名称 | 运力ID |
| --- | --- |
| 达达 | DADA |
| 顺丰同城 | SFTC |

## 5. 代码示例

请求示例

```json
{
    "wx_store_id":"4000000000000042001"
}
```

返回示例

```json
{
	"errcode": 0,
	"errmsg": "ok",
	"total": 1,
	"appid": "wx539e0b4872f196d1",
	"store_list": [{
		"wx_store_id": "4000000000000042001",
		"out_store_id": "123",
		"city_id": 440300,
		"address_info": {
			"province": "广东省",
			"city": "深圳市",
			"area": "南山区",
			"street": "南头街道",
			"house": "深南大道10000号",
			"lat": 22.540366,
			"lng": 113.934559,
			"phone": "1380000138"
		},
		"order_pattern": 0,
		"service_trans_prefer": ""
	}]
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
