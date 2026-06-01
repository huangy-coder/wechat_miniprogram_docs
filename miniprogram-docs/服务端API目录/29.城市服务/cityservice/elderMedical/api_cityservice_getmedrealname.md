# 查询用户实名API

> 官方文档：[查询用户实名API](https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/elderMedical/api_cityservice_getmedrealname.html)
> 所属分类：[城市服务](../../城市服务目录.md)
> 导航路径：城市服务 / 微信长辈就医 / 查询用户实名API
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：cityservice_getmedrealname

查询老年患者实名信息

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cityservice/getmedrealname?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：134
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

用户实名数据属于敏感信息，不能以明文形式传输，所以平台返回的实名信息是经过对称加密后的base64字符串，平台会给进驻的每家医院分配长度为32位(256bit)密钥，解密后可获得明文，默认使用的加解密算法为：AES_256_ECB_PKCS7Padding；解密示例代码[下载](https://share.weiyun.com/HPYWwdQU)

**解密后的实名明文**

```json
{"real_name":"张三","id_card_no":"45088100000000","id_card_type":1,"phone":"13800000138","timestamp":1661420431,"phone_country_code":"86"}
```

**实名信息字段说明**

| 字段 | 字段名 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- |
| real_name | 姓名 | string | 是 |   |
| id_card_no | 证件号 | string | 是 |   |
| id_card_type | 证件类型 | int32 | 是 | 1 居民身份证；<br>4 澳门居民往来内地通行证；<br>5 台湾居民往来内地通行证；<br>6香港居民往来内地通行证。 |
| phone | 电话号码 | string | 是 |   |
| timestamp | 时间戳 | int64 | 是 |   |

## 5. 代码示例

请求示例

```json
{
  "app_id": "wx23dde3xd34569cba",
  "open_id": "ont-9vr_is4GBmeuh_xy1YHidhgY",
  "wxmed_authcode": "BMUewIb9qr2GMDeInZKOBg.."
}
```

返回示例

```json
{
  "app_id":"",
  "openid_id":""
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
