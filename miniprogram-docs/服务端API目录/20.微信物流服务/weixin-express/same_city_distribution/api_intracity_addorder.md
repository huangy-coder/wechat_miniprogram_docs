# 创建配送单

> 官方文档：[创建配送单](https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_addorder.html)
> 所属分类：[微信物流服务](../../微信物流服务目录.md)
> 导航路径：微信物流服务 / 同城配送 / 创建配送单
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：intracity_addorder

创建同城配送单，会根据门店设置的运力偏好来选择运力公司下单。如果没有设置偏好，则默认优先下单低价运力。

如有开发问题或建议，可前往[微信开放社区-微信物流服务](https://developers.weixin.qq.com/community/minihome/mixflow/1792207662500118536) 发帖提问讨论，官方工作人员会及时回复。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/intracity/addorder?access_token=ACCESS_TOKEN
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

### Body.cargo Object Payload

商品信息

### Body.cargo.item_list Object Payload

物品列表，物品的图片和名称等

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Body.verify_code_type Enum

验证码类型

## 5. 注意事项

```text
使用顺丰的沙箱环境环境需要固定的收件人信息（达达没有要求），收件人信息如下
收件人姓名：顺丰同城
收件人手机：13881979410 
收件地址：北京市海淀区学清嘉创大厦A座15层
```

# 其他说明

## 订单状态回调

### 回调协议

当订单状态发生变更时，会由微信服回调接入方的回调地址进行状态变更的通知，回调接口地址需要接入方在下单时传入，详见[门店余额查询](https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/same_city_distribution/api_intracity_balancequery)

| 字段 | 字段名 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- |
| appid | appid | string | 是 | 下单小程序appid |
| wx_store_id | 微信门店id | string | 是 |   |
| wx_order_id | 微信订单号 | string | 是 |   |
| store_order_id | 门店订单号 | string | 是 |   |
| order_status | 订单状态 | uint32 | 是 | 详情看下方订单状态列表 |
| status_change_time | 订单状态变更时间 | uint32 | 是 | 秒级时间戳格式 |
| timestamp | 消息推送时间 | uint32 | 是 | 秒级时间戳格式 |
| service_trans_id | 运力ID | string | 是 |   |
| sign | 签名值 | string | 是 | 生成方式详见回调报文示例里的签名步骤说明 |

### 回调报文示例：

```text
{
    "appid":"wx539e0b4872f19621",
    "order_status":40000,
    "service_trans_id":"DADA",
    "status_change_time":1711458532,
    "store_order_id":"sa5dadada12fd4assdsdad11s",
    "timestamp":1711458532,
    "wx_order_id":"4018734875633256960",
    "wx_store_id":"4000000000000042001",
    "sign":"a85489d9444bdd382e0de0ddca67a8ee"
}
```

#### 签名步骤:

1.对报文的数据做预处理用=连接key和value组成键值对，按key的ascii码升序排列键值对用&链接,示例如下：

```text
appid=wx539e0b4872f19621&order_status=40000&service_trans_id=DADA&status_change_time=1711458532&store_order_id=sa5dadada12fd4assdsdad11s&timestamp=1711458532&wx_order_id=4018734875633256960&wx_store_id=4000000000000042001
```

2.拼接小程序的安全token，安全token需要在下单小程序管理后台设置和获取，设置路径：开发管理->开发设置->消息推送->Token

```text
appid=wx539e0b4872f19621&order_status=40000&service_trans_id=DADA&status_change_time=1711458532&store_order_id=sa5dadada12fd4assdsdad11s×tamp=1711458532&wx_order_id=4018734875633256960&wx_store_id=4000000000000042001&token=abcdefghi
```

3.对第二步中的字符串计算MD5，得到十六进制结果取小写。

```text
to_lower(to_hex(md5(sign_str)))
```

签名值：a85489d9444bdd382e0de0ddca67a8ee 商家需要回复报文：

```json
{
    "return_code":0,
    "return_msg":"OK"
}
```

表示应答成功，如果没有接收到正确的请求应答，微信会重试回调。

### 订单状态列表

| 状态类型 | 状态名称 |
| --- | --- |
| 10000 | 订单创建成功 |
| 20000 | 商家取消订单 |
| 20001 | 配送方取消订单 |
| 30000 | 配送员接单 |
| 40000 | 配送员到店 |
| 50000 | 配送中 |
| 60000 | 配送员撤单 |
| 70000 | 配送完成 |
| 90000 | 配送异常 |

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

## 6. 代码示例

请求示例

```json
{
	"wx_store_id": "4000000000000042001",
	"store_order_id": "testorder123",
	"user_openid": "ozMQO0WsxkA3E56SWBGrLGQ4WVZY",
	"user_lng": "116.353093",
	"user_lat": "40.01496",
	"user_address": "北京市海淀区学清嘉创大厦A座15层）",
	"user_name": "顺丰同城",
	"user_phone": "13881979410",
	"callback_url": "https://testcallback.com",
	"use_sandbox": 1,
	"cargo": {
		"cargo_name": "榴莲披萨套餐",
		"cargo_type": 1,
		"cargo_num": 3,
		"cargo_price": 5000,
		"cargo_weight": 500，
        "item_list":[
            {                       
                "item_name":"8寸榴莲",
                "count":1,
                "item_pic_url": "https://www.qq.com"
            },
            {              
                "item_name":"可口可乐",
                "count":2,
                "item_pic_url": "https://www.qq.com"
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
	"service_trans_id": "SFTC",
	"wx_store_id": "1000000000000023002",
	"store_order_id": "testorder123",
	"distance": 2358,
	"fee": 1300,
    "trans_order_id":"JS123143DA"
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
