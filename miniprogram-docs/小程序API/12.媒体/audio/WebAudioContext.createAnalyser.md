# AnalyserNode WebAudioContext.createAnalyser()

> 官方文档：[AnalyserNode WebAudioContext.createAnalyser()](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createAnalyser.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / WebAudioContext / WebAudioContext.createAnalyser
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.22.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

创建一个 AnalyserNode 。可以用来获取音频时间和频率数据，以及实现数据可视化。

## 返回值

### AnalyserNode

## 示例代码

示例代码

```javascript
const audioCtx = wx.createWebAudioContext();
const analyser = audioCtx.createAnalyser();
analyser.fftSize = 2048;
const bufferLength = analyser.fftSize;
const dataArray = new Uint8Array(bufferLength);
analyser.getByteTimeDomainData(dataArray);
```
