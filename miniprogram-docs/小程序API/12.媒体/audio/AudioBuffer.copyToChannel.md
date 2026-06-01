# AudioBuffer.copyToChannel(Float32Array source, number channelNumber, number startInChannel)

> 官方文档：[AudioBuffer.copyToChannel(Float32Array source, number channelNumber, number startInChannel)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioBuffer.copyToChannel.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / AudioBuffer / AudioBuffer.copyToChannel
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

从指定数组复制样本到audioBuffer的特定通道

## 参数

### Float32Array source

需要复制的源数组

### number channelNumber

需要复制到的目的通道号

### number startInChannel

复制偏移数据量

## 示例代码

示例代码参考AudioBuffer.copyFromChannel
