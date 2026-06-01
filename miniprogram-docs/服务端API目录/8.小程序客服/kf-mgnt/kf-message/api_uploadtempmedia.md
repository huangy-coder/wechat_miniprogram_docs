# 新增临时素材

> 官方文档：[新增临时素材](https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_uploadtempmedia.html)
> 所属分类：[小程序客服](../../小程序客服目录.md)
> 导航路径：小程序客服 / 客服消息 / 新增临时素材
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：uploadTempMedia

本接口用于上传临时多媒体文件

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE
```

### 云调用

- 调用方法：officialAccount.media.upload
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：1、3、8-9、11、19、30-31、100
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1. 文件大小限制：图片2MB/视频10MB
2. 媒体文件保存3天

#### 其他补充

1、临时素材media_id是可复用的。

2、**媒体文件在微信后台保存时间为3天，即3天后media_id失效。**

3、上传临时素材的格式、大小限制与公众平台官网一致。

4、图片（image）: 10M，支持PNG\JPEG\JPG\GIF格式

5、语音（voice）：2M，播放长度不超过60s，支持AMR\MP3格式

6、视频（video）：10MB，支持MP4格式

7、缩略图（thumb）：64KB，支持JPG格式

## 5. 代码示例

请求示例

```bash
curl -F media=@test.jpg "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE"
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "type": "image",
  "media_id": "MEDIA_ID",
  "created_at": 1672500000
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ |

- ✔：该账号可调用此接口。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
