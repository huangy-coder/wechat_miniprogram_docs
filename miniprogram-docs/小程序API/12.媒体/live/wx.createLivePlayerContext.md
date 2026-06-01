# LivePlayerContext wx.createLivePlayerContext(string id, Object this)

> 官方文档：[LivePlayerContext wx.createLivePlayerContext(string id, Object this)](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/wx.createLivePlayerContext.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 实时音视频 / wx.createLivePlayerContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [live-player 组件](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html)

## 功能描述

创建 [live-player](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html) 上下文 [LivePlayerContext](LivePlayerContext.md) 对象。建议使用 [wx.createSelectorQuery](../../19.WXML/wx.createSelectorQuery.md) 获取 context 对象。

## 参数

### string id

[live-player](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html) 组件的 id

### Object this

在自定义组件下，当前组件实例的this，以操作组件内 [live-player](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html) 组件

## 返回值

### LivePlayerContext
