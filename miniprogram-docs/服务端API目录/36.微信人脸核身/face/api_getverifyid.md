# 获取用户人脸核身会话唯一标识

> 官方文档：[获取用户人脸核身会话唯一标识](https://developers.weixin.qq.com/miniprogram/dev/server/API/face/api_getverifyid.html)
> 所属分类：[微信人脸核身](../微信人脸核身目录.md)
> 导航路径：微信人脸核身 / 获取用户人脸核身会话唯一标识
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getVerifyId

业务方后台根据「用户实名信息（姓名+身份证）」调用 `getVerifyId` 接口获取人脸核身会话唯一标识 `verifyId` 字段，然后给到小程序前端调用 `wx.requestFacialVerify` 接口使用。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cityservice/face/identify/getverifyid?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.cert_info Object Payload

用户身份信息

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

用于生成 openid 的小程序 appid 一定要和前端调用 wx.requestFacialVerify 接口进行人脸核身时的小程序 appid 保持一致，不然就会人脸核身失败。

用于生成 verify_id 的 openid 用户身份标识一定要和前端调用 wx.requestFacialVerify 接口进行人脸核身时的用户身份保持一致，不然就会人脸核身失败。

## 5. 代码示例

请求示例

```json
{
  "out_seq_no": "xxx",
  "cert_info": {
    "cert_type": "xxx",
    "cert_name": "xxx",
    "cert_no": "xxx"
  },
  "openid": "xxx"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "verify_id": "verify_id_xxxx",
  "expires_in": 3600,
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
