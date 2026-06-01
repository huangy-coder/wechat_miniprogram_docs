# 消息推送接口

> 官方文档：[消息推送接口](https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/medicalassistant/api_cityservice_sendchannelmsg.html)
> 所属分类：[城市服务](../../城市服务目录.md)
> 导航路径：城市服务 / 微信就医助手 / 消息推送接口
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：cityservice_sendchannelmsg

用于下发就医助手消息，结合通用参数和不同子状态status参数组合实现各类业务消息推送，要获取所有status参数，请查看[微信就医助手开发文档](https://docs.qq.com/doc/DQXRyQURVdHJsaGJy)。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cityservice/sendchannelmsg?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：22、105、113、134
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.business_info Object Payload

业务字段(不同status对应不同结构)

### Body.business_info.redirect_page Object Payload

医院跳转页面信息

> 以下参数也使用此结构：

> - Body.business_info.elder_redirect_page ： 医院适老化页面的跳转信息

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Body.business_info.redirect_page.page_type Enum

页面路径类型，如果有redirect_page字段需要填，则必填page_type; 否则不用填

## 5. 注意事项

1. 仅支持公立医院及卫健委主体的公众号/小程序使用
2. 需先开通就医助手能力
3. 需使用同主体公众号的access_token调用
4. 同次就医流程需使用相同order_id

## 6. 代码示例

请求示例

```json
{
  "status": 1501001,
  "open_id": "osdjkfhsdlkfjhdslkjfh",
  "order_id": "order_123456",
  "msg_id": "msg_0001",
  "app_id": "wx23dde3xd34569cba",
  "business_id": 150,
  "business_info": {
    "pat_name": "李*龙",
    "doc_name": "王小二",
    "pat_hospital_id": "a123456",
    "department_name": "门诊3楼五官科",
    "appointment_time": "2023-06-07 10:30-11:00",
    "redirect_page": {
      "page_type": "web",
      "url": "https:zhongshanyi.com/guahao?order_id=order1"
    }
  }
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
