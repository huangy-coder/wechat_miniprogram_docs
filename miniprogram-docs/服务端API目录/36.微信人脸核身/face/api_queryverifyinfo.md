# 查询用户人脸核身真实验证结果

> 官方文档：[查询用户人脸核身真实验证结果](https://developers.weixin.qq.com/miniprogram/dev/server/API/face/api_queryverifyinfo.html)
> 所属分类：[微信人脸核身](../微信人脸核身目录.md)
> 导航路径：微信人脸核身 / 查询用户人脸核身真实验证结果
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：queryVerifyInfo

业务方后台根据人脸核身会话唯一标识 verifyId 字段调用 queryVerifyInfo 接口查询用户人脸核身真实验证结果。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cityservice/face/identify/queryverifyinfo?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Res.verify_ret Enum

人脸核身验证结果

## 5. 注意事项

微信后台校验 `cert_info`、`openid`，不一致则返回对应的 `errcode` 而不是 `verify_ret`，防止身份信息被篡改。

核身通过的判断条件：`errcode = 0` 且 `verify_ret= 10000` 。

`cert_hash` 由 `cert_info` 生成，假设原始

`cert_info: {"cert_type":"IDENTITY_CARD","cert_name":"张三","cert_no":"310101199801011234"}`，其计算规则如下：

对 `cert_info` 中的 `cert_type`、`cert_name`、`cert_no` 字段内容进行标准 `base64`（若存在中文等 Unicode 字符，需先进行 UTF-8 编码）。

按顺序拼接各个字段：`cert_type=xxx&cert_name=xxx&cert_no=xxx`，即`“cert_type=SURFTlRJVFlfQ0FSRA==&cert_name=5byg5LiJ&cert_no=MzEwMTAxMTk5ODAxMDExMjM0”`。

对拼接串进行 SHA256 并输出十六进小写结果得到 cert_hash，即`3c241f7ff324977aeb91f173bb2a7b06569e6fd784d5573db34a636d8671108b`。

## 6. 代码示例

请求示例

```json
{
    "verify_id": "",
    "out_seq_no": "",
    "cert_hash": "",
    "openid": ""
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "",
    "verify_ret": 0
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
