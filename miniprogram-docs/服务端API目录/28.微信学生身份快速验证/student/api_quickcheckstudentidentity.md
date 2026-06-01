# 快速获取学生身份

> 官方文档：[快速获取学生身份](https://developers.weixin.qq.com/miniprogram/dev/server/API/student/api_quickcheckstudentidentity.html)
> 所属分类：[微信学生身份快速验证](../微信学生身份快速验证目录.md)
> 导航路径：微信学生身份快速验证 / 快速获取学生身份
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：quickCheckStudentIdentity

该接口用于获取学生身份。

说明：此处的access_token获取方式，可[点击此处参考详细说明](https://developers.weixin.qq.com/doc/service/guide/dev/)。接口单日限额：100w/日。

如有提额需求可以联系腾讯工作邮箱(wx_city@tencent.com)。

邮件标题：【学生身份快速验证提额需求】+小程序名称+小程序appid

邮件内容：

1. 能力用途与场景
2. 上线时间
3. 需要提额的原因等

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/intp/quickcheckstudentidentity?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：144
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```json
{
    "openid": "",
    "wx_studentcheck_code": ""
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "bind_status": 3,
    "is_student": false
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
