# 媒资上传完成事件

> 官方文档：[媒资上传完成事件](https://developers.weixin.qq.com/miniprogram/dev/server/event_push/mini_drama/asset_upload_completion_event.html)
> 所属分类：[事件通知](../事件通知目录.md)
> 导航路径：事件通知 / 短剧媒资管理
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

如果开发者是小程序商家，请移步：[消息推送](https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html)

如果开发者是服务商第三方平台，请移步：[消息与事件接收配置](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/operation/thirdparty/prepare.html#_6%E3%80%81%E6%B6%88%E6%81%AF%E4%B8%8E%E4%BA%8B%E4%BB%B6%E6%8E%A5%E6%94%B6%E9%85%8D%E7%BD%AE)

#### 请求参数

| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| media_id | number | 是 | 媒资id。 |
| source_context | string | 否 | 透传上传接口中开发者设置的值。 |
| errcode | number | 是 | 错误码，上传失败时该值非0。 |
| errmsg | string | 否 | 错误提示。 |

#### 推送示例

```xml
<xml>
    <ToUserName>gh_abcdefg</ToUserName>
    <FromUserName>oABCD</FromUserName>
    <CreateTime>12344555555</CreateTime>
    <MsgType>event</MsgType>
    <Event>secvod_upload_event</Event>
    <upload_event>
        <media_id>20001</media_id>
        <source_context>abc12232</source_context>
        <errcode>0</errcode>
        <errmsg>OK</errmsg>
    </upload_event>
</xml>
```
