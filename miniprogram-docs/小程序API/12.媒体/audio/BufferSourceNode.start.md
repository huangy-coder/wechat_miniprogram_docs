# BufferSourceNode.start(number when, number offset, number duration)

> 官方文档：[BufferSourceNode.start(number when, number offset, number duration)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/BufferSourceNode.start.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / BufferSourceNode / BufferSourceNode.start
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

音频源开始播放

## 参数

### number when

延迟播放的时间，单位是秒。与 AudioContext 使用相同的时间坐标系统。如果 when 小于 AudioContext.currentTime, 或者是 0，声音立即被播放。 默认值是 0

### number offset

音频开始播放的位置，单位是秒。默认值是 0

### number duration

音频播放的持续时间，单位是秒。如果这个参数没有被指定，声音播放到自然结束或者使用stop() 方法结束。使用这个参数的功能与调用 start(when, offset) 和调用 stop(when+duration)效果完全相同
