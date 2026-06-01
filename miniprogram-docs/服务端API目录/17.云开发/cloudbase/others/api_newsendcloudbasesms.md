# 发送短信v2

> 官方文档：[发送短信v2](https://developers.weixin.qq.com/miniprogram/dev/server/API/cloudbase/others/api_newsendcloudbasesms.html)
> 所属分类：[云开发](../../云开发目录.md)
> 导航路径：云开发 / 其他 / 发送短信v2
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：newSendCloudBaseSms

发送携带 URL Link 的短信

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/tcb/sendsmsv2?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：cloudbase.sendSmsV2
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：49、99
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.send_status_list(Array) Object Payload

开放数据列表

## 4. 注意事项

**短信内容**

短信由签名和正文内容组成：

短信签名是位于短信正文前【】中的署名，小程序发送短信时，签名为小程序名称。

- 正文内容是由短信模板和变量构成，例：{1}，跳转小程序 {2} 回T退订，模板参数中 {1}，{2} 是变量：
- {1} ：用户可自定义传入的内容，当前最长为30个字。
- {2} ：用户传入的 URL Link，例如 https://wxmpurl.cn/tN5huKl2Gwg
示例：【云开发】能力上新，跳转小程序 https://wxmpurl.cn/tN5huKl2Gwg 回T退订

**短信资源包**

前往“开发者工具-云开发-设置-环境设置-资源包”中购买。

**第三方代开发说明**

小程序需要将【短信服务】或【云开发】权限集授权给第三方，第三方才可代小程序调用此接口。第三方在调用接口时，可选择使用第三方的环境或小程序的环境，默认使用小程序的环境。在resource_appid填入第三方的appid，在env填入第三方账号下的环境，即可使用第三方的环境。

**模版ID**

云开发短信模版 ID，填写 2053122，即为当前统一的跳转小程序短信模板。非营销类内容，需要24小时触达，可走通知类短信，当前内测中，可通过提交工单进行申请。例如:【腾讯电子签】您有一份已完成的收据，请登录“腾讯电子签”小程序查看详情。 https://tcbe.cn/9a3vCqlK 工单链接：https://developers.weixin.qq.com/miniprogram/dev/wxcloud/guide/operations/ticket.html

## 5. 代码示例

### 5.1 HTTPS请求示例

请求示例

```json
{
  "env": "online-12345678910",
  "url_link": "https://wxaurl.cn/xxxxxx",
  "template_id": "844110",
  "template_param_list": [
    "能力上新"
  ],
  "phone_number_list": [
    "+8612345678910"
  ]
}
```

返回示例

```json
{
  "errcode": 0,
  "send_status_list": [
    {
      "serial_no": "8:gFIqWUHzllUyOFRHgeu20201231",
      "phone_number": "+8612345678910",
      "code": "Ok",
      "message": "send success",
      "iso_code": ""
    }
  ]
}
```

### 5.2 云函数调用示例

请求示例

```js
const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
})
exports.main = async (event, context) => {
  try {
    const result = await cloud.openapi.cloudbase.sendSmsV2({
        "env": 'online-12345678910',
        "urlLink": 'https://wxaurl.cn/xxxxxx',
        "templateId": '844110',
        "templateParamList": [
          "能力上新"
        ],
        "phoneNumberList": [
          "+8612345678910"
        ]
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
  "errCode": 0,
  "sendStatusList": [
    {
      "code": "Ok",
      "message": "send success",
      "serialNo": "8:gFIqWUHzllUyOFRHgeu20201231",
      "phoneNumber": "+8612345678910",
      "isoCode": ""
    }
  ],
  "errMsg": "openapi.cloudbase.sendSmsV2:ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

- ✔：该账号可调用此接口。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
