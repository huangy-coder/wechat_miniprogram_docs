# VKSession.updateOSDThreshold(number threshold)

> 官方文档：[VKSession.updateOSDThreshold(number threshold)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.updateOSDThreshold.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKSession / VKSession.updateOSDThreshold
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.24.5 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.24.5](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

更新 OSD 识别精确度，要求调 [wx.createVKSession](wx.createVKSession.md) 时传入的 track.OSD 为 true

## 参数

### number threshold

阈值
