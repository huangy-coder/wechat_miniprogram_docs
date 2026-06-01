# 校验实名信息

> 官方文档：[校验实名信息](https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/basic/api_checkrealnameinfo.html)
> 所属分类：[城市服务](../../城市服务目录.md)
> 导航路径：城市服务 / 基础能力 / 校验实名信息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：checkrealnameinfo

业务方页面获得code之后，需要通过该接口进行实名信息的校验。校验完成后，业务方再根据具体情况，完成自有的业务流程。

城市服务实名信息校验流程请参考[此文档](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/cityservice/cityservice-checkrealnameinfo)

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/intp/realname/checkrealnameinfo?access_token=ACCESS_TOKEN
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

### Res.verify_openid Enum

openid 验证结果，有多个结果时用分号;连接

### Res.verify_real_name Enum

real_name 校验结果，当verify_openid 为V_OP_NM_MA 时返回

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

本接口无代码示例

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
