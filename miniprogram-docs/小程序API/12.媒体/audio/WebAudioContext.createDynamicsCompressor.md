# DynamicsCompressorNode WebAudioContext.createDynamicsCompressor()

> 官方文档：[DynamicsCompressorNode WebAudioContext.createDynamicsCompressor()](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createDynamicsCompressor.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / WebAudioContext / WebAudioContext.createDynamicsCompressor
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

## 功能描述

创建一个DynamicsCompressorNode

## 返回值

### DynamicsCompressorNode

## 示例代码

示例代码

```javascript
let audioCtx = wx.createWebAudioContext()
let compressor = audioCtx.createDynamicsCompressor()

compressor.threshold.value = -50
compressor.knee.value = 40
compressor.ratio.value = 12
compressor.attack.value = 0
compressor.release.value = 0.25
```
