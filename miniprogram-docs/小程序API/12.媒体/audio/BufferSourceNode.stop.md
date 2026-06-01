# BufferSourceNode.stop(number when)

> 官方文档：[BufferSourceNode.stop(number when)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/BufferSourceNode.stop.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / BufferSourceNode / BufferSourceNode.stop
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

停止播放

## 参数

### number when

延迟停止播放的时间，单位是秒。与 AudioContext 使用相同的时间坐标系统。省略此参数、指定值 0 或传递负值会使声音立即停止播放。
