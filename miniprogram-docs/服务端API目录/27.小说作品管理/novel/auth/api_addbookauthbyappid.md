# 新增账号-账号授权

> 官方文档：[新增账号-账号授权](https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/auth/api_addbookauthbyappid.html)
> 所属分类：[小说作品管理](../../小说作品管理目录.md)
> 导航路径：小说作品管理 / 授权管理 / 新增账号-账号授权
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：addbookauthbyappid

增加账号-账号的授权关系数据，主授权账号可一次调用新增多条授权关系（上限20条）

1. 同appid每天限额调用100000次。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/book/addbookauthbyappid?access_token=ACCESS_TOKEN
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

### Body.infos(Array) Object Payload

被授权账号列表。上限一次 20 条

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
    "infos": [
        {
            "grantee_appid": "wx002",
            "expire_time": 1704970161
        },
        {
            "grantee_appid": "wx003",
            "expire_time": 1705460123
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
            "errcode": 0,  //内层errcode，表示每条授权关系是成功/失败,
            "errmsg": "ok"
        }
    ],
    "errmsg": "ok"
}
```

## 6. 错误码

此接口没有特殊错误码，可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
