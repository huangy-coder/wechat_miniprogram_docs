# 通用印刷体识别

> 官方文档：[通用印刷体识别](https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/ocr/api_commocr.html)
> 所属分类：[图像处理与文字识别](../../图像处理与文字识别目录.md)
> 导航路径：图像处理与文字识别 / OCR / 通用印刷体识别
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：commocr

本接口用于识别通用印刷体

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cv/ocr/comm?access_token=ACCESS_TOCKEN&img_url=ENCODE_URL
```

### 云调用

- 调用方法：ocr.printedText
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

### Res.items(Array) Object Payload

识别结果

### Res.img_size Object Payload

图片大小

### Res.items(Array).pos Object Payload

位置信息

### Res.items(Array).pos.left_top Object Payload

左上角位置

### Res.items(Array).pos.right_top Object Payload

右上角位置

### Res.items(Array).pos.right_bottom Object Payload

右下角位置

### Res.items(Array).pos.left_bottom Object Payload

左下角位置

## 4. 注意事项

- 支持已认证的订阅号、服务号、企业号、小程序可直接调用，次数限制为100次/天。如有更高额度调用需求，可前往[服务平台](https://fuwu.weixin.qq.com/service/detail/000ce4cec24ca026d37900ed551415)进行购买。
- 使用 Tips 此接口为后台接口，可基于自有业务承载情况，搭配小程序的拍照、相册选照等一起使用，即可完成身份证照片的采集、上传、识别、信息返回等流程，用于需要基于身份证、银行卡等实体卡或证，采集照片或文字信息等的业务场景。
- 图片说明 文件大小限制：小于2M
- 图片支持使用img参数实时上传，也支持使用img_url参数传送图片地址，由微信后台下载图片进行识别。type 有两种类型

## 5. 代码示例

### 5.1 上传文件请求

请求示例

```bash
curl -F 'img=@test.jpg' "https://api.weixin.qq.com/cv/ocr/comm?access_token=ACCESS_TOCKEN" 
```

返回示例

```json
{
    "errcode": 0, 
    "errmsg": "ok", 
    "items": [ //识别结果
        {
            "text": "腾讯", 
            "pos": {
                "left_top": {
                    "x": 575, 
                    "y": 519
                }, 
                "right_top": {
                    "x": 744, 
                    "y": 519
                }, 
                "right_bottom": {
                    "x": 744, 
                    "y": 532
                }, 
                "left_bottom": {
                    "x": 573, 
                    "y": 532
                }
            }
        }, 
        {
            "text": "微信团队", 
            "pos": {
                "left_top": {
                    "x": 670, 
                    "y": 516
                }, 
                "right_top": {
                    "x": 762, 
                    "y": 517
                }, 
                "right_bottom": {
                    "x": 762, 
                    "y": 532
                }, 
                "left_bottom": {
                    "x": 670, 
                    "y": 531
                }
            }
        }
    ], 
    "img_size": { //图片大小
        "w": 1280, 
        "h": 720
    }
}
```

### 5.2 上传链接请求

请求示例

```bash
curl "https://api.weixin.qq.com/cv/ocr/comm?img_url=ENCODE_URL&access_token=ACCESS_TOCKEN"
```

返回示例

```json
{
    "errcode": 0, 
    "errmsg": "ok", 
    "items": [ //识别结果
        {
            "text": "腾讯", 
            "pos": {
                "left_top": {
                    "x": 575, 
                    "y": 519
                }, 
                "right_top": {
                    "x": 744, 
                    "y": 519
                }, 
                "right_bottom": {
                    "x": 744, 
                    "y": 532
                }, 
                "left_bottom": {
                    "x": 573, 
                    "y": 532
                }
            }
        }, 
        {
            "text": "微信团队", 
            "pos": {
                "left_top": {
                    "x": 670, 
                    "y": 516
                }, 
                "right_top": {
                    "x": 762, 
                    "y": 517
                }, 
                "right_bottom": {
                    "x": 762, 
                    "y": 532
                }, 
                "left_bottom": {
                    "x": 670, 
                    "y": 531
                }
            }
        }
    ], 
    "img_size": { //图片大小
        "w": 1280, 
        "h": 720
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
