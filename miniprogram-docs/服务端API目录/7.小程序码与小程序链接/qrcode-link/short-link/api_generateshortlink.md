# 获取ShortLink

> 官方文档：[获取ShortLink](https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/short-link/api_generateshortlink.html)
> 所属分类：[小程序码与小程序链接](../../小程序码与小程序链接目录.md)
> 导航路径：小程序码与小程序链接 / Short Link / 获取ShortLink
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：generateShortLink

获取小程序 Short Link，适用于微信内拉起小程序的业务场景。目前对所有非个人主体小程序开放。通过该接口，可以选择生成到期失效和永久有效的小程序短链。

详情见[获取 Short Link](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/shortlink.html)。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/genwxashortlink?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：shortlink.generate
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：88
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Res.errcode Enum

[错误码](#apierrcode)

## 5. 注意事项

#### 调用上限

Link 将根据是否为到期有效与失效时间参数，分为 **短期有效ShortLink** 与 **永久有效ShortLink**：

- 单个小程序每日生成 ShortLink 上限为1000万个（包含短期有效 ShortLink 与长期有效 ShortLink ）
- 单个小程序总共可生成永久有效 ShortLink 上限为10万个，请谨慎调用。
- 短期有效ShortLink 有效时间为30天，单个小程序生成短期有效ShortLink 不设上限。

## 6. 代码示例

请求示例

```json
{
    "page_url": "pages/publishHomework/publishHomework?query1=q1",
    "page_title": "Homework title",
    "is_permanent":false
}
```

返回示例

```json
{
 "errcode": 0,
 "errmsg": "ok",
 "link": "Short Link"
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。

`page_title`
