# 获取直播间列表和回放

> 官方文档：[获取直播间列表和回放](https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_getliveinfo.html)
> 所属分类：[小程序直播](../../小程序直播目录.md)
> 导航路径：小程序直播 / 直播间管理 / 获取直播间列表和回放
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getLiveInfo

该接口用于获取直播间列表及直播间信息。也可以用来获取已结束直播间的回放源视频（一般在直播结束后10分钟内生成，源视频无评论等内容）。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/business/getliveinfo?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：liveBroadcast.getLiveInfo
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：52
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.room_info(Array) Object Payload

action="get_replay"不返回。

### Res.live_replay(Array) Object Payload

action="get_replay"才返回。

### Res.room_info(Array).goods Object Payload

商品

## 4. 注意事项

调用额度：100000次/一天

## 5. 代码示例

请求示例

{
"start": 0, // 起始拉取房间，start = 0 表示从第 1 个房间开始拉取
"limit": 10 // 每次拉取的个数上限，不要设置过大，建议 100 以内
}

返回示例

{
"errcode": 0, // 错误码，0代表成功，1代表未创建直播间
"errmsg": "ok", // 错误信息
"total":1,
"room_info":[{
"name":"直播房间名"
"roomid": 1,
"cover_img":"http://http://mmbiz.qpic.cn/mmbiz_jpg\Rl1RuuhdstSfZa8EEljedAYcbtX3Ejpdl2et1tPAQ37bdicnxoVialDLCKKDcPBy8Iic0kCiaiaalXg3EbpNKoicrweQ/0?wx_fmt=jpeg",
"share_img":"http://http://mmbiz.qpic.cn/mmbiz_jpg\Rl1RuuhdstSfZa8EEljedAYcbtX3Ejpdl2et1tPAQ37bdicnxoVialDLCKKDcPBy8Iic0kCiaiaalXg3EbpNKoicrweQ/0?wx_fmt=jpeg",
"live_status": 101,
"start_time": 1568128900,
"end_time": 1568131200,
"anchor_name":"里斯",
"goods":[{
"cover_img":"http://http://mmbiz.qpic.cn/mmbiz_jpg/Rl1RuuhdstSfZa8EEljedAYcbtX3Ejpdl2et1tPAQ37bdicnxoVialDLCKKDcPBy8Iic0kCiaiaalXg3EbpNKoicrweQ/0?wx_fmt=jpeg",
"url":"pages/index/index.html",
"name":"茶杯",
"price": 1889, // 价格（分）
"price2": 0,
"price_type": 1, // 价格类型，1：一口价（只需要传入price，price2不传） 2：价格区间（price字段为左边界，price2字段为右边界，price和price2必传） 3：显示折扣价（price字段为原价，price2字段为现价， price和price2必传）
"goods_id": 256, // 商品id
"third_party_appid": "wx3d0fae56402d8a81" //第三方商品appid ,当前小程序商品则为空
}],
"live_type": 0, // 直播类型，1 推流 0 手机直播
"close_like": 0, // 是否关闭点赞 【0：开启，1：关闭】（若关闭，观众端将隐藏点赞按钮，直播开始后不允许开启）
"close_goods": 0, // 是否关闭货架 【0：开启，1：关闭】（若关闭，观众端将隐藏商品货架，直播开始后不允许开启）
"close_comment": 0, // 是否关闭评论 【0：开启，1：关闭】（若关闭，观众端将隐藏评论入口，直播开始后不允许开启）
"close_kf": 1, // 是否关闭客服 【0：开启，1：关闭】 默认关闭客服（直播开始后允许开启）
"close_replay": 1, // 是否关闭回放 【0：开启，1：关闭】默认关闭回放（直播开始后允许开启）
"is_feeds_public": 0, // 是否开启官方收录，1 开启，0 关闭
"creater_openid": "oawjt4t9NWZV2BYaEPA89sh1XblE", // 创建者openid
"feeds_img": "XXX" // 官方收录封面
}]
}

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
