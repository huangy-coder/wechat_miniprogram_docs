# 查询评论列表

> 官方文档：[查询评论列表](https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/comment/api_getcommentreplylist.html)
> 所属分类：[交易保障](../../交易保障目录.md)
> 导航路径：交易保障 / 交易评价管理 / 查询评论列表
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getCommenTreplyList

查询某评价下面所有的评论和回复。（目前开发者创建的第一条回复定义为评论，之后的回复都是基于这条评论去做回复的，未来会进行评论回复的展开）

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/wxaapi/comment/replyandcommentreplylist/get?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：151
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.list Object Payload

评论（评论回复第一条内容）

### Res.list.reply Object Payload

评论

### Res.list.reply.replyContent Object Payload

回复

### Res.list.reply.replyObject Object Payload

评论的内容

### Res.list.commentReplyList(Array) Object Payload

回复（评论回复第二条及之后的所有集合）

### Res.list.commentReplyList(Array).commentReplyContent Object Payload

回复

### Res.list.commentReplyList(Array).commentReplyObject Object Payload

评论的内容

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

请求示例

```bash
GET https://api.weixin.qq.com/wxaapi/comment/replyandcommentreplylist/get?commentId=123456&access_token=xxxx
```

返回示例

```json
{
  errcode: 0,
  list: {
    reply: {  // 评论（评论回复第一条内容）
      commentId: '123', 
      replyId: '1'
      createTime: '1669032337',
      updateTime: '1669032341',
      replyContent: { content: '999' },
      replyObject: {
        nickname: '小程序名称',
        imgUrl: 'http://xxx/xx'
      },
    },
    commentReplyList: [ // 回复（评论回复第二条及之后的所有集合）
      {
        commentId: '12345',
        commentReplyId: '1'
        createTime: '1669032388',
        updateTime: '1669032392',
        commentReplyContent: { content: 'uuuuuuuuu' },
        commentReplyObject: { nickname: '啊哈', imgUrl: 'xxx' },
      }
    ]
  }
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。
