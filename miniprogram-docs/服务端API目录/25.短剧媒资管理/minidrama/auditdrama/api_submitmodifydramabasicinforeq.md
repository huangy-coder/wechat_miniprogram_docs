# 修改剧目基本信息

> 官方文档：[修改剧目基本信息](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/auditdrama/api_submitmodifydramabasicinforeq.html)
> 所属分类：[短剧媒资管理](../../短剧媒资管理目录.md)
> 导航路径：短剧媒资管理 / 剧目提审 / 修改剧目基本信息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：submitModifyDramaBasicInfoReq

该接口用于修改剧目基本信息。请求成功后，需要经过审核，审核通过后，最终才会修改基本信息。审核完成后，会下发通知。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/vod/modifydramabasicinfo?access_token=ACCESS_TOKEN
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

### Body.actor_list Object Payload

演员信息。如果需要修改，请填写所有的演员信息。

### Body.copyright Object Payload

版权保护相关。apply_for_copyright_protection =1时必填，否则无需填写 。

### Body.actor_list.actor(Array) Object Payload

演员列表

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1. 剧目必须已经审核通过。
2. 审核完成后会发送[事件通知](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/mini_drama/drama_review_status_event)
3. 本接口中使用的临时图片material_id可通过[新增临时素材接口](https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_uploadtempmedia)上传得到，对应临时素材接口中的media_id，本文档中为避免与剧集的media_id混淆，称其为material_id。

## 5. 代码示例

请求示例

```json
{
    "drama_id": 10001,
    "description": "新剧目简介",
    "cover_material_id": "新剧目海报临时material_id",
    "recommendations": "新剧目推荐语",
    "promotion_poster_material_id": "新推广海报临时material_id",
    "alternate_name": "备用剧名",
    "actor_list": {
        "actor": [{
            "name": "演员1",
            "photo_material_id": "xxxxxxxx",
            "role": "角色1",
            "profile": "简介"
        }, {
            "name": "演员2",
            "photo_material_id": "xxxxxxxx",
            "role": "角色2",
            "profile": "简介"
        }]
    },
     "qualification_type": 1,
     "qualification_certificate_material_id": "xxxxxxxx",
     "registration_number":"V123456788888888",
     "other_material_material_id":"新其他材料临时material_id"
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
