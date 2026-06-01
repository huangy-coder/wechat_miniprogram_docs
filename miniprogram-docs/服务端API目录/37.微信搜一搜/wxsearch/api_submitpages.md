# 搜一搜数据推送

> 官方文档：[搜一搜数据推送](https://developers.weixin.qq.com/miniprogram/dev/server/API/wxsearch/api_submitpages.html)
> 所属分类：[微信搜一搜](../微信搜一搜目录.md)
> 导航路径：微信搜一搜 / 搜一搜数据推送
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：submitpages

小程序可以通过该功能推送优质内容的页面路径、参数和结构化数据等信息，让微信搜索可以更及时地收录到小程序内容，推送的内容将会被用于微信搜索结果展示，详情参考 [内容接入](https://developers.weixin.qq.com/miniprogram/introduction/widget/we-search/WXAPAGES)。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/search/wxaapi_submitpages?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：search.submitPages
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.pages(Array) Object Payload

请求提交的小程序页面信息数组，一次可提交多个页面的信息。（注意：path+query标识唯一一个页面，微信侧会使用这个信息构造唯一id）

### Body.pages(Array).data_list Object Payload

小程序页面的数据，一个页面可以同时提交多个结构化信息

### Body.pages(Array).data_list .author Object Payload

作者信息，推荐医疗类填写医生信息

### Body.pages(Array).data_list .video Object Payload

视频

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Body.pages(Array).data_list .@type Enum

数据结构类型，用于标识目标业务系统

### Body.pages(Array).data_list .update Enum

更新字段；内容更新按照新增处理，如果页面路径（path+query）相同，微信会做覆盖更新。

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

请求示例

```json
{
    "pages": [
        {
            "path": "",
            "query": "",
            "data_list": [
                {
                    "@type": "",
                    "update": 0,
                    "content_id": "",
                    "page_type": 0,
                    "h5_url": "",
                    "title": "",
                    "abstract": [
                        ""
                    ],
                    "referer": "",
                    "cover_img_url": "",
                    "mainbody": "",
                    "author": {
                        "author_name": "",
                        "author_title": "",
                        "author_portrait": ""
                    },
                    "video": [
                        {
                            "video_title": "",
                            "video_length": 0,
                            "video_img": ""
                        }
                    ],
                    "time_publish": 0,
                    "time_modify": 0,
                    "extra_info": {}
                }
            ]
        }
    ]
}
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": ""
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。
