# 编辑直播间

> 官方文档：[编辑直播间](https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_editroom.html)
> 所属分类：[小程序直播](../../小程序直播目录.md)
> 导航路径：小程序直播 / 直播间管理 / 编辑直播间
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：editRoom

该接口用于编辑直播间

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxaapi/broadcast/room/editroom?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：liveBroadcast.editRoom
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：52
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

调用额度：10000次/一天

## 5. 代码示例

请求示例

```json
{
  "id": 811,
  "name": "测试更新副号1",
  "coverImg": "hw7zsntcr0rE-RBfBAaF553DqBk-J02UtWsP8VqrUh3tKu3jO_JwEO8n1cWTJ5TN",
  "startTime": 1607443200,
  "endTime": 1607450400,
  "anchorName": "主播昵称11",
  "anchorWechat": "lintest1",
  "shareImg": "hw7zsntcr0rE-RBfBAaF553DqBk-J02UtWsP8VqrUh3tKu3jO_JwEO8n1cWTJ5TN",
  "closeLike": 0,
  "closeGoods": 0,
  "closeComment": 0,
  "isFeedsPublic": 0,
  "closeReplay": 0,
  "closeShare": 0,
  "closeKf": 0,
  "feedsImg": "hw7zsntcr0rE-RBfBAaF553DqBk-J02UtWsP8VqrUh3tKu3jO_JwEO8n1cWTJ5TN"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
