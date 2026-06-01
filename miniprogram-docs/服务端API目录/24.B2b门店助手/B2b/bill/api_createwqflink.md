# 跳转银行转账页面

> 官方文档：[跳转银行转账页面](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/bill/api_createwqflink.html)
> 所属分类：[B2b门店助手](../../B2b门店助手目录.md)
> 导航路径：B2b门店助手 / B2b支付 / 跳转银行转账页面
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：createWqfLink

申请开通银行转账后，当开通状态描述为“待完善信息”、“待用户签约”、“申请驳回”时，都需要跳转到微企付页面完成相应操作。

**页面端方式：**


**接口端方式：**

可以通过此 api 方式获取微企付页面跳转链接。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/retail/B2b/createwqflink?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：158
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

- 该跳转链接有过期时限，且限制点击次数，应在每次跳转前调用接口生成新的链接。

## 5. 代码示例

请求示例

```json
{
    "request_no": "MSE123"
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "url": "https://tencent.com",
    "expire_time": "2025-03-19T16:08:17+08:00"
}
```

## 6. 错误码

此接口没有特殊错误码，可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
