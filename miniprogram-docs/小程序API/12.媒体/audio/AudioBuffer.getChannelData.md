# Float32Array AudioBuffer.getChannelData(number channel)

> 官方文档：[Float32Array AudioBuffer.getChannelData(number channel)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioBuffer.getChannelData.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / AudioBuffer / AudioBuffer.getChannelData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

返回一个 Float32Array，包含了带有频道的PCM数据，由频道参数定义（有0代表第一个频道）

## 参数

### number channel

要获取特定通道数据的索引

## 返回值

### Float32Array

## 示例代码

示例代码

```javascript
const audioCtx = wx.createWebAudioContext()
const myArrayBuffer = audioCtx.createBuffer(2, frameCount, audioCtx.sampleRate);
const nowBuffering = myArrayBuffer.getChannelData(channel);
```
