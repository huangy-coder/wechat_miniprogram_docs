# ArrayBuffer VKFrame.getCameraJpgBuffer(number width, number height, number quality)

> 官方文档：[ArrayBuffer VKFrame.getCameraJpgBuffer(number width, number height, number quality)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.getCameraJpgBuffer.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKFrame / VKFrame.getCameraJpgBuffer
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.0.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

获取当前帧的 jpg 信息Buffer。安卓微信 8.0.49 开始支持，iOS微信 8.0.49 开始支持。

## 参数

### number width

宽度

### number height

高度

### number quality

获取纹理质量，(0 - 100)

## 返回值

### ArrayBuffer

jpg buffer
