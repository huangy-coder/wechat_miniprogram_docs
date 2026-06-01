# WebAudioContextNode

> 官方文档：[WebAudioContextNode](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContextNode.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / WebAudioContextNode
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

一类音频处理模块，不同的Node具备不同的功能，如GainNode(音量调整)等。一个WebAudioContextNode可以通过上下文来创建。
目前已经支持以下Node：
IIRFilterNode
WaveShaperNode
ConstantSourceNode
ChannelMergerNode
OscillatorNode
GainNode
BiquadFilterNode
PeriodicWaveNode
BufferSourceNode
ChannelSplitterNode
ChannelMergerNode
DelayNode
DynamicsCompressorNode
ScriptProcessorNode
PannerNode
AnalyserNode
