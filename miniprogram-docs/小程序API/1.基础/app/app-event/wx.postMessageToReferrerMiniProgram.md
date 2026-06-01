# wx.postMessageToReferrerMiniProgram(Object object)

> 官方文档：[wx.postMessageToReferrerMiniProgram(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.postMessageToReferrerMiniProgram.html)
> 所属分类：[基础](../../基础目录.md)
> 导航路径：基础 / 小程序 / 应用级事件 / wx.postMessageToReferrerMiniProgram
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.2.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

向跳转的源小程序发送消息，源小程序可在 [wx.onShow](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/(wx.onShow)) 或 [wx.getEnterOptionsSync](../life-cycle/wx.getEnterOptionsSync.md) 中通过 extraData 接收消息。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| extraData | Object |   | 否 | 需要返回的数据 |

多次调用会覆盖之前传递的消息，通过 [wx.navigateBackMiniProgram](../../../3.跳转/wx.navigateBackMiniProgram.md) 传递 extraData 也会覆盖消息。

在触发返回后传递的消息不会被收到。

如果没有源小程序能够收到消息，会抛出 no referrer 错误。
