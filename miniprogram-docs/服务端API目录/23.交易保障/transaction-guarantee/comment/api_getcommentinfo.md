# 查询评价详情

> 官方文档：[查询评价详情](https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/comment/api_getcommentinfo.html)
> 所属分类：[交易保障](../../交易保障目录.md)
> 导航路径：交易保障 / 交易评价管理 / 查询评价详情
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getCommentInfo

查询某条评价的详细内容

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/wxaapi/comment/commentinfo/get?access_token=ACCESS_TOKEN
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

### Res.info Object Payload

评价的信息

### Res.processInfo Object Payload

进度条的信息（只有差评才会有）

### Res.oldComment Object Payload

旧评价的信息(只有改评的新评价才有)

### Res.info.content Object Payload

评价

### Res.info.content.orderInfo Object Payload

商家订单信息

### Res.info.content.productInfo Object Payload

评价商品信息

### Res.info.content.productInfo.productList(Array) Object Payload

商品列表

### Res.info.content.userInfo Object Payload

评价用户信息

### Res.info.content.bizInfo Object Payload

商家小程序信息

### Res.info.content.content Object Payload

评价内容

### Res.info.content.content.media(Array) Object Payload

评价的媒体文件，如图片、视频

### Res.processInfo.actionList(Array) Object Payload

进度的具体状态,数组类型，从数组最后往前数有updateTime的就是当前状态

### Res.oldComment.content Object Payload

评论的内容

### Res.oldComment.content.media(Array) Object Payload

评价的多媒体内容,跟上面提到的媒体结构一致

## 4. 枚举信息

### Res.processInfo.actionList(Array).type Enum

进度的类型

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

请求示例

```bash
GET https://api.weixin.qq.com/wxaapi/comment/commentinfo/get?commentId=123456&access_token=xxxxxx
```

返回示例

```json
{
  info: {
    content: {
      commentId: '123',
      createTime: '1669031402',
      userInfo: { openid: 'xxx', headImg: '', nickName: '啊哈' },
      content: {
        txt: '突突突突突突有',
        media: [
          {
            video:
              'https://xxx/xx',
            videoCover: 'http://xxx/xx',
            videoDuration: 11
          }
        ]
      },
      bizInfo: {
        appid: "wx1234567890",
        headImg: "http://wx.qlogo.cn/mmhead/xxxxxx",
        nickName: "xxx的小商店"
      },
      score: 200, // 评价分数、星级，这里200分对应2星
      orderId: 'payorder@xxxx',
      wxPayId: 'xxxx',
      orderInfo: {
        busiOrderId: 'xxxxxx'
      },
      productInfo: {
        productList: [{
          name: "我是描述",
          picUrl: "https://xxxxx/x"
        }]
      },
      payTime: '1669030760',
      amount: 1,
    }
  },
  processInfo: { // 订单处理进度数据
    commentId: 'xxx',
    actionList: [
      {
        type: 1,
        updateTime: 1669031402,
      },
      { type: 2 },
      { type: 3 }
    ]
  },
  oldComment: {
    commentId: 'xxx',
    content: {},
    score: 100,
    createTime: 11111
  },
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。
