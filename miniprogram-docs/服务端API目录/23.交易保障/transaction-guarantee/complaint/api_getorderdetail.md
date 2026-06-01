# 查询投诉单详情

> 官方文档：[查询投诉单详情](https://developers.weixin.qq.com/miniprogram/dev/server/API/transaction-guarantee/complaint/api_getorderdetail.html)
> 所属分类：[交易保障](../../交易保障目录.md)
> 导航路径：交易保障 / 交易投诉处理 / 查询投诉单详情
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：getOrderDetail

该接口用于查询投诉单详情。

## 1. 调用方式

### HTTPS 调用

```bash
GET https://api.weixin.qq.com/wxaapi/minishop/complaintOrderDetail?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：76
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.complaintOrder Object Payload

complaintOrder

### Res.item Object Payload

投诉进度

### Res.returnBill Object Payload

returnBill

### Res.complaintOrder.customerMaterial Object Payload

投诉信息

## 4. 枚举信息

### Res.complaintOrder.type Enum

投诉问题分类

### Res.complaintOrder.status Enum

投诉单状态

### Res.complaintOrder.appealState Enum

申诉状态

### Res.item.itemType Enum

投诉节点状态

### Res.item.appealItemType Enum

处于申诉阶段节点的申诉状态

### Res.returnBill.orderStatus Enum

运单状态

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

请求示例

```text
GET https://api.weixin.qq.com/wxaapi/minishop/complaintOrderDetail?access_token=ACCESS_TOKEN
```

返回示例

```json
{
    errcode: 0,
    errmsg: "ok",
    complaintOrder: {
        complaintOrderId: 'sadfasdf',//订单id
        openId: 'dfasefasefase', //openId
        createTime: 123124124, //投诉发起时间
        phoneNumber: 156222222, //联系方式
        type: 12,  //投诉问题分类
        status: 101,//投诉单状态，枚举值
        customerMaterial:{
            content: '', //投诉内容
            mediaIdList: ['fsadfasdfsaf'] //投诉内容图片cdn列表
        },
        orderId: '2342', //微信支付订单号
        outTradeNo: 'sdfsfd',   //商家订单号
        productName: 'sdf', //商品名称
        payTime: 123123',   //支付时间
        totalCost: 1213,    //交易金额
        expireTime: 1231231 //投诉单当前状态到期时间,0为不存在
    },
    // 投诉进度
    item:[{
        itemType: 1, //投诉节点状态
        time: 1233234234,  //时间
        phoneNumber: 123123, //手机号
        content: "", //内容
        mediaIdList: ['asdfasdf']  //图片cdn列表
    }],
    returnBill: {
        returnId: '23234234234',    //退货id
        waybillId: 'adfasdf', //运单号
        orderStatus: 4 //运单状态
    }
} 
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。
