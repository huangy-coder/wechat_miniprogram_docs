# 获取所有绑定的物流账号

> 官方文档：[获取所有绑定的物流账号](https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-business/api_getallaccount.html)
> 所属分类：[物流助手](../../物流助手目录.md)
> 导航路径：物流助手 / 小程序使用 / 获取所有绑定的物流账号
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getAllAccount

该接口用于获取所有绑定的物流账号。

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/cgi-bin/express/business/account/getall?access_token=ACCESS_TOKEN
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 调用方法：logistics.getAllAccount
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：45、71
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

无

## 3. 返回参数

### 返回体 Response Payload

### Res.list(Array) Object Payload

账号列表

### Res.list(Array).service_type Object Payload

该绑定帐号支持的服务类型

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```text
GET https://api.weixin.qq.com/cgi-bin/express/business/account/getall?access_token=ACCESS_TOKEN
```

返回示例

```json
{
  "count": 1,
  "list": [
    {
      "biz_id": "123456789",
      "delivery_id": "YUNDA",
      "create_time": 1555482786,
      "update_time": 1556594799,
      "status_code": 0,
      "alias": "",
      "remark_wrong_msg": "",
      "remark_content": "",
      "quota_num": 55,
      "quota_update_time": 1556594799
    }
  ]
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口支持「小程序（仅认证）」账号类型调用。其他账号类型如无特殊说明，均不可调用。
