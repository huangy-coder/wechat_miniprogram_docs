# 创建作品

> 官方文档：[创建作品](https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_createbook.html)
> 所属分类：[小说作品管理](../../小说作品管理目录.md)
> 导航路径：小说作品管理 / 作品管理 / 创建作品
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：createBook

该接口用于创建作品（小说）。

1. 支持传入作品提供方主键用于去重。
2. 支持两种章节排序方式 1)、追加（默认方式）：新上传章节会追加到章节列表的最后，可调用“编辑作品”或“调整章节顺序”接口更改章节位置。 2)、seq 递增：上传章节时需要额外带上 seq 字段，根据章节 seq 从小到大进行稳定排序调整章节位置。
3. 封面图支持的文件格式：jpg、jpeg、png。建议尺寸 600x800 像素。
4. 题材关键词、精彩片段用于平台推荐场景。精彩片段需为本书内容。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/book/createbook?access_token=ACCESS_TOKEN
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

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
    "title": "香蕉牛奶",
    "intro": "香蕉牛奶的奇幻之旅。",
    "cover_media_id": "xxx",
    "author": "香蕉和牛奶",
    "first_category_id": 10001,
    "second_category_id": 10002,
    "third_category_id": 10003,
    "complete_status": 1
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "book_id": "A1b2C3d4"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
