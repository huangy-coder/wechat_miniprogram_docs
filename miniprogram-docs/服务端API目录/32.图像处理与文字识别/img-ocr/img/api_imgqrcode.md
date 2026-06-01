# 二维码/条码识别

> 官方文档：[二维码/条码识别](https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/img/api_imgqrcode.html)
> 所属分类：[图像处理与文字识别](../../图像处理与文字识别目录.md)
> 导航路径：图像处理与文字识别 / 图像处理 / 二维码/条码识别
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：imgQrcode

识别图片中的二维码、条码、DataMatrix和PDF417

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cv/img/qrcode?access_token=ACCESS_TOKEN&img_url=https://example.com/img.jpg
```

### 云调用

- 调用方法：img.scanQRCode
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：117
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.code_results(Array) Object Payload

处理结果

### Res.img_size Object Payload

图片大小

### Res.code_results(Array).pos Object Payload

码的坐标

### Res.code_results(Array).pos.left_top Object Payload

左上角位置

### Res.code_results(Array).pos.right_top Object Payload

右上角位置

### Res.code_results(Array).pos.right_bottom Object Payload

右下角位置

### Res.code_results(Array).pos.left_bottom Object Payload

左下角位置

## 4. 注意事项

1. 图片支持使用img参数实时上传，也支持使用img_url参数传送图片地址，由微信后台下载图片进行识别
2. 文件需小于2MB
3. 支持条码、二维码、DataMatrix和PDF417的识别。
4. 二维码、DataMatrix会返回位置坐标，条码和PDF417暂不返回位置坐标。

## 5. 代码示例

### 5.1 文件链接请求

请求示例

```json
curl 'https://api.weixin.qq.com/cv/img/qrcode?img_url=ENCODE_URL&access_token=ACCESS_TOCKEN'
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "code_results": [
    {
      "type_name": "QR_CODE",
      "data": "https://www.qq.com",
      "pos": {
        "left_top": {
          "x": 585,
          "y": 378
        },
        "right_top": {
          "x": 828,
          "y": 378
        },
        "right_bottom": {
          "x": 828,
          "y": 618
        },
        "left_bottom": {
          "x": 585,
          "y": 618
        }
      }
    }
  ],
  "img_size": {
    "w": 1000,
    "h": 900
  }
}
```

### 5.2 文件上传请求

请求示例

```bash
curl -F 'img=@test.jpg' 'https://api.weixin.qq.com/cv/img/qrcode?access_token=ACCESS_TOCKEN'
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "code_results": [
    {
      "type_name": "QR_CODE",
      "data": "https://www.qq.com",
      "pos": {
        "left_top": {
          "x": 585,
          "y": 378
        },
        "right_top": {
          "x": 828,
          "y": 378
        },
        "right_bottom": {
          "x": 828,
          "y": 618
        },
        "left_bottom": {
          "x": 585,
          "y": 618
        }
      }
    }
  ],
  "img_size": {
    "w": 1000,
    "h": 900
  }
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

| 小程序 | 公众号 | 服务号 |
| --- | --- | --- |
| ✔ | 仅认证 | 仅认证 |

- ✔：该账号可调用此接口。
- 仅认证：表示仅允许企业主体已认证账号调用，未认证或不支持认证的账号无法调用。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
