# 获取短剧合作推广活动

> 官方文档：[获取短剧合作推广活动](https://developers.weixin.qq.com/miniprogram/dev/server/API/dramaOthersAPI/api_getfinderevent.html)
> 所属分类：[短剧播放器](../短剧播放器目录.md)
> 导航路径：短剧播放器 / 获取短剧合作推广活动
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getFinderEvent

该接口可获取当前小程序短剧所关联的短剧合作推广活动。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxadrama/getfinderevent?access_token=ACCESS_TOKEN
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

## 3. 返回参数

### 返回体 Response Payload

### Res.finder_event_list(Array) Object Payload

推广计划数组

## 4. 注意事项

1. 批量获取小程序提交审核的所有关联小程序短剧的推广活动
2. 批量获取小程序可播放短剧的推广活动，无法获取该短剧其他可播放小程序的推广活动
3. 传入event_id_list用于筛选指定event_id的推广活动，最大数量限制为50

## 5. 代码示例

请求示例

```json
{
   "event_id_list": [] //为空时全量读取
}
```

返回示例

```json
{
    "finder_event_list": [
        {
            "encrypted_event_id": "event/id",
            "event_name": "《示例短剧》示例小程序",
            "event_url": "https://channels.weixin.qq.com/mobile/toNativeActivity.html?title=&topicType=&eventEncryptedTopicId=&authorNickname=",
            "src_appid": "wx",
            "drama_id": "10000"
        }
    ],
    "errcode": 0,
    "errmsg": "ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
