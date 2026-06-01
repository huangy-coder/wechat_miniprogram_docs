# Array.<Object> VKSession.hitTest(number x, number y, Object reset)

> 官方文档：[Array.<Object> VKSession.hitTest(number x, number y, Object reset)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.hitTest.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKSession / VKSession.hitTest
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.20.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

触摸检测，v1 版本只支持单平面（即 hitTest 生成一次平面后，后续 hitTest 均不会再生成平面，而是以之前生成的平面为基础进行检测）。如果需要重新识别其他平面，可以在调用此方法时将 reset 参数置为 true。

## 参数

### number x

相对视窗的横坐标，取值范围为 [0, 1]，0 为左边缘，1 为右边缘

### number y

相对视窗的纵坐标，取值范围为 [0, 1]，0 为上边缘，1 为下边缘

### Object reset

是否需要重新识别其他平面，v2 版本不再需要此参数

## 返回值

### Array.<Object>

检测结果

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| transform | Float32Array | 包含位置、旋转、放缩信息的矩阵，以列为主序 |
