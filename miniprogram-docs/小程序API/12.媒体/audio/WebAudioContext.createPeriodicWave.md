# PeriodicWaveNode WebAudioContext.createPeriodicWave(Float32Array real, Float32Array imag, object constraints)

> 官方文档：[PeriodicWaveNode WebAudioContext.createPeriodicWave(Float32Array real, Float32Array imag, object constraints)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createPeriodicWave.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / WebAudioContext / WebAudioContext.createPeriodicWave
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

## 功能描述

创建一个PeriodicWaveNode

## 参数

### Float32Array real

一系列余弦术语(传统上的A项)

### Float32Array imag

一系列正弦项(传统上的B项)

### object constraints

一个字典对象，用于指定是否禁用规范化(默认启用规范化)

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| disableNormalization | boolean |   | 否 | 如果指定为true则禁用标准化，默认为false |

## 返回值

### PeriodicWaveNode

## 注意

`real`和`imag`数组必须拥有一样的长度，否则抛出错误

```js
const real = new Float32Array(2)
const imag = new Float32Array(2)
real[0] = 0
imag[0] = 0
real[1] = 1
imag[1] = 0

const waveNode = audioContext.createPeriodicWave(real, imag, {disableNormalization: true})
```
