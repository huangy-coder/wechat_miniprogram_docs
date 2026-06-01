# 查询设备激活详情

> 官方文档：[查询设备激活详情](https://developers.weixin.qq.com/miniprogram/dev/server/API/hardware-device/api_getlicensedeviceinfo.html)
> 所属分类：[硬件设备](../硬件设备目录.md)
> 导航路径：硬件设备 / 查询设备激活详情
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getLicenseDeviceInfo

该接口用于批量查询设备剩余有效期。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/business/license/getdeviceinfo?access_token=ACCESS_TOKEN
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

设备列表

## 3. 返回参数

### 返回体 Response Payload

### Res.device_list(Array) Object Payload

设备列表

## 4. 注意事项

## 其他说明

1. 自2024年9月9日15时起，为确保兼容性，本接口对于请求设备列表均返回无实际意义的「已激活」，形如：

```json
{
      "model_id": "MODEL_ID2",
      "sn": "SN2",
      "expire_time": 1893427200
}
```

其中`expire_time`固定返回`2030-01-01 00:00:00`时间戳

1. 本接口将于2024年12月31日正式回收，请开发者及时进行调整适配。

详见[调整公告](https://developers.weixin.qq.com/community/minihome/doc/000428b5bd4d10c54812f7cd466401)

## 5. 代码示例

请求示例

```json
{
  "device_list": [
    {
      "model_id": "MODEL_ID1",
      "sn": "SN1"
    },
    {
      "model_id": "MODEL_ID2",
      "sn": "SN2"
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
      "expire_time": 1630425600
    },
    {
      "model_id": "MODEL_ID2",
      "sn": "SN2",
      "expire_time": 1630425600
    }
  ]
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
