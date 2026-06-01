# 营业执照识别

> 官方文档：[营业执照识别](https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/ocr/api_bizlicenseocr.html)
> 所属分类：[图像处理与文字识别](../../图像处理与文字识别目录.md)
> 导航路径：图像处理与文字识别 / OCR / 营业执照识别
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：bizlicenseOcr

本接口提供营业执照 OCR 识别能力

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cv/ocr/bizlicense?access_token=ACCESS_TOCKEN&img_url=ENCODE_URL
```

### 云调用

- 调用方法：ocr.businessLicense
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

### Res.cert_position Object Payload

营业执照位置

### Res.img_size Object Payload

图片大小

### Res.cert_position.pos Object Payload

位置信息

### Res.cert_position.pos.left_top Object Payload

左上角位置

### Res.cert_position.pos.right_top Object Payload

右上角位置

### Res.cert_position.pos.right_bottom Object Payload

右下角位置

### Res.cert_position.pos.left_bottom Object Payload

左下角位置

## 4. 注意事项

- 支持已认证的订阅号、服务号、企业号、小程序可直接调用，次数限制为100次/天。如有更高额度调用需求，可前往[服务平台](https://fuwu.weixin.qq.com/service/detail/000ce4cec24ca026d37900ed551415)进行购买。
- 使用 Tips 此接口为后台接口，可基于自有业务承载情况，搭配小程序的拍照、相册选照等一起使用，即可完成身份证照片的采集、上传、识别、信息返回等流程，用于需要基于身份证、银行卡等实体卡或证，采集照片或文字信息等的业务场景。
- 图片说明 ，文件大小限制：小于2M
- 返回字段仅包含当前营业执照图片中存在的字段，若对应字段不存在则不返回

## 5. 代码示例

### 5.1 上传文件请求

请求示例

```bash
curl -F 'img=@test.jpg' "https://api.weixin.qq.com/cv/ocr/bizlicense?access_token=ACCESS_TOCKEN" 
```

返回示例

```json
{
    "errcode": 0, 
    "errmsg": "ok", 
    "reg_num": "123123",//注册号
    "serial": "123123",//编号
    "legal_representative": "张三", //法定代表人姓名
    "enterprise_name": "XX饮食店", //企业名称
    "type_of_organization": "个人经营", //组成形式
    "address": "XX市XX区XX路XX号", //经营场所/企业住所
    "type_of_enterprise": "xxx", //公司类型
    "business_scope": "中型餐馆(不含凉菜、不含裱花蛋糕，不含生食海产品)。", //经营范围
    "registered_capital": "200万", //注册资本
    "paid_in_capital": "200万", //实收资本
    "valid_period": "2019年1月1日", //营业期限
    "registered_date": "2018年1月1日", //注册日期/成立日期
    "cert_position": { //营业执照位置
        "pos": {
            "left_top": {
                "x": 155, 
                "y": 191
            }, 
            "right_top": {
                "x": 725, 
                "y": 157
            }, 
            "right_bottom": {
                "x": 743, 
                "y": 512
            }, 
            "left_bottom": {
                "x": 164, 
                "y": 525
            }
        }
    }, 
    "img_size": { //图片大小
        "w": 966, 
        "h": 728
    }
}
```

### 5.2 上传链接请求

请求示例

```bash
curl "https://api.weixin.qq.com/cv/ocr/bizlicense?img_url=ENCODE_URL&access_token=ACCESS_TOCKEN"
```

返回示例

```json
{
    "errcode": 0, 
    "errmsg": "ok", 
    "reg_num": "123123",//注册号
    "serial": "123123",//编号
    "legal_representative": "张三", //法定代表人姓名
    "enterprise_name": "XX饮食店", //企业名称
    "type_of_organization": "个人经营", //组成形式
    "address": "XX市XX区XX路XX号", //经营场所/企业住所
    "type_of_enterprise": "xxx", //公司类型
    "business_scope": "中型餐馆(不含凉菜、不含裱花蛋糕，不含生食海产品)。", //经营范围
    "registered_capital": "200万", //注册资本
    "paid_in_capital": "200万", //实收资本
    "valid_period": "2019年1月1日", //营业期限
    "registered_date": "2018年1月1日", //注册日期/成立日期
    "cert_position": { //营业执照位置
        "pos": {
            "left_top": {
                "x": 155, 
                "y": 191
            }, 
            "right_top": {
                "x": 725, 
                "y": 157
            }, 
            "right_bottom": {
                "x": 743, 
                "y": 512
            }, 
            "left_bottom": {
                "x": 164, 
                "y": 525
            }
        }
    }, 
    "img_size": { //图片大小
        "w": 966, 
        "h": 728
    }
}
```

### 5.3 云函数调用示例

请求示例

```js
cloud.openapi.ocr.businessLicense({
  img: {
    contentType: 'image/png',
    value: Buffer
  }
})
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "reg_num": "123123",                                                     //注册号
    "serial": "123123",                                                      //编号
    "legalRepresentative": "张三",                                          //法定代表人姓名
    "enterprise_name": "XX饮食店",                                           //企业名称
    "typeOfOrganization": "个人经营",                                      //组成形式
    "address": "XX市XX区XX路XX号",                                           //经营场所/企业住所
    "typeOfEnterprise": "xxx",                                             //公司类型
    "businessScope": "中型餐馆(不含凉菜、不含裱花蛋糕，不含生食海产品)。",  //经营范围
    "registeredCapital": "200万",                                           //注册资本
    "paidInCapital": "200万",                                              //实收资本
    "validPeriod": "2019年1月1日",                                          //营业期限
    "registeredDate": "2018年1月1日",                                       //注册日期/成立日期
    "certPosition": {                                                       //营业执照位置
        "pos": {
            "left_top": {
                "x": 155,
                "y": 191
            },
            "right_top": {
                "x": 725,
                "y": 157
            },
            "right_bottom": {
                "x": 743,
                "y": 512
            },
            "left_bottom": {
                "x": 164,
                "y": 525
            }
        }
    },
    "imgSize": { //图片大小
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
