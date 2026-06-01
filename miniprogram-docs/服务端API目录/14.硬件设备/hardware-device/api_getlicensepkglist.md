# 查询license资源包列表

> 官方文档：[查询license资源包列表](https://developers.weixin.qq.com/miniprogram/dev/server/API/hardware-device/api_getlicensepkglist.html)
> 所属分类：[硬件设备](../硬件设备目录.md)
> 导航路径：硬件设备 / 查询license资源包列表
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getLicensePkgList

查询小程序已购买的 license 资源包列表信息。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/business/license/getpkglist?access_token=ACCESS_TOKEN
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

## 3. 返回参数

### 返回体 Response Payload

### Res.pkg_list(Array) Object Payload

资源包列表

## 4. 注意事项

开发者需要先在小程序管理后台购买设备 license 的套餐包后，方可查询到对应的资源包。

本接口将于2024年12月31日正式回收，请开发者及时进行调整适配。

详见[调整公告](https://developers.weixin.qq.com/community/minihome/doc/000428b5bd4d10c54812f7cd466401)

## 5. 代码示例

请求示例

```json
{
  "pkg_type": 0
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "success",
  "pkg_list": [
    {
      "pkg_id": "ZY100000000",
      "pkg_type": 1,
      "start_time": 1629907200,
      "end_time": 1630425600,
      "pkg_status": 1,
      "used": 10,
      "all": 100
    },
    {
      "pkg_id": "ZY100000001",
      "pkg_type": 2,
      "start_time": 1629907200,
      "end_time": 1630425600,
      "pkg_status": 1,
      "used": 20,
      "all": 200
    }
  ],
  "max_active_number": 300
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
