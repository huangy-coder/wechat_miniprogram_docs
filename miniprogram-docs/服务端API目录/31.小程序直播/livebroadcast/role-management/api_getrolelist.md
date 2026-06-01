# 查询成员列表

> 官方文档：[查询成员列表](https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/role-management/api_getrolelist.html)
> 所属分类：[小程序直播](../../小程序直播目录.md)
> 导航路径：小程序直播 / 成员管理 / 查询成员列表
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getRoleList

该接口用于查询小程序直播成员列表。

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/wxaapi/broadcast/role/getrolelist?access_token=ACCESS_TOKEN&offset=OFFSET&limit=LIMIT&keyword=KEYWORD
```

### 云调用

- 调用方法：liveBroadcast.getRoleList
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：52
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

无

## 3. 返回参数

### 返回体 Response Payload

### Res.list(Array) Object Payload

角色列表

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```bash
GET https://api.weixin.qq.com/wxaapi/broadcast/role/getrolelist?access_token=ACCESS_TOKEN&offset=OFFSET&limit=LIMIT&keyword=KEYWORD
```

返回示例

```json
{
    "errcode": 0,
    "total" : 1, // 总个数
    "list": [{
        "headingimg": "http://wx.qlogo.cn/mmhead/Q3auHgzwzM5jBhFwrHoeoaxTlhP9YzlVica7wu6lZLnGreKAj7CVicA/0", // 头像
        "nickname": "test1", // 昵称
        "openid": "o7esq5MvImF2SEm7OHYohausj2o",
        "roleList": [2, 3], // 具有的身份，[0-超级管理员，1-管理员，2-主播，3-运营者]
        "updateTimestamp": "1600340080", // 更新时间
        "username": "o0****0o", //脱敏微信号
    }]
} 
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
