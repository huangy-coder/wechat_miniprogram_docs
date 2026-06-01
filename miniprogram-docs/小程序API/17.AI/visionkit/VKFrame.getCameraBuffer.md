# ArrayBuffer VKFrame.getCameraBuffer(number width, number height)

> 官方文档：[ArrayBuffer VKFrame.getCameraBuffer(number width, number height)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.getCameraBuffer.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKFrame / VKFrame.getCameraBuffer
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.24.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

获取当前帧 rgba buffer。iOS 端微信在 v8.0.20 开始支持，安卓端微信在 v8.0.30 开始支持。按 aspect-fill 规则裁剪，此接口要求在创建 VKSession 对象时必须传入 gl 参数。此接口仅建议拿来做帧分析使用，上屏请使用 getCameraTexture 来代替。

## 参数

### number width

宽度，受系统限制，必须是 16 的整数倍

### number height

高度

## 返回值

### ArrayBuffer

帧 rgba buffer
