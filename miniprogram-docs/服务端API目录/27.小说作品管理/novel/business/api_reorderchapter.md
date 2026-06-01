# 调整章节顺序

> 官方文档：[调整章节顺序](https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_reorderchapter.html)
> 所属分类：[小说作品管理](../../小说作品管理目录.md)
> 导航路径：小说作品管理 / 作品管理 / 调整章节顺序
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：reorderChapter

该接口用于调整作品编辑版信息中的章节顺序，不直接影响发布版，需要提审通过后才会更新发布版。若需批量修改章节顺序，可通过“编辑作品”接口的 chapter_id_list 参数实现。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/book/reorderchapter?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：169
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1. 该接口仅当作品“章节排序方式”为“追加”时才生效，如需修改章节排序方式可调用“[编辑作品](https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_updatebook)”接口。

## 5. 代码示例

请求示例

```json
{
    "book_id": "A1b2C3d4",
    "chapter_id": "abc123",
    "target_chapter_id": "qwe456",
    "operation": 1
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
