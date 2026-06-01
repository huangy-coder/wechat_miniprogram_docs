# 触发云函数

> 官方文档：[触发云函数](https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/functions/api_invokecloudfunction.html)
> 所属分类：[云开发](../../云开发目录.md)
> 导航路径：云开发 / 云函数 / 触发云函数
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：invokeCloudFunction

通过本接口可以触发指定云开发环境中的云函数。

云函数是云开发中运行在云端的代码，可用于处理业务逻辑。

**重要提示**：使用本 API 触发的云函数无法获取 OpenID 等用户登录态信息，因此无法使用涉及用户登录态的其他 API。

## 1. 调用方式

### HTTPS 调用

```bash
POST New https://api.weixin.qq.com/tcb/invokecloudfunction?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：49
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

- 使用本 API 触发云函数，在云函数中无法获取 OpenID 等用户相关信息，无法使用涉及用户登录态的其他 API。
- 注意 POST BODY 部分会传递给云函数作为输入参数。
- 由 HTTP API 触发的云函数可以使用云调用。
- 由 HTTP API 触发云函数的超时时间为 5s，请注意云函数的执行时间不能过长。
- 如果是服务商模式-批量代云开发，则使用 [component_access_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getcomponentaccesstoken)；
- 如果是服务商模式-普通代云开发，则使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getauthorizeraccesstoken)；
- 如果是小程序普通调用，则使用 [access_token](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-access-token/api_getaccesstoken)。

## 5. 代码示例

请求示例

```text
curl -d '{}' \
'https://api.weixin.qq.com/tcb/invokecloudfunction?access_token=ACCESS_TOKEN&env=ENV&name=login'
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "resp_data": "{\"event\":{\"userInfo\":{\"appId\":\"SAMPLE_APPID\"}},\"appid\":\"SAMPLE_APPID\"}"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口支持「第三方平台」账号类型代调用，权限集请参考「调用方式」部分。其他账号类型如无特殊说明，均不可调用。
