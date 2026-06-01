# AudioBuffer WebAudioContext.createBuffer(number numOfChannels, number length, number sampleRate)

> 官方文档：[AudioBuffer WebAudioContext.createBuffer(number numOfChannels, number length, number sampleRate)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createBuffer.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / WebAudioContext / WebAudioContext.createBuffer
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

## 功能描述

创建一个AudioBuffer，代表着一段驻留在内存中的短音频

## 参数

### number numOfChannels

定义了 buffer 中包含的声频通道数量的整数

### number length

代表 buffer 中的样本帧数的整数

### number sampleRate

线性音频样本的采样率，即每一秒包含的关键帧的个数

## 返回值

### AudioBuffer

buffer 返回一个AudioBuffer实例

## 示例代码

示例代码

```javascript
const audioCtx = wx.createWebAudioContext()
const channels = 2, frameCount = audioCtx.sampleRate * 2.0
const myArrayBuffer = audioCtx.createBuffer(channels, frameCount, audioCtx.sampleRate)
```
