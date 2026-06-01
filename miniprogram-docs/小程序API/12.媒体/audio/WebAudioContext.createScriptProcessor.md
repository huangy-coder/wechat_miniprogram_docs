# ScriptProcessorNode WebAudioContext.createScriptProcessor(number bufferSize, number numberOfInputChannels, number numberOfOutputChannels)

> 官方文档：[ScriptProcessorNode WebAudioContext.createScriptProcessor(number bufferSize, number numberOfInputChannels, number numberOfOutputChannels)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createScriptProcessor.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / WebAudioContext / WebAudioContext.createScriptProcessor
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

## 功能描述

创建一个ScriptProcessorNode

## 参数

### number bufferSize

缓冲区大小，以样本帧为单位

### number numberOfInputChannels

用于指定输入node的声道的数量

### number numberOfOutputChannels

用于指定输出node的声道的数量

## 返回值

### ScriptProcessorNode

## 示例代码

示例代码

```javascript
let audioCtx = wx.createWebAudioContext()
const sampleSize = 4096
audioCtx.createScriptProcessor(sampleSize, 1, 1)
```
