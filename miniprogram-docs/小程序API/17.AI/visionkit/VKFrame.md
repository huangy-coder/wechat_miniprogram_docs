# VKFrame

> 官方文档：[VKFrame](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKFrame
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

vision kit 会话对象。

## 属性

### number timestamp

生成时间，单位:纳秒(ns)

### VKCamera camera

相机对象

## 方法

### Object VKFrame.getCameraTexture(WebGLRenderingContext gl)

获取当前帧纹理，目前只支持 YUV 纹理。

### ArrayBuffer VKFrame.getCameraBuffer(number width, number height)

获取当前帧 rgba buffer。iOS 端微信在 v8.0.20 开始支持，安卓端微信在 v8.0.30 开始支持。按 aspect-fill 规则裁剪，此接口要求在创建 VKSession 对象时必须传入 gl 参数。此接口仅建议拿来做帧分析使用，上屏请使用 getCameraTexture 来代替。

### ArrayBuffer VKFrame.getCameraJpgBuffer(number width, number height, number quality)

获取当前帧的 jpg 信息Buffer。安卓微信 8.0.49 开始支持，iOS微信 8.0.49 开始支持。

### Float32Array VKFrame.getDisplayTransform()

获取纹理调整矩阵。默认获取到的纹理是未经裁剪调整的纹理，此矩阵可用于在着色器中根据帧对象尺寸对纹理进行裁剪。

### Object VKFrame.getDepthBuffer()

获取每帧的深度图信息Buffer。安卓微信 8.0.38 开始支持，iOS微信 8.0.39 开始支持。

### Object VKFrame.getLegSegmentBuffer()

获取每帧的腿部分割信息Buffer，安卓微信 8.0.43，iOS微信 8.0.43 开始支持。
