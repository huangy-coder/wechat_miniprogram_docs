# 使用AppSecret重置API调用次数

> 官方文档：[使用AppSecret重置API调用次数](https://developers.weixin.qq.com/miniprogram/dev/server/API/openApi-mgnt/api_clearquotabyappsecret.html)
> 所属分类：[openApi管理](../openApi管理目录.md)
> 导航路径：openApi管理 / 使用AppSecret重置API调用次数
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：clearQuotaByAppSecret

本接口是通过AppSecret清空服务端接口的每日调用接口次数。

适用的账号类型为：公众号/服务号/小程序/小游戏/微信小店/带货助手/视频号助手/联盟带货机构/移动应用/网站应用/多端应用/第三方平台

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/clear_quota/v2
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

无

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1、该接口通过 appsecret 调用，解决了 accesss_token 耗尽无法调用「重置 API 调用次数」的问题。

2、每个账号每月使用「重置 API 调用次数」与本接口共10次清零操作机会，清零生效一次即用掉一次机会；

3、由于指标计算方法或统计时间差异，实时调用量数据可能会出现误差，一般在1%以内

4、该接口仅支持POST调用

5、如果要清除 [获取令牌接口](https://developers.weixin.qq.com/doc/oplatform/openApi/ticket-token/api_getcomponentaccesstoken) 调用次数或者以服务商身份代商家清除公众号或者小程序调用次数，则需要使用[使用AppSecret重置第三方平台API调用次数接口](https://developers.weixin.qq.com/doc/oplatform/openApi/openapi/api_componentclearquota_v2)。

## 5. 代码示例

请求示例

```bash
POST  https://api.weixin.qq.com/cgi-bin/clear_quota/v2?appid=wx888888888888&appsecret=xxxxxxxxxxxxxxxxxxxxxxxx
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

| 小程序 | 公众号 | 服务号 | 小游戏 | 微信小店 | 联盟带货机构 | 带货助手 | 小店供货商 | 移动应用 | 网站应用 | 视频号助手 | 多端应用 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

- ✔：该账号可调用此接口。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
