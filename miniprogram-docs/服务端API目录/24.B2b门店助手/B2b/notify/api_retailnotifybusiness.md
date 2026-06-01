# 模板消息列表及下发

> 官方文档：[模板消息列表及下发](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b/notify/api_retailnotifybusiness.html)
> 所属分类：[B2b门店助手](../../B2b门店助手目录.md)
> 导航路径：B2b门店助手 / 消息触达 / 模板消息列表及下发
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：retailNotifyBusiness

该接口用于下发模板消息。

### 模板列表及发送频次

1. 门店物料申请进度通知（不限下发次数）
2. 门店订单发货通知（不限下发次数）
3. 门店订单派送通知（不限下发次数）
4. 门店认证进度通知（不限下发次数）
5. 门店任务进展通知（单门店可被发送上限：1次/日）
6. 优惠券到期提醒（单门店可被发送上限：4次/月）
7. 积分到期提醒（单门店可被发送上限：4次/月）
8. 兑换券到期提醒（单门店可被发送上限：4次/月）
9. 门店调研通知（单门店可被发送上限：4次/月）
10. 订单受理结果通知（不限制下发次数）
11. 订单退款进度通知（不限制下发次数）
12. 退货申请受理通知（不限制下发次数）
13. 订单变动通知（不限制下发次数）
14. 订单签收通知（不限制下发次数）
15. 验证码通知（不限制下发次数）
16. 满意度评价提醒（不限制下发次数）
17. 月度账单提醒（不限制下发次数）
18. 协议签约审核结果通知（不限制下发次数）
19. 电子券已核销通知（不限制下发次数）
20. 解绑通知（不限制下发次数）

**新增模板需求可填写链接**[B2b门店助手模板新增需求](https://wj.qq.com/s2/14907941/64ff/?wj_lang=zhs)

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/business/retailnotifybusiness?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：158
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

```json
{
    "type": 0,
    "to_user_list": [
        ""
    ],
    "content": ""
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

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
