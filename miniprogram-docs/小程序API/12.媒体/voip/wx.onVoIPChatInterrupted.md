# wx.onVoIPChatInterrupted(function listener)

> 官方文档：[wx.onVoIPChatInterrupted(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.onVoIPChatInterrupted.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 实时语音 / wx.onVoIPChatInterrupted
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.9.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

> 相关文档: [多人音视频对话](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/voip-chat.html)

## 功能描述

监听被动断开实时语音通话事件。包括小游戏切入后端时断开

## 参数

### function listener

被动断开实时语音通话事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errCode | Number | 错误码 |
| errMsg | String | 调用结果（错误原因） |
