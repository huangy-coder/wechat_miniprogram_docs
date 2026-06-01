# Object VKFrame.getCameraTexture(WebGLRenderingContext gl)

> 官方文档：[Object VKFrame.getCameraTexture(WebGLRenderingContext gl)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.getCameraTexture.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKFrame / VKFrame.getCameraTexture
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.20.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

获取当前帧纹理，目前只支持 YUV 纹理。

## 参数

### WebGLRenderingContext gl

画布

## 返回值

### Object

帧纹理对象

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| yTexture | WebGLTexture | Y 分量纹理 |
| uvTexture | WebGLTexture | UV 分量纹理 |
