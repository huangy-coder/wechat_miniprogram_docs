# wx.onAudioInterruptionBegin(function listener)

> 官方文档：[wx.onAudioInterruptionBegin(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAudioInterruptionBegin.html)
> 所属分类：[基础](../../基础目录.md)
> 导航路径：基础 / 小程序 / 应用级事件 / wx.onAudioInterruptionBegin
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.6.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.15.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

监听音频因为受到系统占用而被中断开始事件。以下场景会触发此事件：闹钟、电话、FaceTime 通话、微信语音聊天、微信视频聊天、有声广告开始播放、实名认证页面弹出等。此事件触发后，小程序内所有音频会暂停。

## 参数

### function listener

音频因为受到系统占用而被中断开始事件的监听函数
