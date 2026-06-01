# Object VKFrame.getLegSegmentBuffer()

> 官方文档：[Object VKFrame.getLegSegmentBuffer()](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.getLegSegmentBuffer.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKFrame / VKFrame.getLegSegmentBuffer
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.2.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

获取每帧的腿部分割信息Buffer，安卓微信 8.0.43，iOS微信 8.0.43 开始支持。

## 返回值

### Object

帧深度纹理buffer对象，width * height 大小的 深度值（float32）

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 腿部分割纹理宽 |
| height | number | 腿部分割纹理高 |
| DepthAddress | ArrayBuffer | 腿部分割纹理buffer，width * height 大小的 裁剪值（0 为不是脚，越靠近 255 越接近腿部区域）（uint8） |
