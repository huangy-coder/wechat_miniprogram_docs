# 单个文件上传

> 官方文档：[单个文件上传](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_singlefileupload.html)
> 所属分类：[短剧媒资管理](../../短剧媒资管理目录.md)
> 导航路径：短剧媒资管理 / 媒资上传 / 单个文件上传
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：singleFileUpload

该接口用于上传媒体（和封面）文件，上传小文件（小于10MB）时使用。上传大文件请使用[分片上传](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload/api_applyupload)接口。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/vod/singlefileupload?access_token=ACCESS_TOKEN
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

1. 不填写 `cover_type`，`cover_data` 字段时默认截取视频首帧作为封面图。
2. Content-Type 需要指定为 `multipart/form-data; boundary=<delimiter>`
3. `<箭头括号>` 表示必须替换为有效值的变量。

## 5. 代码示例

请求示例

```bash
POST /wxa/sec/vod/singlefileupload?access_token=ACCESS_TOKEN HTTP/1.1
Host: api.weixin.qq.com
Content-Type: multipart/form-data; boundary=--------------------------334603653359572775563544
Content-Length: 1675021

----------------------------334603653359572775563544
Content-Disposition: form-data; name="media_name"

我的演艺 - 第1集
----------------------------334603653359572775563544
Content-Disposition: form-data; name="media_type"

MP4
----------------------------334603653359572775563544
Content-Disposition: form-data; name="cover_type"

JPEG
----------------------------334603653359572775563544
Content-Disposition: form-data; name="media_data"; filename="test.mp4"

<test.mp4>
----------------------------334603653359572775563544
Content-Disposition: form-data; name="cover_data"; filename="wechat.jpeg"

<wechat.jpeg>
----------------------------334603653359572775563544--
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
