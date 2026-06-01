# VKSession.detectDepth(Object object)

> 官方文档：[VKSession.detectDepth(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.detectDepth.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKSession / VKSession.detectDepth
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.33.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.33.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

深度识别。当 wx.createVKSession 参数传入 {track: {depth: {mode: 2} } } 时可用。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/depth.html)。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| frameBuffer | ArrayBuffer |   | 是 | 需要识别深度的图像像素点数据，每四项表示一个像素点的 RGBA |
| width | number |   | 是 | 图像宽度 |
| height | number |   | 是 | 图像高度 |
