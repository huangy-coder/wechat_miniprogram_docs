# IIRFilterNode WebAudioContext.createIIRFilter(Array.<number> feedforward, Array.<number> feedback)

> 官方文档：[IIRFilterNode WebAudioContext.createIIRFilter(Array.<number> feedforward, Array.<number> feedback)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createIIRFilter.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / WebAudioContext / WebAudioContext.createIIRFilter
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

## 功能描述

创建一个IIRFilterNode

## 参数

### Array.<number> feedforward

一个浮点值数组，指定IIR滤波器传递函数的前馈(分子)系数。

### Array.<number> feedback

一个浮点值数组，指定IIR滤波器传递函数的反馈(分母)系数。

## 返回值

### IIRFilterNode

## 示例代码

```javascript
let lowPassCoefs = [
  {
    frequency: 200,
    feedforward: [0.00020298, 0.0004059599, 0.00020298],
    feedback: [1.0126964558, -1.9991880801, 0.9873035442]
  },
  {
    frequency: 500,
    feedforward: [0.0012681742, 0.0025363483, 0.0012681742],
    feedback: [1.0317185917, -1.9949273033, 0.9682814083]
  },
  {
    frequency: 1000,
    feedforward: [0.0050662636, 0.0101325272, 0.0050662636],
    feedback: [1.0632762845, -1.9797349456, 0.9367237155]
  },
  {
    frequency: 5000,
    feedforward: [0.1215955842, 0.2431911684, 0.1215955842],
    feedback: [1.2912769759, -1.5136176632, 0.7087230241]
  }
]

const feedForward = lowPassCoefs[filterNumber].feedforward
const feedBack = lowPassCoefs[filterNumber].feedback
const iirFilter = audioContext.createIIRFilter(feedForward, feedBack)
```
