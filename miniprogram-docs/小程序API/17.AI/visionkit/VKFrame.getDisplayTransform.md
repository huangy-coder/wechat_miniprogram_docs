# Float32Array VKFrame.getDisplayTransform()

> 官方文档：[Float32Array VKFrame.getDisplayTransform()](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.getDisplayTransform.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKFrame / VKFrame.getDisplayTransform
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.20.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

获取纹理调整矩阵。默认获取到的纹理是未经裁剪调整的纹理，此矩阵可用于在着色器中根据帧对象尺寸对纹理进行裁剪。

## 返回值

### Float32Array

纹理调整矩阵
