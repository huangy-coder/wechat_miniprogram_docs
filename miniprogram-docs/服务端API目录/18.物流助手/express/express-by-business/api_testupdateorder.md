# 模拟更新订单状态

> 官方文档：[模拟更新订单状态](https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_testupdateorder.html)
> 所属分类：[物流助手](../../物流助手目录.md)
> 导航路径：物流助手 / 小程序使用 / 模拟更新订单状态
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：testUpdateOrder

该接口用于模拟快递公司更新订单状态, 该接口只能用户测试。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/business/test_update_order?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：45、71
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

## 其他说明

### action_type 的合法值

| 值 | 说明 |
| --- | --- |
| 100001 | 揽件阶段-揽件成功 |
| 100002 | 揽件阶段-揽件失败 |
| 100003 | 揽件阶段-分配业务员 |
| 200001 | 运输阶段-更新运输轨迹 |
| 300002 | 派送阶段-开始派送 |
| 300003 | 派送阶段-签收成功 |
| 300004 | 派送阶段-签收失败 |
| 400001 | 异常阶段-订单取消 |
| 400002 | 异常阶段-订单滞留 |

## 5. 代码示例

请求示例

```json
{
  "biz_id": "test_biz_id",
  "order_id": "xxxxxxxxxxxx",
  "delivery_id": "TEST",
  "waybill_id": "xxxxxxxxxx",
  "action_time": 123456789,
  "action_type": 100001,
  "action_msg": "揽件阶段"
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

本接口支持「小程序（仅认证）」账号类型调用。其他账号类型如无特殊说明，均不可调用。
