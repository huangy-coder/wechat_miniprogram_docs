# 获取不限制的小程序码

> 官方文档：[获取不限制的小程序码](https://developers.weixin.qq.com/miniprogram/dev/server/API/qrcode-link/qr-code/api_getunlimitedqrcode.html)
> 所属分类：[小程序码与小程序链接](../../小程序码与小程序链接目录.md)
> 导航路径：小程序码与小程序链接 / 小程序码 / 获取不限制的小程序码
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getUnlimitedQRCode

该接口用于获取小程序码，适用于需要的码数量极多的业务场景。通过该接口生成的小程序码，永久有效，数量暂无限制。 更多用法详见 [获取小程序码](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/qr-code.html)。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=ACCESS_TOKEN
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 调用方法：wxacode.getUnlimited
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：17
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.line_color Object Payload

默认是{"r":0,"g":0,"b":0} 。auto_color 为 false 时生效，使用 rgb 设置颜色 例如 {"r":"xxx","g":"xxx","b":"xxx"} 十进制表示

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

- 如果调用成功，会直接返回图片二进制内容，如果请求失败，会返回 JSON 格式的数据。
- POST 参数需要转成 JSON 字符串，不支持 form 表单提交。
- 调用分钟频率受限（5000次/分钟），如需大量小程序码，建议预生成

#### 获取 scene 值

- scene 字段的值会作为 query 参数传递给小程序/小游戏。用户扫描该码进入小程序/小游戏后，开发者可以获取到二维码中的 scene 值，再做处理逻辑。
- 调试阶段可以使用开发工具的条件编译自定义参数 scene=xxxx 进行模拟，开发工具模拟时的 scene 的参数值需要进行 encodeURIComponent

##### 小程序

```json
Page({
  onLoad (query) {
    // scene 需要使用 decodeURIComponent 才能获取到生成二维码时传入的 scene
    const scene = decodeURIComponent(query.scene)
  }
})
```

##### 小游戏

```json
// 在首次启动时通过 wx.getLaunchOptionsSync 接口获取
const {query} = wx.getLaunchOptionsSync()
const scene = decodeURIComponent(query.scene)

// 或者在 wx.onShow 事件中获取
wx.onShow(function ({query}) {
  // scene 需要使用 decodeURIComponent 才能获取到生成二维码时传入的 scene
  const scene = decodeURIComponent(query.scene)
})
```

## 5. 代码示例

### 5.1 HTTP调用示例（成功）

请求示例

```json
{
  "page": "pages/index/index",
  "scene": "a=1",
  "check_path": true,
  "env_version": "release"
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
  "page": "pages/index/index",
  "scene": "a=1",
  "check_path": true,
  "env_version": "release_error"
}
```

返回示例

```json
{
  "errcode": 40097,
  "errmsg": "invalid args"
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
    const result = await cloud.openapi.wxacode.getUnlimited({
        "page": 'pages/index/index',
        "scene": 'a=1',
        "checkPath": true,
        "envVersion": 'release'
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
