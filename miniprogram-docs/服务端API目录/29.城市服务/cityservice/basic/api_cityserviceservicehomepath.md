# 获取城市服务限定页面链接

> 官方文档：[获取城市服务限定页面链接](https://developers.weixin.qq.com/miniprogram/dev/server/API/cityservice/basic/api_cityserviceservicehomepath.html)
> 所属分类：[城市服务](../../城市服务目录.md)
> 导航路径：城市服务 / 基础能力 / 获取城市服务限定页面链接
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：cityserviceservicehomepath

本接口用于获取城市服务限定页面链接

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cityservice/getservicepath?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：22、105
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.ext_params(Array) Object Payload

附加参数，包括关键字等其他参数，page_type为5时必填

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Body.page_type Enum

获取城市服务路径类型

### Body.src_channel Enum

跳转来源渠道

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

### 6.1 城市服务首页示例

请求示例

```json
{
    "page_type": 1,
    "src_channel": 0,
    "city_name": "广州"
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "成功"
    "path": "XXX",
    "business_type": "xxd"
}
```

效果参考


### 6.2 专题页面示例

请求示例

```json
{
    "page_type": 3,
    "src_channel": 0,
    "city_name": '广州',
    "content_name": '购房落户'
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "成功",
    "path": "XXX",
    "bussiness_type": "xxd"
}
```

效果参考


### 6.3 服务列表页示意

请求示例

```json
{
    "city_name":"广州",
    "page_type":5,
    "src_channel":1,
    "ext_params":[
        {
            "key":"keyword",
            "value":"挂号就诊"
        }
    ]
 }
```

返回示例

```json
{
    "errcode":0,
    "errmsg":"ok",
    "path":"path/xxx/xxx",
    "app_id":"wx322xxxx",
    "username":"gh_xxx"
 }
```

效果参考


### 6.4 服务主页示例

请求示例

```json
{
    "page_type":0,
    "src_channel":0,
    "service_id":1001344,
    " params ": "[
                    { \"key\":\"type\",
                      \"value\":\"11\"},
                        { 
                            \"key\":\"dd\",
                            \"value\":\"23\"
                        }]" 
 }
```

返回示例

```json
{
    "errcode":0,
    "errmsg":"成功",
    "path":"XXX",
    "query_string":"xxx”",
    "business_type":"xxd”"
}
```

效果参考


## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
