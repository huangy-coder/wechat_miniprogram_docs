# BufferSourceNode

> 官方文档：[BufferSourceNode](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/BufferSourceNode.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / BufferSourceNode
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

音频源节点，通过 [WebAudioContext.createBufferSource](WebAudioContext.createBufferSource.md)方法获得。

## 属性

### AudioBuffer buffer

是一个 AudioBuffer， 它定义了要播放的音频，当设置它的值为 0 时，它会定义一个静默的单通道。（可读可写）

### Boolean loop

定义音频是否循环播放（可读可写）

### number loopStart

定义音频循环播放时，开始播放的位置。单位是秒，默认值是0（可读可写）

### number loopEnd

定义音频循环播放时，结束播放的位置。单位是秒，默认值是0（可读可写）

### AudioParam playbackRate

定义音频的播放倍速，数值越大速度越快，默认速度1.0，有效范围为 0 < playbackRate <= 2.0（可读可写）

### function onended

定义音频播放结束事件回调函数（可读可写）

## 方法

### BufferSourceNode.connect(AudioNode|AudioParam destination)

连接到一个指定目标。这个指定的目标可能是另一个 AudioNode（从而将音频数据引导到下一个指定节点）或一个AudioParam, 以便上一个节点的输出数据随着时间流逝能自动地对下一个参数值进行改变

### BufferSourceNode.disconnect()

与已连接的目标节点断开连接

### BufferSourceNode.start(number when, number offset, number duration)

音频源开始播放

### BufferSourceNode.stop(number when)

停止播放

## 示例代码

```js
const source = audioCtx.createBufferSource()
source.buffer = AudioBuffer
source.connect(audioCtx.destination)
source.start()
```
