# 获取加密scheme码

> 官方文档：[获取加密scheme码](https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/url-scheme/api_generatescheme.html)
> 所属分类：[小程序码与小程序链接](../../小程序码与小程序链接目录.md)
> 导航路径：小程序码与小程序链接 / URL Scheme / 获取加密scheme码
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：generateScheme

- 该接口用于获取小程序 scheme 码，适用于短信、邮件、外部网页、微信内等拉起小程序的业务场景。目前仅针对国内非个人主体的小程序开放，详见[获取 URL scheme](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/url-scheme.html)。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/generatescheme?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：urlscheme.generate
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：88
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.jump_wxa Object Payload

跳转到的目标小程序信息。

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

#### 调用上限

- 生成端：每天生成 URL Scheme（加密+明文） 和 URL Link 的总数量上限为50万
- 打开端：每天通过 URL Scheme（加密+明文） 和 URL Link 打开小程序的总次数上限为300万
- **自 2023 年 12 月 19 日起，取消 URL Scheme 一人一链的限制，支持同一条连接被多名用户访问。详细调整说明可见[《URL Scheme 和 URL Link优化公告》](https://developers.weixin.qq.com/community/develop/doc/00024e32cbc36055c0c0a34b066401)。**

### 其他注意事项

- **加密 URL Scheme 支持开发者自行在链接后面拼接 query 参数，详见[获取 URL Scheme](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/url-scheme.html)**
- 微信内的网页如需打开小程序请使用微信开放标签-小程序跳转按钮，无公众号也可以直接使用小程序身份开发网页并免鉴权跳转小程序，见云开发静态网站跳转小程序。符合开放范围的小程序可以下发支持打开小程序的短信
- 该功能基本覆盖当前用户正在使用的微信版本，开发者无需进行低版本兼容
- 只能生成已发布的小程序的 URL Scheme
- 通过 URL Scheme 跳转到微信时，可能会触发系统弹框询问，若用户选择不跳转，则无法打开小程序。请开发者妥善处理用户选择不跳转的场景
- 部分浏览器会限制打开网页直接跳转，可参考示例网页设置跳转按钮

## 5. 代码示例

### 5.1 HTTPS请求

请求示例

```json
{
  "jump_wxa": {
    "path": "/pages/publishHomework/publishHomework",
    "query": "",
    "env_version": "release"
  },
  "is_expire": true,
  "expire_type": 1,
  "expire_interval": 1
}
```

返回示例

```json
{
 "errcode": 0,
 "errmsg": "ok",
 "openlink": Scheme
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
    const result = await cloud.openapi.urlscheme.generate({
        "jumpWxa": {
          "path": '/pages/publishHomework/publishHomework',
          "query": ''
        },
        "isExpire": true,
        "expireTime": 1606737600
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
 "errcode": 0,
 "errmsg": "ok",
 "openlink": Scheme
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
