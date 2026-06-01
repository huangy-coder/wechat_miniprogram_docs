# 发送客服消息

> 官方文档：[发送客服消息](https://developers.weixin.qq.com/miniprogram/dev/server/API/kf-mgnt/kf-message/api_sendcustommessage.html)
> 所属分类：[小程序客服](../../小程序客服目录.md)
> 导航路径：小程序客服 / 客服消息 / 发送客服消息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：sendCustomMessage

本接口用于发送多种类型的客服消息，主要应用在有人工消息处理环节的场景。

当用户和应用产生特定动作的交互时，微信将会把消息数据推送给开发者，开发者可以在一段时间内（目前为48小时）调用客服接口，通过POST一个JSON数据包来发送消息给普通用户。

目前允许的动作列表如下（公众平台会根据运营情况更新该列表，不同动作触发后，允许的客服接口

1. 用户发送信息
2. 点击自定义菜单（仅有点击推事件、扫码推事件、扫码推事件且弹出“消息接收中”提示框这3种菜单类型是会触发客服接口的）
3. 关注公众号
4. 扫描二维码

各场景的客服消息下发规则：

| 场景 | 下发额度 | 额度有效期 |
| --- | --- | --- |
| 用户发送消息 | 5条 | 48小时 |
| 点击自定义菜单 | 3条 | 1分钟 |
| 关注公众号 | 3条 | 1分钟 |
| 扫描二维码 | 3条 | 1分钟 |

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=ACCESS_TOKEN
```

> **支持加密请求：** 本接口支持服务通信二次加密和签名，可有效防止数据篡改与泄露。[查看详情](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature)

### 云调用

- 调用方法：customerServiceMessage.send
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：1、6、19、100-101
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.text Object Payload

文本消息，msgtype="text" 时必填

### Body.image Object Payload

图片消息，msgtype="image" 时必填

### Body.voice Object Payload

语音消息，msgtype="voice" 时必填

### Body.video Object Payload

视频消息，msgtype="video" 时必填

### Body.music Object Payload

音乐消息，msgtype="music" 时必填

### Body.news Object Payload

图文消息（点击跳转到外链），msgtype="news" 时必填

### Body.mpnews Object Payload

图文消息（点击跳转到图文消息页面），msgtype="mpnews" 时必填，图文消息条数限制在1条以内，注意，如果图文数超过1，则将会返回错误码45008。（草稿灰度完成后，此类型不再支持）

### Body.mpnewsarticle Object Payload

图文消息（点击跳转到图文消息页面），msgtype="mpnewsarticle" 时必填，使用通过 “发布” 系列接口得到的 article_id

### Body.msgmenu Object Payload

菜单消息，msgtype="msgmenu" 时必填

### Body.wxcard Object Payload

卡券信息，msgtype="wxcard"时必填

### Body.miniprogrampage Object Payload

小程序消息，msgtype="miniprogrampage"时必填

### Body.customservice Object Payload

以某个客服账号来发消息

### Body.aimsgcontext Object Payload

ai 消息上下文

### Body.news.articles(Array) Object Payload

图文消息条数限制在1条以内

### Body.msgmenu.list(Array) Object Payload

菜单内容

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

- 发送文本消息时，支持添加可跳转小程序的文字连接.
- data-miniprogram-appid 项，填写小程序appid，则表示该链接跳转小程序
- data-miniprogram-path项，填写小程序路径，路径与app.json中保持一致，可带参数；
- 对于不支持 data-miniprogram-appid 项的客户端版本（6.5.16 以下），如果有 herf 项，则仍然保持跳 href 中的链接；
- 小程序发带小程序文字链的文本消息，data-miniprogram-appid必须是该小程序的appid

## 5. 代码示例

### 5.1 发送文本消息

请求示例

```json
{
    "touser":"OPENID",
    "msgtype":"text",
    "text":
    {
         "content":`文本内容<a href="http://www.qq.com" data-miniprogram-appid="appid" data-miniprogram-path="pages/index/index">点击跳小程序</a>`
    },
    "customservice":{
         "kf_account": "test1@kftest"
    }
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.2 发送图片消息

请求示例

```json
{
    "touser":"OPENID",
    "msgtype":"image",
    "image":
    {
      "media_id":"MEDIA_ID"
    }
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.3 发送语音消息

请求示例

```json
{
    "touser":"OPENID",
    "msgtype":"voice",
    "voice":
    {
      "media_id":"MEDIA_ID"
    }
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.4 发送视频消息

请求示例

```json
{
    "touser":"OPENID",
    "msgtype":"video",
    "video":
    {
      "media_id":"MEDIA_ID",
      "thumb_media_id":"MEDIA_ID",
      "title":"TITLE",
      "description":"DESCRIPTION"
    }
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.5 发送音乐消息

请求示例

```json
{
    "touser":"OPENID",
    "msgtype":"music",
    "music":
    {
      "title":"MUSIC_TITLE",
      "description":"MUSIC_DESCRIPTION",
      "musicurl":"MUSIC_URL",
      "hqmusicurl":"HQ_MUSIC_URL",
      "thumb_media_id":"THUMB_MEDIA_ID" 
    }
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.6 发送外链图文消息

请求示例

```json
{
    "touser":"OPENID",
    "msgtype":"news",
    "news":{
        "articles": [
         {
             "title":"Happy Day",
             "description":"Is Really A Happy Day",
             "url":"URL",
             "picurl":"PIC_URL"
         }
         ]
    }
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.7 发送公众号图文消息（废弃）

请求示例

```json
{
    "touser":"OPENID",
    "msgtype":"mpnews",
    "mpnews":
    {
         "media_id":"MEDIA_ID"
    }
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.8 发送公众号图文消息

请求示例

```json
{
    "touser":"OPENID",
    "msgtype":"mpnewsarticle",
    "mpnewsarticle": {
         "article_id":"ARTICLE_ID"
    }
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.9 发送菜单消息

请求示例

```json
{
  "touser": "OPENID",
  "msgtype": "msgmenu",
  "msgmenu": {
    "head_content": "您对本次服务是否满意呢? ",
    "list": [
      {
        "id": "101",
        "content": "满意"
      },
      {
        "id": "102",
        "content": "不满意"
      }
    ],
    "tail_content": "欢迎再次光临"
  }
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.10 发送卡券消息

请求示例

```json
{
  "touser":"OPENID", 
  "msgtype":"wxcard",
  "wxcard":
  {              
   "card_id":"123dsdajkasd231jhksad"        
   }
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.11 发送小程序消息

请求示例

```json
{
    "touser":"OPENID",
    "msgtype":"miniprogrampage",
    "miniprogrampage":
    {
        "title":"title",
        "appid":"appid",
        "pagepath":"pagepath",
        "thumb_media_id":"thumb_media_id"
    }
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

| 小程序 | 公众号 | 服务号 | 小游戏 |
| --- | --- | --- | --- |
| ✔ | 仅认证 | 仅认证 | ✔ |

- ✔：该账号可调用此接口。
- 仅认证：表示仅允许企业主体已认证账号调用，未认证或不支持认证的账号无法调用。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
