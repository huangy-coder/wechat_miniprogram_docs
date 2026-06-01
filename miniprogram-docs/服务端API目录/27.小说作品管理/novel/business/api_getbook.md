# 获取作品信息

> 官方文档：[获取作品信息](https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_getbook.html)
> 所属分类：[小说作品管理](../../小说作品管理目录.md)
> 导航路径：小说作品管理 / 作品管理 / 获取作品信息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getBook

该接口用于获取作品详细信息，同获取作品列表，这里也会区分发布版和编辑版。 发布版和编辑版的区别见“获取作品列表”小节。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/book/getbook?access_token=ACCESS_TOKEN
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

### Res.book(Array) Object Payload

作品信息

### Res.book(Array).volume_list Object Payload

分卷信息

### Res.book(Array).audit_info Object Payload

审核信息。未发起审核不返回该字段。

## 4. 注意事项

1. mp 后台的作品列表对应编辑版信息，需要设置 need_edited_data = true 来拉取。

## 5. 代码示例

请求示例

```json
{
    "book_id": "A1b2C3d4"
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "book": {
        "book_id": "A1b2C3d4",
        "title": "香蕉牛奶",
        "intro": "香蕉牛奶的奇幻之旅。",
        "cover_url": "https://xxx.jpg",
        "author": "香蕉和牛奶",
        "first_category_id": 10001,
        "first_category_name": "男频",
        "second_category_id": 10002,
        "second_category_name": "都市",
        "third_category_id": 10003,
        "third_category_name": "娱乐明星",
        "complete_status": 2,
        "upload_scene": 1,
        "chapter_cnt": 5,
        "volume_cnt": 0,
        "volume_list": [],
        "total_word_cnt": 15234,
        "create_time": 1704715412,
        "original_id": "",
        "chapter_order_method": 0

    }
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
