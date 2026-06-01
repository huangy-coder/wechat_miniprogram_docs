# RecorderManager.onFrameRecorded(function listener)

> 官方文档：[RecorderManager.onFrameRecorded(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.onFrameRecorded.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 录音 / RecorderManager / RecorderManager.onFrameRecorded
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听已录制完指定帧大小的文件事件。如果设置了 frameSize，则会回调此事件。

## 参数

### function listener

已录制完指定帧大小的文件事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| frameBuffer | ArrayBuffer | 录音分片数据 |
| isLastFrame | boolean | 当前帧是否正常录音结束前的最后一帧 |
