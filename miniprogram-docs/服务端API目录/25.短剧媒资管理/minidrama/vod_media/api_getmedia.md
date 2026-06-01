# 获取媒资详细信息

> 官方文档：[获取媒资详细信息](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_media/api_getmedia.html)
> 所属分类：[短剧媒资管理](../../短剧媒资管理目录.md)
> 导航路径：短剧媒资管理 / 媒资管理 / 获取媒资详细信息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getMedia

该接口用于获取已上传到平台的指定媒资信息，用于开发者后台管理使用。用于给用户客户端播放的链接应该使用[getmedialink接口](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_media/api_getmedialink)获取。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/vod/getmedia?access_token=ACCESS_TOKEN
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

媒体文件id。

### Res.media_info.audit_detail Object Payload

审核信息

## 4. 枚举信息

### Res.media_info.audit_detail.status Enum

审核状态，需要注意可能存在单个剧集的状态为审核通过，但是剧目整体是未通过的情况，而能不能获取播放链接取决于剧目的审核状态

## 5. 注意事项

1. `Content-Type` 需要指定为 `application/json`。
2. 本接口返回的视频或图片链接均为临时链接，不应将其保存下来

## 6. 代码示例

请求示例

```json
{
    "media_id": 28918028
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "media_info": {
        "media_id": 28918028,
        "create_time": 1682214878,
        "expire_time": 1689990878,
        "drama_id": 4907,
        "file_size": "9849163",
        "duration": 120,
        "name": "我的演艺 - 第1集",
        "description": "剧情非常精彩哦",
        "cover_url": "https://developers.weixin.qq.com/test.jpg",
        "original_url": "https://developers.weixin.qq.com/test.mp4",
        "mp4_url": "",
        "hls_url": "",
        "audit_detail": {
            "status": 3,
            "create_time": 1682215878,
            "audit_time": 1682235878,
            "reason": "",
            "evidence_material_id_list": [
                "ivpvxwtX5GNzkCi6aX12f_VIFmGKiiwW5fkbISkZcamr6g_XrWqHkxB22MMAmIShb6rKOrS7"
            ]
        }
    }
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
