# 获取媒资播放链接

> 官方文档：[获取媒资播放链接](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_media/api_getmedialink.html)
> 所属分类：[短剧媒资管理](../../短剧媒资管理目录.md)
> 导航路径：短剧媒资管理 / 媒资管理 / 获取媒资播放链接
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getMediaLink

该接口用于获取视频临时播放链接，用于给用户的播放使用。只有审核通过的视频才能通过该接口获取播放链接。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/vod/getmedialink?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：153
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.media_info Object Payload

媒体播放信息

## 4. 注意事项

1. `Content-Type` 需要指定为 `application/json`。
2. 本接口返回的视频或图片链接均为临时链接，不应将其保存下来。
3. 能不能获取播放链接取决于剧目审核状态，可能存在单个剧集的状态为审核通过，但是剧目整体是未通过的情况，这种情况也没法获取播放链接。
4. 开发者如需区分不同渠道的播放流量或次数，可以在us参数中传入渠道标识，这样得到的播放链接中us参数的前半部分就包含有渠道标识。开发者把这个带有渠道标识的链接分发给对应的渠道播放，就能统计到不同渠道播放情况。统计的数据来源为CDN日志（从[getcdnlogs接口](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/usagedata/api_getcdnlogs)得到），CDN日志中“文件路径”列中的参数也带有该标识，再结合日志中“字节数”列的流量数值，估算每个渠道所消耗的流量。另需注意日志统计的流量和扣费流量的差异，详情参考[getcdnlogs接口](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/usagedata/api_getcdnlogs)中的注意事项。
5. 平台可能使用多个域名分发，不要假定播放链接的域名是固定的。

## 5. 代码示例

请求示例

```json
{
    "media_id": 28918028,
    "t": 1689990878
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "media_info": {
        "media_id": 28918028,
        "duration": 120,
        "name": "我的演艺 - 第1集",
        "description": "剧情非常精彩哦",
        "cover_url": "https://developers.weixin.qq.com/test.jpg",
        "mp4_url": "https://developers.weixin.qq.com/test-encode.mp4?t=64bb36de&us=647488c4792c15185b8fd2a6&sign=631355adf06a6cf7e45e29be17c66820",
        "hls_url": "https://developers.weixin.qq.com/test-encode.m3u8?t=64bb36de&us=647488c4792c15185b8fd2a6&sign=631355adf06a6cf7e45e29be17c66820"
    }
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
