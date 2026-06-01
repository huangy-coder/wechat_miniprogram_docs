# 小程序交易类型变更申请

> 官方文档：[小程序交易类型变更申请](https://developers.weixin.qq.com/miniprogram/dev/server/API/order_shipping/api_setwxatradetypecgi.html)
> 所属分类：[小程序交易管理服务](../小程序交易管理服务目录.md)
> 导航路径：小程序交易管理服务 / 小程序交易类型变更申请
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：setwxatradetypecgi

本接口用于小程序开发者提交交易类型变更申请。当小程序的交易类型需要更新时，开发者可通过本接口提交相关材料进行申请。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/order/setwxatradetypecgi?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：142
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.material_list(Array) Object Payload

申请材料列表，最多10个，其中视频最多3个

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Body.trade_type Enum

申请变更后的目标交易类型

## 5. 注意事项

1. 请确保 access_token 有效且未过期
2. 申请材料需真实有效，支持图片和视频两种类型
3. 申请理由需详细说明交易类型变更的原因
4. **一个账号只能申请一次**，重复提交会返回错误码 268486048
5. 如有特殊需求需要多次申请，请联系小程序客服处理
6. 图片和视频需要先通过[新增临时素材](https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_uploadtempmedia)接口上传，获取 media_id 后再使用

## 6. 代码示例

请求示例

```json
{
        "trade_type": 3,
        "material_list": [
          {
            "type": 1,
            "media_id": "media_id_sample_1"
          },
          {
            "type": 2,
            "media_id": "media_id_sample_2"
          }
        ],
        "reason": "申请理由"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
