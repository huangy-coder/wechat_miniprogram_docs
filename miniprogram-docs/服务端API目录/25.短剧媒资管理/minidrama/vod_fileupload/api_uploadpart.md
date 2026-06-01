# 上传分片

> 官方文档：[上传分片](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_uploadpart.html)
> 所属分类：[短剧媒资管理](../../短剧媒资管理目录.md)
> 导航路径：短剧媒资管理 / 媒资上传 / 上传分片
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：uploadPart

将文件的其中一个分片上传到平台，最多支持100个分片，每个分片大小为5MB，最后一个分片可以小于5MB。该接口适用于视频和封面图片。视频最大支持500MB，封面图片最大支持10MB。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/vod/uploadpart?access_token=ACCESS_TOKEN
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

1. 调用该接口之前必须先调用[申请分片上传](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_applyupload)接口。
2. 在申请分片上传时，如果不填写 `cover_type`，则默认截取视频首帧作为封面图。
3. `Content-Type` 需要指定为 `multipart/form-data; boundary=<delimiter>`，`<箭头括号>`表示必须替换为有效值的变量。
4. `part_number` 从 1 开始。如除了上传视频外还需要上传封面图，则封面图的 `part_number` 需重新从 1 开始编号。

## 5. 代码示例

请求示例

```bash
POST /wxa/sec/vod/uploadpart?access_token=ACCESS_TOKEN HTTP/1.1
Host: api.weixin.qq.com
Content-Type: multipart/form-data; boundary=--------------------------334603653359572775563544
Content-Length: 5347737

----------------------------334603653359572775563544
Content-Disposition: form-data; name="upload_id"

9457878
----------------------------334603653359572775563544
Content-Disposition: form-data; name="part_number"

1
----------------------------334603653359572775563544
Content-Disposition: form-data; name="resource_type"

1
----------------------------334603653359572775563544
Content-Disposition: form-data; name="data"; filename="test.mp4"

<test.mp4>
----------------------------334603653359572775563544--
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "etag": "\"d899fbd1e06109ea2e4550f5751c88d6\""
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
