# 获取章节信息

> 官方文档：[获取章节信息](https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_getchapter.html)
> 所属分类：[小说作品管理](../../小说作品管理目录.md)
> 导航路径：小说作品管理 / 作品管理 / 获取章节信息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getChapter

该接口用于获取章节信息。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/book/getchapter?access_token=ACCESS_TOKEN
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

### Res.chapter Object Payload

章节信息

### Res.chapter.audit_info Object Payload

审核信息

## 4. 注意事项

同作品信息，该接口也会区分编辑版和发布版。当设置编辑版信息时，只能获取作品编辑版里的章节信息；当设置发布版信息时，只能获取作品发布版里的章节信息。

## 5. 代码示例

请求示例

```json
{
    "book_id": "A1b2C3d4",
    "chapter_id": "abc123"
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "chapter": {
        "book_id": "A1b2C3d4",
        "chapter_id": "abc1234",
        "chapter_title": "第一章 香蕉的诞生",
        "content": "从前，有一座山……",
        "word_cnt": 1234,
        "create_time": 1704793640,
        "audit_info": {
            "audit_status": 3,
            "create_time": 1705062255,
            "audit_time": 1705063255,
        },
        "volume_index": -1,
        "original_id": "1234"
    }
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
