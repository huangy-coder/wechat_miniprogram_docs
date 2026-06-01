# 推荐剧目

> 官方文档：[推荐剧目](https://developers.weixin.qq.com/miniprogram/dev/server/API/dramaOthersAPI/api_developersetrecmddrama.html)
> 所属分类：[短剧播放器](../短剧播放器目录.md)
> 导航路径：短剧播放器 / 推荐剧目
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：developerSetRecmdDrama

开启推荐位之后，推荐剧目范围默认为播放小程序所有已授权的剧目。

同时支持开发者设置推荐库，在设置推荐库之后，推荐剧目将从开发者设置的推荐剧目中产生。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxadrama/developersetrecmddrama?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：157
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.list(Array) Object Payload

list

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1. src_appid 和 drama_id 同时为空，代表小程序维度。展示优先级低于剧粒度的设置。
2. 每次设置都会覆盖之前的设置，需要把所有要设置的推荐剧一次加上；list不传或者传空数组，则将记录清空。
3. 所有appid需要合法，不然报错。另外存在所传剧目没有授权给该调用账号的，也会失败报错。
4. list当前的上限是200个。

## 5. 代码示例

请求示例

```json
{

    "entry_type":1, //1-剧结束 2-选集最右侧推荐 3-剧集profile页相关推荐

    "src_appid":"wx94a6522b1d640c3b",

    "drama_id":"666666",

    "list":[

        {"src_appid":"wx4f3ca6d4c2407ccc","drama_id":"266946"},

        {"src_appid":"wx5cefe18a7902141d","drama_id":"236424"}

    ]

}
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

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
