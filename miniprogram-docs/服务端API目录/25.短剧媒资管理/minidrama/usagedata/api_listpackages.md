# 查询流量包详情

> 官方文档：[查询流量包详情](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/usagedata/api_listpackages.html)
> 所属分类：[短剧媒资管理](../../短剧媒资管理目录.md)
> 导航路径：短剧媒资管理 / 数据统计 / 查询流量包详情
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：listPackages

该接口用于查询流量包的使用详情

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/vod/listpackages?access_token=ACCESS_TOKEN
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

### Res.package_list(Array) Object Payload

流量包详情列表

## 4. 注意事项

1. 流量包单位为MB，流量进制换算规则：1GB=1000MB
2. 剩余可用流量为有效的(status=1)流量包的余额之和。
3. 流量包是存在有效期限制的，需要注意流量包是否即将过期

## 5. 代码示例

请求示例

```json
{
    "status": 1,
    "limit": 100
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "package_list": [{
            "all": 100000,
            "end_time": 1715234665,
            "is_deleted": 0,
            "order_id": 2921020570379436032,
            "package_id": "ZY2921020620526534656",
            "start_time": 1683698665,
            "status": 1,
            "used": 188
        },
        {
            "all": 10000,
            "end_time": 1715151889,
            "is_deleted": 0,
            "order_id": 2919631279891890176,
            "package_id": "ZY2919631860383563776",
            "start_time": 1683615889,
            "status": 1,
            "used": 10000
        }
    ],
    "total_count": 2
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
