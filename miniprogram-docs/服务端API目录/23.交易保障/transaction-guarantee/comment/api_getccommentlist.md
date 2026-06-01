# 查询评价列表

> 官方文档：[查询评价列表](https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/comment/api_getccommentlist.html)
> 所属分类：[交易保障](../../交易保障目录.md)
> 导航路径：交易保障 / 交易评价管理 / 查询评价列表
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getCcommentList

查询某小程序下面所有的评价。

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/wxaapi/comment/mpcommentlist/get?access_token=ACCESS_TOKEN
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

### Res.commentList(Array) Object Payload

评价的列表

### Res.commentList(Array).orderInfo Object Payload

商家订单信息

### Res.commentList(Array).userInfo Object Payload

评价用户信息

### Res.commentList(Array).bizInfo Object Payload

商家小程序信息

### Res.commentList(Array).content Object Payload

评价内容

### Res.commentList(Array).content.media Object Payload

评价的媒体文件，如图片、视频, 视频跟图片只能存在一种，不同时存在，如果是图片可以有多张图，如果是视频只会有一个视频

### Res.commentList(Array).extInfo Object Payload

评价额外信息

### Res.commentList(Array).productInfo Object Payload

评价商品信息

### Res.commentList(Array).productInfo.productList Object Payload

商品列表

## 4. 枚举信息

### Body.filterType Enum

过滤的数据类型

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

请求示例

```bash
GET  https://api.weixin.qq.com/wxaapi/comment/mpcommentlist/get?filterType=1&offset=0&limit=8&startTime=1588237130&endTime=1588237131&access_token=xxxx
```

返回示例

```json
{
  errcode: 0,
  success: true,
  commentList: [{
    commentId: "2797755680173111111",
    amount: 100,
    orderId: "payorder@_4200001761202302096311111111",
    payTime: "1675915718",
    wxPayId: "4200001761202302096311111111",
    orderInfo: {
      busiOrderId: 'xxxxxx'
    },
    userInfo: {
      openid: "xxxxxxxxxx",
      headImg: "http://wx.qlogo.cn/mmhead/xxxxxxxxxxx",
      nickName: "test"
    },
    bizInfo: {
        appid: "wx1234567890",
        headImg: "http://wx.qlogo.cn/mmhead/xxxxxxxxxxxx",
        nickName: "xxx"
    },
    score: 200, // 200分对应2星，每100分就是1星
    createTime: "1676351504",
    content: {
      media: [{img: 'http://xxx', thumbImg: 'http://xxx'}],
      txt: "一般吧 我总感觉这个成分很伤皮肤，用了之后一直很干燥，不是很喜欢这款产品"
    },
    extInfo: {
      isAlreadySendTmpl: false,
    },
    productInfo: {
      productList: [
        {
            name: "纸巾一张",
            picUrl: "https://xxxxxx",
        }
      ]
    }
  }],
  total: 3,
  offset: 0,
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。
