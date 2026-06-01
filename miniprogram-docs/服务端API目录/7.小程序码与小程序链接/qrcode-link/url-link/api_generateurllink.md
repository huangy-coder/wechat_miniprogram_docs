# 获取加密URLLink

> 官方文档：[获取加密URLLink](https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/url-link/api_generateurllink.html)
> 所属分类：[小程序码与小程序链接](../../小程序码与小程序链接目录.md)
> 导航路径：小程序码与小程序链接 / URL Link / 获取加密URLLink
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：generateUrlLink

获取小程序 URL Link，适用于短信、邮件、网页、微信内等拉起小程序的业务场景。目前仅针对国内非个人主体的小程序开放，详见[获取 URL Link](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/url-link.html)

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/generate_urllink?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：urllink.generate
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：88
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.cloud_base Object Payload

云开发静态网站自定义 H5 配置参数，可配置中转的云开发 H5 页面。不填默认用官方 H5 页面

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

#### 调用上限

- 生成端：每天生成 URL Scheme（加密+明文） 和 URL Link 的总数量上限为50万
- 打开端：每天通过 URL Scheme（加密+明文） 和 URL Link 打开小程序的总次数上限为300万
- **自 2023 年 12 月 19 日起，取消 URL Link 一人一链的限制，支持同一条连接被多名用户访问。详细调整说明可见[《URL Scheme 和 URL Link优化公告》](https://developers.weixin.qq.com/community/develop/doc/00024e32cbc36055c0c0a34b066401)。**

#### 返回值说明

- 如果调用成功，会直接返回生成的小程序 URL Link。如果请求失败，会返回 JSON 格式的数据。

#### 其他注意事项

- **加密 URL Link 支持开发者自行在链接后面拼接 query 参数，详见[获取 URL Link](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/url-link.html)**
- 只能生成已发布的小程序的 URL Link。
- 在微信内或者安卓手机打开 URL Link 时，默认会先跳转官方 H5 中间页，如果需要定制 H5 内容，可以使用云开发静态网站。

## 5. 代码示例

### 5.1 HTTPS请求

请求示例

```json
{
  "path": "/pages/publishHomework/publishHomework",
  "query": "",
  "expire_type": 1,
  "expire_interval": 1,
  "env_version": "release",
  "cloud_base": {
    "env": "xxx",
    "domain": "xxx.xx",
    "path": "/jump-wxa.html",
    "query": "a=1&b=2"
  }
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "url_link": "URL Link"
}
```

### 5.2 云函数调用

请求示例

```json
const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
})
exports.main = async (event, context) => {
  try {
    const result = await cloud.openapi.urllink.generate({
        "path": '/pages/publishHomework/publishHomework',
        "query": '',
        "isExpire": true,
        "expireType": 1,
        "expireInterval": 1,
        "envVersion": 'release',
        "cloudBase": {
          "env": 'xxx',
          "domain": 'xxx.xx',
          "path": '/jump-wxa.html',
          "query": 'a=1&b=2'
        }
      })
    return result
  } catch (err) {
    return err
  }
}
```

返回示例

```json
{
  "errCode": 0,
  "errMsg": "ok",
  "urlLink": "URL Link"
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
