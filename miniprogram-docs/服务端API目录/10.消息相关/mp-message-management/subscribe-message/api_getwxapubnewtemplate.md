# 获取已有模板列表

> 官方文档：[获取已有模板列表](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_getwxapubnewtemplate.html)
> 所属分类：[消息相关](../../消息相关目录.md)
> 导航路径：消息相关 / 订阅消息 / 获取已有模板列表
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getwxapubnewtemplate

该接口用于获取当前帐号下的已有的模板列表。

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/wxaapi/newtmpl/gettemplate?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：officialAccount.newtmpl.getTemplate
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18、89
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

无

## 3. 返回参数

### 返回体 Response Payload

### Res.data(Array) Object Payload

模板列表

### Res.data(Array).keywordEnumValueList Object Payload

枚举参数值范围

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

### 5.1 HTTPS请求示例

请求示例

```json
GET https://api.weixin.qq.com/wxaapi/newtmpl/gettemplate?access_token=ACCESS_TOKEN
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "priTmplId": "9Aw5ZV1j9xdWTFEkqCpZ7mIBbSC34khK55OtzUPl0rU",
      "title": "报名结果通知",
      "content": "会议时间:{{date2.DATA}}\n会议地点:{{thing1.DATA}}\n",
      "example": "会议时间:2016年8月8日\n会议地点:TIT会议室\n",
      "type": 2
    },
    {
      "priTmplId": "cy_DfOZL7lypxHh3ja3DyAUbn1GYQRGwezuy5LBTFME",
      "title": "洗衣机故障提醒",
      "content": "完成时间:{{time1.DATA}}\n所在位置:{{enum_string2.DATA}}\n提示说明:{{enum_string3.DATA}}\n",
      "example": "完成时间:2021年10月21日 12:00:00\n所在位置:客厅\n提示说明:设备发生故障，导致工作异常，请及时查看\n",
      "keywordEnumValueList": [
        {
          "enumValueList": [
            "客厅",
            "餐厅",
            "厨房",
            "卧室",
            "主卧",
            "次卧",
            "客卧",
            "父母房",
            "儿童房",
            "男孩房",
            "女孩房",
            "卫生间",
            "主卧卫生间",
            "公共卫生间",
            "衣帽间",
            "书房",
            "游戏室",
            "阳台",
            "地下室",
            "储物间",
            "车库",
            "保姆房",
            "其他房间"
          ],
          "keywordCode": "enum_string2.DATA"
        },
        {
          "enumValueList": [
            "设备发生故障，导致工作异常，请及时查看"
          ],
          "keywordCode": "enum_string3.DATA"
        }
      ],
      "type": 3
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
    const result = await cloud.openapi.subscribeMessage.getTemplateList({})
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
  "errMsg": "openapi.subscribeMessage.getTemplateList:ok",
  "data": [
    {
      "priTmplId": "9Aw5ZV1j9xdWTFEkqCpZ7mIBbSC34khK55OtzUPl0rU",
      "title": "报名结果通知",
      "content": "会议时间:{{date2.DATA}}\n会议地点:{{thing1.DATA}}\n",
      "example": "会议时间:2016年8月8日\n会议地点:TIT会议室\n",
      "type": 2
    },
    {
      "priTmplId": "cy_DfOZL7lypxHh3ja3DyAUbn1GYQRGwezuy5LBTFME",
      "title": "洗衣机故障提醒",
      "content": "完成时间:{{time1.DATA}}\n所在位置:{{enum_string2.DATA}}\n提示说明:{{enum_string3.DATA}}\n",
      "example": "完成时间:2021年10月21日 12:00:00\n所在位置:客厅\n提示说明:设备发生故障，导致工作异常，请及时查看\n",
      "keywordEnumValueList": [
        {
          "enumValueList": [
            "客厅",
            "餐厅",
            "厨房",
            "卧室",
            "主卧",
            "次卧",
            "客卧",
            "父母房",
            "儿童房",
            "男孩房",
            "女孩房",
            "卫生间",
            "主卧卫生间",
            "公共卫生间",
            "衣帽间",
            "书房",
            "游戏室",
            "阳台",
            "地下室",
            "储物间",
            "车库",
            "保姆房",
            "其他房间"
          ],
          "keywordCode": "enum_string2.DATA"
        },
        {
          "enumValueList": [
            "设备发生故障，导致工作异常，请及时查看"
          ],
          "keywordCode": "enum_string3.DATA"
        }
      ],
      "type": 3
    }
  ]
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

- ✔：该账号可调用此接口。
- 仅认证：表示仅允许企业主体已认证账号调用，未认证或不支持认证的账号无法调用。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
