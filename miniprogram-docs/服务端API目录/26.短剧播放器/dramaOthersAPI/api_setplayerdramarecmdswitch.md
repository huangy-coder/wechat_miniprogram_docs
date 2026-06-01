# 播放原始视频-推荐位控制接口

> 官方文档：[播放原始视频-推荐位控制接口](https://developers.weixin.qq.com/miniprogram/dev/server/API/dramaOthersAPI/api_setplayerdramarecmdswitch.html)
> 所属分类：[短剧播放器](../短剧播放器目录.md)
> 导航路径：短剧播放器 / 播放原始视频-推荐位控制接口
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：setPlayerDramaRecmdSwitch

开发者可通过后台接口选择播放上传未经转码的原始视频。

开发者可通过后台接口控制推荐位的开启与关闭。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxadrama/setplayerdramarecmdswitch?access_token=ACCESS_TOKEN
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

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

### 5.1 播放原始视频

请求示例

```json
{
    "entry_type": 2002,
    "switch_status": "true"
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

### 5.2 推荐位控制

请求示例

```json
{
    "entry_type":1,
    "switch_status": true
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
