# 设备组添加设备

> 官方文档：[设备组添加设备](https://developers.weixin.qq.com/miniprogram/dev/server/API/hardware-device/api_addiotgroupdevice.html)
> 所属分类：[硬件设备](../硬件设备目录.md)
> 导航路径：硬件设备 / 设备组添加设备
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：addIotGroupDevice

本接口用于为设备组添加设备

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/business/group/adddevice?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口不支持第三方平台调用。

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

一个设备组最多添加 50 个设备。 一个设备同一时间只能被添加到一个设备组中。

## 5. 代码示例

请求示例

```json
{
  "group_id": "GROUP_ID",
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
