# 批量上传章节

> 官方文档：[批量上传章节](https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_batchcreatechapter.html)
> 所属分类：[小说作品管理](../../小说作品管理目录.md)
> 导航路径：小说作品管理 / 作品管理 / 批量上传章节
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：batchCreateChapter

该接口用于批量上传章节到作品编辑版信息里，不直接影响发布版，需要提审通过后才会更新发布版

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/book/batchcreatechapter?access_token=ACCESS_TOKEN
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

### Body.chapter_list(Array) Object Payload

章节信息，单次最多上传 10 章。

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1. 该接口会对标题进行预处理，删除标题的首尾空格，并将标题中间的连续空格替换为 1 个空格。
2. 审核中的作品不支持上传章节。
3. 作品章节排序方式为“追加”模式时，新上传章节会放到作品的最后，seq 字段选填，无实际作用，请按照章节顺序串行调用接口。若需要对已上传章节调整顺序，可以调用”[编辑作品](https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_updatebook)“或“[调整章节顺序](https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_createbook)”接口。
4. 作品章节排序方式为“seq 递增”模式时，新上传的章节会根据 seq 从小到大稳定排序到正确位置。接口仍需串行调用，不支持并发调用

## 5. 代码示例

请求示例

```json
{
    "book_id": "A1b2C3d4",
    "chapter_list": [
        {
            "chapter_title": "第一章 香蕉的诞生",
            "content": "从前，有一座山……"
        },
        {
            "chapter_title": "第二章 牛奶的诞生",
            "content": "一望无际的草原，有一群快乐的奶牛……"
        }
    ]
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "chapter_id_list": ["abc1234", "abc2345"]
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
