# 查询CDN日志下载链接列表

> 官方文档：[查询CDN日志下载链接列表](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/usagedata/api_getcdnlogs.html)
> 所属分类：[短剧媒资管理](../../短剧媒资管理目录.md)
> 导航路径：短剧媒资管理 / 数据统计 / 查询CDN日志下载链接列表
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getCdnLogs

查询域名的 CDN 访问日志的下载链接。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/sec/vod/getcdnlogs?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：153
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.domestic_cdn_logs Object Payload

国内CDN节点的日志下载列表。

## 4. 注意事项

1. 可以查询最近30天内的 CDN 日志下载链接，单次查询的时间跨度不超过48小时。
2. 日志文件以小时为单位产生，但一个小时内可能会产生多个文件，每个文件对应一个域名，平台有可能使用多个域名分发。若某一个小时没有CDN访问，不会生成日志文件。
3. CDN 日志下载链接的有效期为24小时。
4. 日志字段依次为：请求时间、客户端 IP、访问域名、文件路径、字节数、省级编码、运营商编码、 HTTP 状态码、referer、Request-Time、 UA、range、HTTP Method、协议标识、缓存 HIT / MISS， 日志数据打包存在延迟，正常情况下3小时后数据包趋于完整日志中的字节数为应用层数据大小，未考虑网络协议包头、加速重传等开销，因此与计费数据存在一定差异。
5. CDN日志中记录的下行字节数统计而来的流量数据，是应用层数据。在实际网络传输中，产生的网络流量要比纯应用层流量多5%-15%，比如TCP/IP协议的包头消耗、网络丢包重传等，这些无法被应用层统计到。在业内标准中，计费用流量一般在应用层流量的基础上加上上述开销，媒资管理服务中计费的加速流量约为日志计算加速流量的110%。

#### 省份映射

22：北京；86：内蒙古；146：山西；1069：河北；1177：天津；119：宁夏；152：陕西；1208：甘肃；1467：青海；1468：新疆；145：黑龙江；1445：吉林；1464：辽宁；2：福建；120：江苏；121：安徽；122：山东；1050：上海；1442：浙江；182：河南；1135：湖北；1465：江西；1466：湖南；118：贵州；153：云南；1051：重庆；1068：四川；1155：西藏；4：广东；173：广西；1441：海南；0：其他；1：港澳台；-1：海外。

#### 运营商映射

2：中国电信；26：中国联通；38：教育网；43：长城宽带；1046：中国移动；3947：中国铁通；-1：海外运营商；0：其他运营商。

## 5. 代码示例

请求示例

```json
{
    "start_time": 1711589350,
    "end_time": 1711632520,
}
```

返回示例

```json
{
    "domestic_cdn_logs": [
        {
            "date": "2024-03-28",
            "end_time": 1711627199,
            "name": "2024032819-1500020822.vod2.myqcloud.com-mainland",
            "start_time": 1711623600,
            "url": "https://log-download.cdn.qcloud.com/20240328/19/2024032819-1500020822.vod2.myqcloud.com.gz?st=WdyksvfNz23NWKgEvcLQ&e=1711715411"
        },
        {
            "date": "2024-03-28",
            "end_time": 1711623599,
            "name": "2024032818-1500020822.vod2.myqcloud.com-mainland",
            "start_time": 1711620000,
            "url": "https://log-download.cdn.qcloud.com/20240328/18/2024032818-1500020822.vod2.myqcloud.com.gz?st=QmphynCTcO1G23-Ol-SlAg&e=1711715411"
        }
    ],
    "errcode": 0,
    "errmsg": "ok",
    "total_count": 2
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
