# 批处理短剧合作推广计划

> 官方文档：[批处理短剧合作推广计划](https://developers.weixin.qq.com/miniprogram/dev/server/API/dramaOthersAPI/api_batchprocessdramapromotion.html)
> 所属分类：[短剧播放器](../短剧播放器目录.md)
> 导航路径：短剧播放器 / 批处理短剧合作推广计划
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：batchProcessDramaPromotion

- 开发者注意：使用该接口前请阅读并同意[《微信小程序平台短剧推广计划合作协议》](https://developers.weixin.qq.com/miniprogram/product/duanju.html)；你以任何方式使用该接口，即视为你确认同意[《微信小程序平台短剧推广计划合作协议》](https://developers.weixin.qq.com/miniprogram/product/duanju.html)，自愿遵守包括但不限于剧目授权、收益分成、责任承担等所有条款约定，如你不同意，请不要使用本接口。
- 使用接口设置后，可批量将剧目加入/退出短剧推广计划中。 开发者确认并同意，通过本接口设置将短剧加入推广合作计划中，即视为你按照[《微信小程序平台短剧推广计划合作协议》](https://developers.weixin.qq.com/miniprogram/product/duanju.html)的约定主动合作推广并向腾讯授予该剧目的相关权利。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxadrama/batchprocessdramapromotion?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：157
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.list(Array) Object Payload

短剧数组

## 3. 返回参数

### 返回体 Response Payload

### Res.list(Array) Object Payload

短剧数组

## 4. 注意事项

1. 该接口必须由剧目提审时的小程序调用，即access_token对应的小程序appid必须等于src_appid。
2. 每次批量加入短剧最大数目限制为100。
3. 短剧需要满足码率大于0.5Mbps，分辨率大于720。
4. 若加入计划时存在不符合条件的短剧，会使本次请求所有短剧加入失败。开发者可以通过批查询action_type=2查询短剧状态。

## 5. 代码示例

### 5.1 加入/退出计划请求示例

请求示例

此处仅以加入计划为例，如需退出计划可修改action_type为3。

```json
{
   "action_type": 1,
   "list": [
           {"src_appid":"example_src_appid", "drama_id":"123456"},
           {"src_appid":"example_src_appid", "drama_id":"123457"}
     ]
}
```

返回示例

```json
{
    "errcode":0,
    "errmsg":"ok"
}

{ //加入计划时，若分辨率或码率不满足条件
    "errcode":106017,
    "errmsg":"分辨率不足或码率不足"
}

{ //加入计划时，若授权库中已存在同内容短剧
    "errcode":106018,
    "errmsg":"官方授权库中已存在相同内容的短剧,请勿重复授权"
}
```

### 5.2 查询计划请求示例

请求示例

```json
{
   "action_type": 2,
   "list": [
           {"src_appid":"example_src_appid", "drama_id":"123456"},
           {"src_appid":"example_src_appid", "drama_id":"123457"}
     ]
}
```

返回示例

```json
{
   "list": [
           {"src_appid":"example_src_appid", "drama_id":"123456", "status": 0 },
           {"src_appid":"example_src_appid", "drama_id":"123457", "status": 1 }
     ],
    "errcode":0,
    "errmsg":"ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
