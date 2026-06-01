# AudioBuffer

> 官方文档：[AudioBuffer](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioBuffer.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / AudioBuffer
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.19.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

AudioBuffer接口表示存在内存里的一段短小的音频资源，利用[WebAudioContext.decodeAudioData](WebAudioContext.decodeAudioData.md)方法从一个音频文件构建，或者利用 [WebAudioContext.createBuffer](WebAudioContext.createBuffer.md)从原始数据构建。把音频放入AudioBuffer后，可以传入到一个 AudioBufferSourceNode进行播放。

## 属性

### number sampleRate

存储在缓存区的PCM数据的采样率（单位为sample/s)

### number length

返回存储在缓存区的PCM数据的采样帧率

### number duration

返回存储在缓存区的PCM数据的时长（单位为秒）

### number numberOfChannels

储存在缓存区的PCM数据的通道数

## 方法

### Float32Array AudioBuffer.getChannelData(number channel)

返回一个 Float32Array，包含了带有频道的PCM数据，由频道参数定义（有0代表第一个频道）

### AudioBuffer.copyFromChannel()

从AudioBuffer的指定频道复制到数组终端。

### AudioBuffer.copyToChannel(Float32Array source, number channelNumber, number startInChannel)

从指定数组复制样本到audioBuffer的特定通道
