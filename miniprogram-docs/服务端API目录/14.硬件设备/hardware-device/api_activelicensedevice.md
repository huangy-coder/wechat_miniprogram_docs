# 激活设备license

> 官方文档：[激活设备license](https://developers.weixin.qq.com/miniprogram/dev/server/API/hardware-device/api_activelicensedevice.html)
> 所属分类：[硬件设备](../硬件设备目录.md)
> 导航路径：硬件设备 / 激活设备license
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：activeLicenseDevice

该接口用于批量绑定设备，并消耗相应的资源包中的激活码序号。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/business/license/activedevice?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：118
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.device_list(Array) Object Payload

待激活的设备列表

## 3. 返回参数

### 返回体 Response Payload

### Res.device_list(Array) Object Payload

设备列表

## 4. 注意事项

- 正式license的使用：每次调用最多激活100个设备，且所有设备类型必须属于同一个资源包类型。每个激活码序号只能用于激活一台设备。每个设备最多绑定 3 个激活码序号，即剩余有效时间不能超过 3 年。
- 体验license的使用：详见[平台公告](https://developers.weixin.qq.com/community/minihome/doc/000204860703984b45c02830963c01)

## 其他说明

1. 自2024年9月9日15时起，激活操作不再消耗license。为确保兼容性，本接口对于请求激活设备将返回无实际意义的「激活成功」，形如：

```json
{
  "model_id": "MODEL_ID1",
  "sn": "SN1",
  "errcode": 0,
  "expire_time": 1893427200,
}
```

其中`errcode`固定返回0，`expire_time`固定返回`2030-01-01 00:00:00`时间戳

1. 本接口将于2024年12月31日正式回收，请开发者及时进行调整适配。

详见[调整公告](https://developers.weixin.qq.com/community/minihome/doc/000428b5bd4d10c54812f7cd466401)

## 5. 代码示例

请求示例

```json
{
  "pkg_type": 0,
  "device_list": [
    {
      "model_id": "MODEL_ID1",
      "sn": "SN1",
      "active_number": 1
    },
    {
      "model_id": "MODEL_ID2",
      "sn": "SN2",
      "active_number": 2
    }
  ]
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "device_list": [
    {
      "model_id": "MODEL_ID1",
      "sn": "SN1",
      "errcode": 0
    },
    {
      "model_id": "MODEL_ID2",
      "sn": "SN2",
      "errcode": 0
    }
  ]
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
