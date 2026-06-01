# 审核状态事件

> 官方文档：[审核状态事件](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/mini_drama/drama_review_status_event.html)
> 所属分类：[事件通知](../事件通知目录.md)
> 导航路径：事件通知 / 短剧媒资管理 / 审核状态事件
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

如果开发者是小程序商家，请移步：[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)

如果开发者是服务商第三方平台，请移步：[消息与事件接收配置](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/operation/thirdparty/prepare.html#_6%E3%80%81%E6%B6%88%E6%81%AF%E4%B8%8E%E4%BA%8B%E4%BB%B6%E6%8E%A5%E6%94%B6%E9%85%8D%E7%BD%AE)

#### 请求参数

| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drama_id | number | 是 | 剧目id。 |
| audit_detail | DramaAuditDetail | 是 | 剧目审核结果，单独每一集的审核结果可以根据drama_id查询剧集详情得到。 |

#### 推送示例

```xml
<xml>
    <ToUserName>gh_abcdefg</ToUserName>
    <FromUserName>oABCD</FromUserName>
    <CreateTime>12344555555</CreateTime>
    <MsgType>event</MsgType>
    <Event>secvod_audit_event</Event>
    <audit_event>
        <drama_id>20001</drama_id>
        <audit_detail>
            <status>3</status>
            <audit_type>0</audit_type>
            <create_time>168625255</create_time>
            <audit_time>168626255</audit_time>
        </audit_detail>
    </audit_event>
</xml>
```
