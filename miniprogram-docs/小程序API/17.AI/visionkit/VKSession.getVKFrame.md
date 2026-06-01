# VKFrame VKSession.getVKFrame(number width, number height)

> 官方文档：[VKFrame VKSession.getVKFrame(number width, number height)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.getVKFrame.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKSession / VKSession.getVKFrame
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.20.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

获取帧对象，每调用一次都会触发一次帧分析过程。目前 VKSession 相机的最大帧数是 30 fps，因此调用 getVKFrame 的频率也可以限制在 30 fps，以减少渲染开销。

## 参数

### number width

宽度

### number height

高度

## 返回值

### VKFrame

帧对象
