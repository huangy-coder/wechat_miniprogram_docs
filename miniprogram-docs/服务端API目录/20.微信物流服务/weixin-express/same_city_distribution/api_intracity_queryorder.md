# 查询配送单

> 官方文档：[查询配送单](https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_queryorder.html)
> 所属分类：[微信物流服务](../../微信物流服务目录.md)
> 导航路径：微信物流服务 / 同城配送 / 查询配送单
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：intracity_queryorder

通过该接口查询订单是否创建成功，以及订单创建后的状态更新

如有开发问题或建议，可前往[微信开放社区-微信物流服务](https://developers.weixin.qq.com/community/minihome/mixflow/1792207662500118536) 发帖提问讨论，官方工作人员会及时回复。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/intracity/queryorder?access_token=ACCESS_TOKEN
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

### Res.transporter_info Object Payload

配送员信息

### Res.store_info Object Payload

门店信息

### Res.receiver_info Object Payload

收货人信息

### Res.cargo_info Object Payload

商品信息

### Res.cargo_info.item_list Object Payload

商品详情

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
	"wx_order_id": "2000000000000042007",
	"store_order_id": "testorder12345",
	"order_status": 10000,
	"appid": "wx539e0b4872f196d1",
	"user_openid": "ozMQO0ehr_FBgL5mWa5_duxH71Yw",
	"service_trans_id": "SFTC",
	"delivery_no": "SF6508800795950",
	"distance": 2358,
	"actualfee": 201,
	"deductfee": 0,
	"create_time": 1682318663,
	"expected_finish_time": 1682319663,
	"store_info": {
		"phone_num": "13800000138",
		"address": "北京市海淀区西三旗街道永辉超市",
		"lng": 116.354787,
		"lat": 40.030613,
		"store_name": "测试门店3"
	},
	"receiver_info": {
		"phone_num": "顺丰同城",
		"address": "北京市海淀区学清嘉创大厦A座15层）",
		"lng": 116.353093,
		"lat": 40.01496
	},
	"cargo_info": {
		"cargo_name": "榴莲披萨套餐",
		"cargo_weight": 500,
		"cargo_price": 5000,
		"cargo_num": 3,
		"cargo_type": 1
        "item_list":[
            {            "item_name":"8寸榴莲"，
             "item_num":1,
             "item_pic_url": "https://www.qq.com",
            },
            {            "item_name":"可口可乐"，
             "item_num":2,
             "item_pic_url": "https://www.qq.com",
            },
        ]
	},
	"errcode": 0,
	"errmsg": "ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
