# 驾驶证识别

> 官方文档：[驾驶证识别](https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/ocr/api_drivinglicenseocr.html)
> 所属分类：[图像处理与文字识别](../../图像处理与文字识别目录.md)
> 导航路径：图像处理与文字识别 / OCR / 驾驶证识别
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：drivinglicenseocr

本接口用于驾驶证识别

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cv/ocr/drivinglicense?access_token=ACCESS_TOCKEN&img_url=ENCODE_URL
```

### 云调用

- 调用方法：ocr.driverLicense
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

## 4. 注意事项

- 支持已认证的订阅号、服务号、企业号、小程序可直接调用，次数限制为100次/天。
- 使用 Tips 此接口为后台接口，可基于自有业务承载情况，搭配小程序的拍照、相册选照等一起使用，即可完成身份证照片的采集、上传、识别、信息返回等流程，用于需要基于身份证、银行卡等实体卡或证，采集照片或文字信息等的业务场景。
- 图片说明 ，文件大小限制：小于2M
- 图片支持使用img参数实时上传，也支持使用img_url参数传送图片地址，由微信后台下载图片进行识别。type 有两种类型

## 5. 代码示例

### 5.1 上传文件请求

请求示例

```bash
curl -F 'img=@test.jpg' 'https://api.weixin.qq.com/cv/ocr/drivinglicense?access_token=ACCESS_TOCKEN'
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "id_num": "660601xxxxxxxx1234", //证号
    "name": "张三", //姓名
    "sex": "男", //性别
    "nationality": "中国", //国籍
    "address": "广东省东莞市xxxxx号", //住址
    "birth_date": "1990-12-21", //出生日期
    "issue_date": "2012-12-21", //初次领证日期
    "car_class": "C1", //准驾车型
    "valid_from": "2018-07-06", //有效期限起始日
    "valid_to": "2020-07-01", //有效期限终止日
    "official_seal": "xx市公安局公安交通管理局" //印章文字
}
```

### 5.2 上传链接请求

请求示例

```bash
curl https://api.weixin.qq.com/cv/ocr/drivinglicense?img_url=ENCODE_URL&access_token=ACCESS_TOCKEN
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "id_num": "660601xxxxxxxx1234", //证号
    "name": "张三", //姓名
    "sex": "男", //性别
    "nationality": "中国", //国籍
    "address": "广东省东莞市xxxxx号", //住址
    "birth_date": "1990-12-21", //出生日期
    "issue_date": "2012-12-21", //初次领证日期
    "car_class": "C1", //准驾车型
    "valid_from": "2018-07-06", //有效期限起始日
    "valid_to": "2020-07-01", //有效期限终止日
    "official_seal": "xx市公安局公安交通管理局" //印章文字
}
```

### 5.3 云函数调用示例

请求示例

```js
const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
})
exports.main = async (event, context) => {
  try {
    const result = await cloud.openapi.ocr.driverLicense({
        "type": 'photo',
        "imgUrl": 'ENCODE_URL'
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
  "id_num": "660601xxxxxxxx1234",
  "name": "张三",
  "sex": "男",
  "nationality": "中国",
  "address": "广东省东莞市xxxxx号",
  "birthDate": "1990-12-21",
  "issueDate": "2012-12-21",
  "carClass": "C1",
  "validFrom": "2018-07-06",
  "validTo": "2020-07-01",
  "officialSeal": "xx市公安局公安交通管理局"
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
