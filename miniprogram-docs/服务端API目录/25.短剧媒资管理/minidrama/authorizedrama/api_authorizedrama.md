# 增加剧目授权

> 官方文档：[增加剧目授权](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/authorizedrama/api_authorizedrama.html)
> 所属分类：[短剧媒资管理](../../短剧媒资管理目录.md)
> 导航路径：短剧媒资管理 / 剧目授权 / 增加剧目授权
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：authorizedRama

该接口用于授权方给被授权方授权一些剧目的播放权限。

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/wxa/sec/vod/authorizedrama?access_token=ACCESS_TOKEN
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

剧目的授权结果。

## 4. 注意事项

1. 授权方与被授权方都需申请【文娱-微短剧】类目;
2. 被授权的剧目必须已经审核通过;
3. 如果指定授权到期时间，授权时长不能小于7天（从当前时间算起）

## 5. 代码示例

请求示例

```json
{
    "authorized_appid": "wx*************",
    "drama_id": [100200, 100205],
    "authz_expire_time": 0
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "result": [
        {
            "drama_id": 100200,
            "errcode": 0
        },
        {
            "drama_id": 100205,
            "errcode": 1,
            "errmsg": "获取剧目100205失败！"
        }
    ]
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
