# RecorderManager.onError(function listener)

> 官方文档：[RecorderManager.onError(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.onError.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 录音 / RecorderManager / RecorderManager.onError
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听录音错误事件

## 参数

### function listener

录音错误事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |
