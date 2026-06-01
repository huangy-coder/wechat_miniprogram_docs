# 剧目提审

> 官方文档：[剧目提审](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/auditdrama/api_auditdrama.html)
> 所属分类：[短剧媒资管理](../../短剧媒资管理目录.md)
> 导航路径：短剧媒资管理 / 剧目提审 / 剧目提审
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：auditDrama

剧目提交审核

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/vod/auditdrama?access_token=ACCESS_TOKEN
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

演员信息，需填写2-5位演员。当drama_type=2时必填，当drama_type=1和3时无需填写。

### Body.replace_media_list(Array) Object Payload

用于重新提审时替换审核不通过的剧集。

### Body.copyright Object Payload

版权保护相关。

### Body.actor_list.actor(Array) Object Payload

演员列表

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1. Content-Type 需要指定为 application/json。
2. 剧目信息与审核材料在首次提审时为必填，重新提审时根据是否需要修改选填，
3. 本接口中使用的临时图片material_id可通过[新增临时素材接口](https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_uploadtempmedia)上传得到，对应临时素材接口中的media_id，本文档中为避免与剧集的media_id混淆，称其为material_id。
4. 新增临时素材接口可以被小程序调用，调用的小程序账号和剧目提审的小程序账号必须是同一个，否则提交审核时会无法识别素材id。
5. 为规范微短剧行业健康有序发展，平台将对微短剧剧目提审及备案机制进行调整：**2024年5月27日起，针对制作成本在30万元以下的微短剧（2026年1月14日起制作成本调整为100万元以下），开发者需上传[《成本配置比例情况报告》](https://res.wx.qq.com/op_res/F0TQYnsCpdzIUXDGgP7rHCoeeWYDxu_mRNt3iA6a9BU_J5JchXBQEs_LO-0pxRV_VTbKcVN8Ulz8oO2R0ZrHDw)，剧目经平台审核后由平台下发备案号（备案号仅适用微信小程序平台）。**

## 5. 代码示例

### 5.1 首次提审请求数据示例

请求示例

```json
{
    "name": "这是剧名",
    "media_count": 2,
    "media_id_list": [
        20001,
        20002
    ],
    "producer": "制作方名",
    "description": "很有意思的一部剧",
    "cover_material_id": "xxxxxxxxxx",
    "registration_number": "012345678901234",
    "authorized_material_id": "122344",
    "other_material_material_id": "122355",
    "recommendations": "这是这部剧的推荐语。",
    "actor_list": {
        "actor": [
            {
                "name": "演员1",
                "photo_material_id": "xxxxxxxx",
                "role": "角色1",
                "profile": "简介"
            },
            {
                "name": "演员2",
                "photo_material_id": "xxxxxxxx",
                "role": "角色2",
                "profile": "简介"
            }
        ]
    },
    "copyright": {
        "copyright_role": 2,
        "apply_for_copyright_protection": 1,
        "proof_of_production": [
            "b45d9b657f80415f8f92d43fe500c9f8"
        ],
        "purchase_or_broadcast_authorization_certificate": [
            "671b7650084c404e9e70231823ffb7ee",
            "1fe80a9bbece4531b13e646dc2e170c2"
        ]
    }
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "drama_id": 10001
}
```

### 5.2 重新提审请求数据示例

请求示例

```json
{
    "drama_id": 10001,
    "replace_media_list": [
        {
            "old": 20001,
            "new": 20021
        },
        {
            "old": 20002,
            "new": 20022
        }
    ]
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "drama_id": 10001
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
