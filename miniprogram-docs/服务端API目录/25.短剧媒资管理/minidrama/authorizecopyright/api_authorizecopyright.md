# 增加版权授权

> 官方文档：[增加版权授权](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizecopyright/api_authorizecopyright.html)
> 所属分类：[短剧媒资管理](../../短剧媒资管理目录.md)
> 导航路径：短剧媒资管理 / 版权授权 / 增加版权授权
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：authorizeCopyright

该接口用于授权受版权保护的剧目。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/vod/authorizecopyright?access_token=ACCESS_TOKEN
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

### Res.result(Array) Object Payload

授权的结果

## 4. 注意事项

1. 授权方与被授权方都需申请【文娱-微短剧】或【文娱-互动微短剧】类目;
2. 可按小程序授权或按主体授权，如果按主体授权，则该主体下有【文娱-微短剧】或【文娱-互动微短剧】类目的小程序都自动获得授权。
3. 受版权保护的剧目才能授权，剧目提审时可申请版权保护。

## 5. 代码示例

请求示例

```json
{
    "authorization_type": 2,
    "authorized_appid": "wx*************",
    "drama_ids": [10001, 10009],
    "expire_time": 1729157743
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "result": [
        {
            "drama_id": 10001,
            "errcode": 0,
            "errmsg": "ok"
        },
        {
            "drama_id": 10009,
            "errcode": 0,
            "errmsg": "ok"
        }
    ]
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
