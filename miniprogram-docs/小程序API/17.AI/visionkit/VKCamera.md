# VKCamera

> 官方文档：[VKCamera](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKCamera.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKCamera
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

相机对象

## 属性

### Float32Array transform

相机原始的Pose矩阵

### Float32Array viewMatrix

视图矩阵

### Float32Array intrinsics

> 基础库 2.22.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

相机内参，只有 v2 版本支持

## 方法

### Float32Array VKCamera.getProjectionMatrix(number near, number far)

获取投影矩阵
