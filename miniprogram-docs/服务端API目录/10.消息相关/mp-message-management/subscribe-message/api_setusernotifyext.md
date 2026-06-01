# 更新服务卡片扩展信息

> 官方文档：[更新服务卡片扩展信息](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_setusernotifyext.html)
> 所属分类：[消息相关](../../消息相关目录.md)
> 导航路径：消息相关 / 订阅消息 / 更新服务卡片扩展信息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：setUserNotifyExt

更新服务卡片扩展信息

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/set_user_notifyext?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

服务卡片详细介绍可参考[文章](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message-2.html)

## 5. 代码示例

请求示例

```json
{
  "notify_type": 1003,
  "openid": "xxx",
  "notify_code": "xxx",
  "ext_json": "{\"pay_info\":\"{\\\"transaction_id\\\":\\\"4200001855202305090060871147\\\",\\\"pay_amount\\\":2001,\\\"pay_time\\\":1683546394}\",\"store_info\":\"{\\\"store_name\\\":\\\"westore\\\",\\\"store_address\\\":\\\"深圳市南山区南山大道18号\\\",\\\"latitude\\\":22,\\\"longitude\\\":114}\"}"
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

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

- ✔：该账号可调用此接口。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
