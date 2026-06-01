# 图片智能裁剪

> 官方文档：[图片智能裁剪](https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/img/api_imgaicrop.html)
> 所属分类：[图像处理与文字识别](../../图像处理与文字识别目录.md)
> 导航路径：图像处理与文字识别 / 图像处理 / 图片智能裁剪
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：imgAiCrop

本接口用于对图片主体区域进行智能识别和裁剪

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cv/img/aicrop?access_token=ACCESS_TOCKEN&img_url=ENCODE_URL
```

### 云调用

- 调用方法：img.aiCrop
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

### Res.results(Array) Object Payload

智能裁剪结果

### Res.img_size Object Payload

图片大小

## 4. 注意事项

1. 支持使用img参数实时上传，也支持使用img_url参数传送图片地址，由微信后台下载图片进行识别。
2. ratios参数为可选，如果为空，则算法自动裁剪最佳宽高比；如果提供多个宽高比，请以英文逗号“,”分隔，最多支持5个宽高比
3. 文件大小限制：小于2M 图片

## 5. 代码示例

### 5.1 上传文件请求

请求示例

```bash
curl -F 'img=@test.jpg' -F 'ratios=1,2.35' 'http://api.weixin.qq.com/cv/img/aicrop?access_token=ACCESS_TOCKEN'
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "results": [
    {
      "crop_left": 112,
      "crop_top": 0,
      "crop_right": 839,
      "crop_bottom": 727
    },
    {
       "crop_left": 0,
       "crop_top": 205,
       "crop_right": 965,
       "crop_bottom": 615
   }
  ],
  "img_size": {
    "w": 966,
    "h": 728
  }
}
```

### 5.2 上传链接请求

请求示例

```bash
curl -F 'ratios=1,2.35' "http://api.weixin.qq.com/cv/img/aicrop?img_url=ENCODE_URL&access_token=ACCESS_TOCKEN"
```

返回示例

```json
{
    "errcode": 0, 
    "errmsg": "ok", 
    "results": [ //智能裁剪结果
        {
            "crop_left": 112, 
            "crop_top": 0, 
            "crop_right": 839, 
            "crop_bottom": 727
        }, 
        {
            "crop_left": 0, 
            "crop_top": 205, 
            "crop_right": 965, 
            "crop_bottom": 615
        }
    ], 
    "img_size": { //图片大小
        "w": 966, 
        "h": 728
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
