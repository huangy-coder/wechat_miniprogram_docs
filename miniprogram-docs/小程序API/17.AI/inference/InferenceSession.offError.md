# InferenceSession.offError(function callback)

> 官方文档：[InferenceSession.offError(function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/InferenceSession.offError.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / AI 推理 / InferenceSession / InferenceSession.offError
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.30.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.30.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

取消监听模型加载失败事件

## 参数

### function callback

模型加载失败回调函数。传入指定回调函数则只取消指定回调，不传则取消所有回调
