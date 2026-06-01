# 确认上传

> 官方文档：[确认上传](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_commitupload.html)
> 所属分类：[短剧媒资管理](../../短剧媒资管理目录.md)
> 导航路径：短剧媒资管理 / 媒资上传 / 确认上传
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：commitUpload

该接口用于完成整个分片上传流程，合并所有文件分片，确认媒体文件（和封面图片文件）上传到平台的结果，返回文件的 ID。请求中需要给出每一个分片的 `part_number` 和 `etag`，用来校验分片的准确性。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/vod/commitupload?access_token=ACCESS_TOKEN
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

### Body.media_part_infos Object Payload

本次分片上传中媒体文件每个分片的信息。

### Body.cover_part_infos Object Payload

本次分片上传中封面图片文件每个分片的信息。

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1. `Content-Type` 需要指定为 `application/json`。
2. 调用该接口之前必须先调用[申请分片上传](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_applyupload)接口以及[上传分片](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_uploadpart)接口。
3. 如本次分片上传除上传媒体文件外还需要上传封面图片，则请求中还需提供 cover_part_infos 字段以用于合并封面图片文件分片。
4. 请求中 `media_part_infos` 和 `cover_part_infos` 字段必须按 `part_number` 从小到大排序，`part_number` 必须从 1 开始，连续且不重复。

## 5. 代码示例

请求示例

```json
{
    "upload_id": "abcdefg12345",
    "media_part_infos": [
        {
            "part_number": 1,
            "etag": "\"d899fbd1e06109ea2e4550f5751c88d6\""
        },
        {
            "part_number": 2,
            "etag": "\"jfb9892jfnhda2e4550f5bvhju9392af\""
        },
        {
            "part_number": 3,
            "etag": "\"bifh9u92wjefvjhytvn9u2898ef9uhea\""
        }
    ]
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "media_id": 123456
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
