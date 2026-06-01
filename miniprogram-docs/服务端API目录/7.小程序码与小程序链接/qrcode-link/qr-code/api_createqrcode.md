# 获取小程序二维码

> 官方文档：[获取小程序二维码](https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/qr-code/api_createqrcode.html)
> 所属分类：[小程序码与小程序链接](../../小程序码与小程序链接目录.md)
> 导航路径：小程序码与小程序链接 / 小程序码 / 获取小程序二维码
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：createQRCode

获取小程序二维码，适用于需要的码数量较少的业务场景。通过该接口生成的小程序码，永久有效，有数量限制，详见[获取二维码](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/qr-code.html)。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/wxaapp/createwxaqrcode?access_token=ACCESS_TOKEN
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 调用方法：wxacode.createQRCode
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：17
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

- 如果调用成功，会直接返回图片二进制内容，如果请求失败，会返回 JSON 格式的数据。
- POST 参数需要转成 JSON 字符串，不支持 form 表单提交。
- 接口只能生成已发布的小程序的二维码。开发版的带参二维码可以在开发者工具预览时生成。
- 与 [wxacode.get](https://developers.weixin.qq.com/doc/channels/API/funds/qrcode/get.html) 总共生成的码数量限制为 100,000，请谨慎调用。

## 5. 代码示例

### 5.1 HTTP调用示例（成功）

请求示例

```json
{
  "path": "page/index/index",
  "width": 430
}
```

返回示例

```text
图片 Buffer
```

### 5.2 HTTP调用示例（失败）

请求示例

```json
{
  "path": "",
  "width": 430
}
```

返回示例

```json
{
  "errcode": 40159,
  "errmsg": "invalid length for path  or thedata is not json string"
}
```

### 5.3 云调用示例（成功）

请求示例

```json
const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
})
exports.main = async (event, context) => {
  try {
    const result = await cloud.openapi.wxacode.createQRCode({
        "path": 'page/index/index',
        "width": 430
      })
    return result
  } catch (err) {
    return err
  }
}
```

返回示例

```text
图片 Buffer
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

- ✔：该账号可调用此接口。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
