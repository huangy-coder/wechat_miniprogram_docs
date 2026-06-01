# 查看账号主授权关系列表

> 官方文档：[查看账号主授权关系列表](https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/auth/api_querybookauthv2.html)
> 所属分类：[小说作品管理](../../小说作品管理目录.md)
> 导航路径：小说作品管理 / 授权管理 / 查看账号主授权关系列表
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：querybookauthv2

此接口可用于查看账号的授权关系列表，也可以看账号被授权关系列表。

1. 查看账号的授权关系列表，主授权账号使用（同 appid 每天限额调用 50000 次）
2. 查看账号的被授权关系列表，被授权账号使用（同 appid 每天限额调用 10000 次），支持查询：当前账号关联的授权方账号列表、指定授权方所授权的小说列表、指定小说的账号级别授权信息
3. 查询指定授权方所授权的小说列表
4. 查询指定小说的授权信息

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/book/querybookauthv2?access_token=ACCESS_TOKEN
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

### Res.appid_results(Array) Object Payload

被授权方列表, 结果按授权过期时间从早到晚排序

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

### 5.1 查询授权关系列表

请求示例

```json
{
    "type": 0,
    "count": 20,
    "cursor": ""   
}
```

返回示例

```json
{
    "errcode": 0, //当等于0时，results字段的数据才有效
    "errmsg": "ok",
    "appid_results": [
        {
            "grantor_appid": "wx001",
            "grantee_appid": "wx004",
            "expire_time": 1704259146
        },
        {
            "grantor_appid": "wx001",
            "grantee_appid": "wx005",
            "expire_time": 1801698644
        }
    ],
    "next_cursor": "123456"
}
```

### 5.2 查询被授权关系

请求示例

type = 1，不传 grantor_appid 和 book_ids

```json
{
    "type": 1,
    "cursor": "",
    "count": 5
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "appid_results": [
        {
            "grantor_appid": "wx003",
            "grantee_appid": "wx002",
            "expire_time": 1704970161
        },
        {
            "grantor_appid": "wx001",
            "grantee_appid": "wx002",
            "expire_time": 1705460123
        }
    ],
    "next_cursor": "123456"
}
```

### 5.3 查询指定授权方所授权的小说列表

请求示例

type = 1，传 grantor_appid

```json
{
    "type": 1,
    "cursor": "",
    "count": 5,
    "grantor_appid": "wx001"
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "book_results": [
        {
            "book_id": "b001",
            "grantor_appid": "wx001",
            "grantee_appid": "wx002",
            "expire_time": 1704970161
        },
        {
            "book_id": "b002",
            "grantor_appid": "wx001",
            "grantee_appid": "wx002",
            "expire_time": 1704970161
        }
    ],
    "next_cursor": "123456"
}
```

### 5.4 查询指定小说的授权信息

请求示例

type = 1，book_ids 元素不为空

```json
{
    "type": 1,
    "book_ids": ["b001", "b003"]
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "book_results": [
        {
            "book_id": "b001",
            "grantor_appid": "wx001",
            "grantee_appid": "wx002",
            "expire_time": 1704970161
        },
        {
            "book_id": "b003",
            "grantor_appid": "wx003",
            "grantee_appid": "wx002",
            "expire_time": 1705460123
        }
    ]
}
```

## 6. 错误码

此接口没有特殊错误码，可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
