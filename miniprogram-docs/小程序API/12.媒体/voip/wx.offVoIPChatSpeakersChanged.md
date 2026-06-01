# wx.offVoIPChatSpeakersChanged(function listener)

> 官方文档：[wx.offVoIPChatSpeakersChanged(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.offVoIPChatSpeakersChanged.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 实时语音 / wx.offVoIPChatSpeakersChanged
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.9.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.9.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

> 相关文档: [多人音视频对话](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/voip-chat.html)

## 功能描述

移除实时语音通话成员通话状态变化事件的监听函数

## 参数

### function listener

onVoIPChatSpeakersChanged 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```js
const listener = function (res) { console.log(res) }

wx.onVoIPChatSpeakersChanged(listener)
wx.offVoIPChatSpeakersChanged(listener) // 需传入与监听时同一个的函数对象
```
