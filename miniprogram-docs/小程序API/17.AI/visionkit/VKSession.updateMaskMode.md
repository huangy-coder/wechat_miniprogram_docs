# VKSession.updateMaskMode(Object object)

> 官方文档：[VKSession.updateMaskMode(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.updateMaskMode.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKSession / VKSession.updateMaskMode
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.2.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [3.2.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

设置裁剪相关配置，要求调 [wx.createVKSession](wx.createVKSession.md) 时使用 shoe。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| useMask | boolean |   | 是 | 设置是否开启试鞋，返回腿部遮挡纹理 |
