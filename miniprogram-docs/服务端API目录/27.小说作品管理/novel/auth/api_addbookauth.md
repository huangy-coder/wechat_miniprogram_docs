# 新增账号-小说授权

> 官方文档：[新增账号-小说授权](https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/auth/api_addbookauth.html)
> 所属分类：[小说作品管理](../../小说作品管理目录.md)
> 导航路径：小说作品管理 / 授权管理 / 新增账号-小说授权
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：addBookAuth

增加账号-小说的授权关系数据，主授权账号使用可一次调用新增多条授权关系（上限20条）

1. 同appid每天限额调用1000000次
2. 同appid每分钟限额调用100次，即2000条授权关系（建议控制好每分钟调用量，调用过猛被拦截的调用量也会消耗每日调用量的额度， 日限额耗完当日就会无法调用）

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/book/addbookauth?access_token=ACCESS_TOKEN
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

### Body.books(Array) Object Payload

books

## 3. 返回参数

### 返回体 Response Payload

### Res.results(Array) Object Payload

results

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
    "books": [
        {
            "book_id": "A1Hcfuuv",
            "expire_time": 1704970161,
            "grantee_appid": "wx002"
        },
        {
            "book_id": "KqNdTu",
            "expire_time": 1705460123,
            "grantee_appid": "wx003"
        }
    ]
}
```

返回示例

```json
{
    "errcode": 0,  //外层errcode， 表示本次调用整体成功/失败
    "results": [
        {
            "errcode": 0  //内层errcode，表示每条授权关系是成功/失败
        }
    ]
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
