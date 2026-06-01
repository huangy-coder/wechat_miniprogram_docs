# WebAudioContext

> 官方文档：[WebAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / WebAudioContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.19.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

WebAudioContext 实例，通过[wx.createWebAudioContext](wx.createWebAudioContext.md) 接口获取该实例。

## 属性

### string state

当前WebAudio上下文的状态。可能的值如下：suspended（暂停）、running（正在运行）、closed（已关闭）。需要注意的是，不要在 audioContext close后再访问state属性

### function onstatechange

可写属性，开发者可以对该属性设置一个监听函数，当WebAudio状态改变的时候，会触发开发者设置的监听函数。

### number currentTime

获取当前上下文的时间戳。

### WebAudioContextNode destination

当前上下文的最终目标节点，一般是音频渲染设备。

### AudioListener listener

空间音频监听器。

### number sampleRate

采样率，通常在8000-96000之间，通常44100hz的采样率最为常见。

## 方法

### Promise WebAudioContext.close()

关闭WebAudioContext

### Promise WebAudioContext.resume()

同步恢复已经被暂停的WebAudioContext上下文

### Promise WebAudioContext.suspend()

同步暂停WebAudioContext上下文

### IIRFilterNode WebAudioContext.createIIRFilter(Array.<number> feedforward, Array.<number> feedback)

创建一个IIRFilterNode

### WaveShaperNode WebAudioContext.createWaveShaper()

创建一个WaveShaperNode

### ConstantSourceNode WebAudioContext.createConstantSource()

创建一个ConstantSourceNode

### OscillatorNode WebAudioContext.createOscillator()

创建一个OscillatorNode

### GainNode WebAudioContext.createGain()

创建一个GainNode

### PeriodicWaveNode WebAudioContext.createPeriodicWave(Float32Array real, Float32Array imag, object constraints)

创建一个PeriodicWaveNode

### BiquadFilterNode WebAudioContext.createBiquadFilter()

创建一个BiquadFilterNode

### BufferSourceNode WebAudioContext.createBufferSource()

创建一个BufferSourceNode实例，通过AudioBuffer对象来播放音频数据。

### ChannelMergerNode WebAudioContext.createChannelMerger(number numberOfInputs)

创建一个ChannelMergerNode

### ChannelSplitterNode WebAudioContext.createChannelSplitter(number numberOfOutputs)

创建一个ChannelSplitterNode

### DelayNode WebAudioContext.createDelay(number maxDelayTime)

创建一个DelayNode

### DynamicsCompressorNode WebAudioContext.createDynamicsCompressor()

创建一个DynamicsCompressorNode

### ScriptProcessorNode WebAudioContext.createScriptProcessor(number bufferSize, number numberOfInputChannels, number numberOfOutputChannels)

创建一个ScriptProcessorNode

### AnalyserNode WebAudioContext.createAnalyser()

创建一个 AnalyserNode 。可以用来获取音频时间和频率数据，以及实现数据可视化。

### PannerNode WebAudioContext.createPanner()

创建一个PannerNode

### AudioBuffer WebAudioContext.createBuffer(number numOfChannels, number length, number sampleRate)

创建一个AudioBuffer，代表着一段驻留在内存中的短音频

### AudioBuffer WebAudioContext.decodeAudioData(ArrayBuffer audioData, function successCallback, function errorCallback)

异步解码一段资源为AudioBuffer。

## 示例代码

```js
// 监听状态
const audioCtx = wx.createWebAudioContext()
audioCtx.onstatechange = () => {
  console.log(ctx.state)
}
setTimeout(audioCtx.suspend, 1000)
setTimeout(audioCtx.resume, 2000)
```
