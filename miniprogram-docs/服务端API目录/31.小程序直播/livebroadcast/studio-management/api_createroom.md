# 创建直播间

> 官方文档：[创建直播间](https://developers.weixin.qq.com/miniprogram/dev/server/API/livebroadcast/studio-management/api_createroom.html)
> 所属分类：[小程序直播](../../小程序直播目录.md)
> 导航路径：小程序直播 / 直播间管理 / 创建直播间
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：createRoom

调用此接口创建直播间，创建成功后将在直播间列表展示。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxaapi/broadcast/room/create?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：liveBroadcast.createRoom
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

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

{
name: "测试直播房间1", // 房间名字
coverImg: "", // 通过 uploadfile 上传，填写 mediaID
startTime: 1588237130, // 开始时间
endTime: 1588237130 , // 结束时间
anchorName: "zefzhang1", // 主播昵称
anchorWechat: "WxgQiao_04", // 主播微信号
subAnchorWechat: "WxgQiao_03", // 主播副号微信号
createrWechat: 'test_creater', // 创建者微信号
shareImg: "hw7zsntcr0rE-RBfBAaF553DqBk-J02UtWsP8VqrUh3tKu3jO_JwEO8n1cWTJ5TN" , //通过 uploadfile 上传，填写 mediaID
feedsImg: "hw7zsntcr0rE-RBfBAaF553DqBk-J02UtWsP8VqrUh3tKu3jO_JwEO8n1cWTJ5TN", //通过 uploadfile 上传，填写 mediaID
isFeedsPublic: 1, // 是否开启官方收录，1 开启，0 关闭
type: 1 , // 直播类型，1 推流 0 手机直播
closeLike: 0 , // 是否关闭点赞 1：关闭
closeGoods: 0, // 是否关闭商品货架，1：关闭
closeComment: 0 // 是否开启评论，1：关闭
closeReplay: 1 , // 是否关闭回放 1 关闭
closeShare: 0, // 是否关闭分享 1 关闭
closeKf: 0, // 是否关闭客服，1 关闭
}

返回示例

{
"roomId": 33, //房间ID
"errcode": 0,
// 当主播微信号没有在 “小程序直播“ 小程序实名认证 返回该字段
"qrcode_url": "https://res.wx.qq.com/op_res/9rSix1dhHfK4rR049JL0PHJ7TpOvkuZ3mE0z7Ou_Etvjf-w1J_jVX0rZqeStLfwh"
}

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
