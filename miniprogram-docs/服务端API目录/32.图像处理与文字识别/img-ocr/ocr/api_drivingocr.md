# 行驶证识别

> 官方文档：[行驶证识别](https://developers.weixin.qq.com/miniprogram/dev/server/API/img-ocr/ocr/api_drivingocr.html)
> 所属分类：[图像处理与文字识别](../../图像处理与文字识别目录.md)
> 导航路径：图像处理与文字识别 / OCR / 行驶证识别
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：drivingocr

提供机动车行驶证信息OCR识别

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cv/ocr/driving?access_token=ACCESS_TOCKEN&img_url=ENCODE_URL
```

### 云调用

- 调用方法：ocr.drivingLicense
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

- 支持已认证的订阅号、服务号、企业号、小程序可直接调用，次数限制为100次/天。如有更高额度调用需求，可前往[服务平台](https://fuwu.weixin.qq.com/service/detail/000ce4cec24ca026d37900ed551415)进行购买。
- 使用 Tips 此接口为后台接口，可基于自有业务承载情况，搭配小程序的拍照、相册选照等一起使用，即可完成照片的采集、上传、识别、信息返回等流程，用于需要基于身份证、银行卡等实体卡或证，采集照片或文字信息等的业务场景。
- 图片说明 文件大小限制：小于2M
- 图片支持使用img参数实时上传，也支持使用img_url参数传送图片地址，由微信后台下载图片进行识别。type 有两种类型

## 5. 代码示例

### 5.1 上传文件请求

请求示例

```bash
curl -F 'img=@test.jpg' "https://api.weixin.qq.com/cv/ocr/driving?access_token=ACCESS_TOCKEN"
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "plate_num": "粤xxxxx", //车牌号码
    "vehicle_type": "小型普通客车", //车辆类型
    "owner": "东莞市xxxxx机械厂", //所有人
    "addr": "广东省东莞市xxxxx号", //住址
    "use_character": "非营运", //使用性质
    "model": "江淮牌HFCxxxxxxx", //品牌型号
    "vin": "LJ166xxxxxxxx51", //车辆识别代号
    "engine_num": "J3xxxxx3", //发动机号码
    "register_date": "2018-07-06", //注册日期
    "issue_date": "2018-07-01", //发证日期
    "plate_num_b": "粤xxxxx", //车牌号码
    "record": "441xxxxxx3", //号牌
    "passengers_num": "7人", //核定载人数
    "total_quality": "2700kg", //总质量
    "prepare_quality": "1995kg" //整备质量,
    "overall_size": "4582x1795x1458mm" //外廓尺寸,
    "card_position_front": {//卡片正面位置（检测到卡片正面才会返回）
        "pos": {
            "left_top": {
                "x": 119, 
                "y": 2925
            }, 
            "right_top": {
                "x": 1435, 
                "y": 2887
            }, 
            "right_bottom": {
                "x": 1435, 
                "y": 3793
            }, 
            "left_bottom": {
                "x": 119, 
                "y": 3831
            }
        }
    }, 
    "card_position_back": {//卡片反面位置（检测到卡片反面才会返回）
        "pos": {
            "left_top": {
                "x": 1523, 
                "y": 2849
            }, 
            "right_top": {
                "x": 2898, 
                "y": 2887
            }, 
            "right_bottom": {
                "x": 2927, 
                "y": 3831
            }, 
            "left_bottom": {
                "x": 1523, 
                "y": 3831
            }
        }
    }, 
    "img_size": {//图片大小
        "w": 3120, 
        "h": 4208
    }
}
```

### 5.2 上传链接请求

请求示例

```bash
curl https://api.weixin.qq.com/cv/ocr/driving?img_url=ENCODE_URL&access_token=ACCESS_TOCKEN
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "plate_num": "粤xxxxx", //车牌号码
    "vehicle_type": "小型普通客车", //车辆类型
    "owner": "东莞市xxxxx机械厂", //所有人
    "addr": "广东省东莞市xxxxx号", //住址
    "use_character": "非营运", //使用性质
    "model": "江淮牌HFCxxxxxxx", //品牌型号
    "vin": "LJ166xxxxxxxx51", //车辆识别代号
    "engine_num": "J3xxxxx3", //发动机号码
    "register_date": "2018-07-06", //注册日期
    "issue_date": "2018-07-01", //发证日期
    "plate_num_b": "粤xxxxx", //车牌号码
    "record": "441xxxxxx3", //号牌
    "passengers_num": "7人", //核定载人数
    "total_quality": "2700kg", //总质量
    "prepare_quality": "1995kg" //整备质量,
    "overall_size": "4582x1795x1458mm" //外廓尺寸,
    "card_position_front": {//卡片正面位置（检测到卡片正面才会返回）
        "pos": {
            "left_top": {
                "x": 119, 
                "y": 2925
            }, 
            "right_top": {
                "x": 1435, 
                "y": 2887
            }, 
            "right_bottom": {
                "x": 1435, 
                "y": 3793
            }, 
            "left_bottom": {
                "x": 119, 
                "y": 3831
            }
        }
    }, 
    "card_position_back": {//卡片反面位置（检测到卡片反面才会返回）
        "pos": {
            "left_top": {
                "x": 1523, 
                "y": 2849
            }, 
            "right_top": {
                "x": 2898, 
                "y": 2887
            }, 
            "right_bottom": {
                "x": 2927, 
                "y": 3831
            }, 
            "left_bottom": {
                "x": 1523, 
                "y": 3831
            }
        }
    }, 
    "img_size": {//图片大小
        "w": 3120, 
        "h": 4208
    }
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
    const result = await cloud.openapi.ocr.vehicleLicense({
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
  "vehicleType": "小型普通客⻋",
  "owner": "东莞市xxxxx机械厂",
  "addr": "广东省东莞市xxxxx号",
  "useCharacter": "非营运",
  "model": "江淮牌HFCxxxxxxx",
  "vin": "LJ166xxxxxxxx51",
  "engineNum": "J3xxxxx3",
  "registerDate": "2018-07-06",
  "issueDate": "2018-07-01",
  "plateNumB": "粤xxxxx",
  "record": "441xxxxxx3",
  "passengersNum": "7人",
  "totalQuality": "2700kg",
  "prepareQuality": "1995kg"
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
