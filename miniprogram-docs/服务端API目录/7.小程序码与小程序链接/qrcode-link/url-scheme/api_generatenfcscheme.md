# 获取NFC的小程序scheme

> 官方文档：[获取NFC的小程序scheme](https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/url-scheme/api_generatenfcscheme.html)
> 所属分类：[小程序码与小程序链接](../../小程序码与小程序链接目录.md)
> 导航路径：小程序码与小程序链接 / URL Scheme / 获取NFC的小程序scheme
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：generateNFCScheme

该接口用于获取用于 NFC 的小程序 scheme 码，适用于 NFC 拉起小程序的业务场景。目前仅针对国内非个人主体的小程序开放，详见 [NFC 标签打开小程序](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/NFC.html)。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/generatenfcscheme?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：urlscheme.generateNFCScheme
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.jump_wxa Object Payload

跳转到的目标小程序信息。

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

# 调试

通过开发者工具的”快速 URL Schema编译“可以调试生成的 URL Schema


## 5. 代码示例

请求示例

```json
{
  "jump_wxa": {
    "path": "/pages/publishHomework/publishHomework",
    "query": ""
  },
  "sn": "xxx",
  "model_id": "xxx"
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

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
