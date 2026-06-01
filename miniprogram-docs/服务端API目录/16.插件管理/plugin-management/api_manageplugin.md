# 插件管理

> 官方文档：[插件管理](https://developers.weixin.qq.com/miniprogram/dev/server/API/plugin-management/api_manageplugin.html)
> 所属分类：[插件管理](../插件管理目录.md)
> 导航路径：插件管理 / 插件管理
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：managePlugin

该接口用于管理插件，支持申请、查看、更新、删除插件等操作。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/plugin?access_token=ACCESS_TOKEN
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 调用方法：pluginManager.getPluginList
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：40
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.plugin_list(Array) Object Payload

申请或使用中的插件信息列表，当 action == 'list' 时返回

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

### 5.1 申请插件示例

请求示例

```json
{
  "action": "apply",
  "plugin_appid": "aaaa",
  "reason": "hello"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.2 更新插件示例

请求示例

```json
{
  "action": "update",
  "user_version": "2.2.46",
  "plugin_appid": "wx5514af450eaceec2"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.3 获取插件列表示例

请求示例

```json
{
  "action": "list"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "plugin_list": [
    {
      "appid": "aaaa",
      "status": 1,
      "nickname": "插件昵称",
      "headimgurl": "http://plugin.qq.com"
    }
  ]
}
```

### 5.4 删除已添加的插件

请求示例

```json
{
  "action": "unbind",
  "plugin_appid": "aaaa"
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

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。
