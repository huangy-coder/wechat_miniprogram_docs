# 申请分片上传

> 官方文档：[申请分片上传](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_applyupload.html)
> 所属分类：[短剧媒资管理](../../短剧媒资管理目录.md)
> 导航路径：短剧媒资管理 / 媒资上传 / 申请分片上传
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：applyUpload

上传大文件时需使用分片上传方式，分为 3 个步骤：

1. 申请分片上传，确定文件名、格式类型，返回 `upload_id`，唯一标识本次分片上传。
2. 上传分片，多次调用上传文件分片，需要携带 `part_number` 和 `upload_id`，其中 `part_number` 为分片的编号，支持乱序上传。当传入 `part_number` 和 `upload_id` 都相同的时候，后发起上传请求的分片将覆盖之前的分片。
3. 确认分片上传，当上传完所有分片后，需要完成整个文件的合并。请求体中需要给出每一个分片的 `part_number` 和 `etag`，用来校验分片的准确性，最后返回文件的 `media_id`。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/vod/applyupload?access_token=ACCESS_TOKEN
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

## 4. 注意事项

1. 如果填写了 cover_type，表明本次分片上传除上传媒体文件外还需要上传封面图片，不填写 cover_type 则默认截取视频首帧作为封面图片。
2. Content-Type 需要指定为 application/json

## 5. 代码示例

请求示例

```json
{
    "media_name": "我的演艺 - 第1集",
    "media_type": "MP4",
    "cover_type": "JPG"
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "upload_id": "123456"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
