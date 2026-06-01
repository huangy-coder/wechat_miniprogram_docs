# RecorderManager.start(Object object)

> 官方文档：[RecorderManager.start(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.start.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 录音 / RecorderManager / RecorderManager.start
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

开始录音

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| duration | number | 60000 | 否 | 录音的时长，单位 ms，最大值 600000（10 分钟） |   |
| sampleRate | number | 8000 | 否 | 采样率（pc不支持） |   |
| numberOfChannels | number | 2 | 否 | 录音通道数 |   |
| encodeBitRate | number | 48000 | 否 | 编码码率，有效值见下表格 |   |
| format | string | aac | 否 | 音频格式 |   |
| frameSize | number |   | 否 | 指定帧大小，单位 KB。传入 frameSize 后，每录制指定帧大小的内容后，会回调录制的文件内容，不指定则不会回调。暂仅支持 mp3、pcm 格式。 |   |
| audioSource | string | auto | 否 | 指定录音的音频输入源，可通过 [wx.getAvailableAudioSources()](../audio/wx.getAvailableAudioSources.md) 获取当前可用的音频源 | [2.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 8000 | 8000 采样率 |
| 11025 | 11025 采样率 |
| 12000 | 12000 采样率 |
| 16000 | 16000 采样率 |
| 22050 | 22050 采样率 |
| 24000 | 24000 采样率 |
| 32000 | 32000 采样率 |
| 44100 | 44100 采样率 |
| 48000 | 48000 采样率 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 1 | 1 个通道 |
| 2 | 2 个通道 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| mp3 | mp3 格式 |
| aac | aac 格式 |
| wav | wav 格式 |
| PCM | pcm 格式 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| auto | 自动设置，默认使用手机麦克风，插上耳麦后自动切换使用耳机麦克风，所有平台适用 |
| buildInMic | 手机麦克风，仅限 iOS |
| headsetMic | 有线耳机麦克风，仅限 iOS |
| mic | 麦克风（没插耳麦时是手机麦克风，插耳麦时是耳机麦克风），仅限 Android |
| camcorder | 同 mic，适用于录制音视频内容，仅限 Android |
| voice_communication | 同 mic，适用于实时沟通，仅限 Android |
| voice_recognition | 同 mic，适用于语音识别，仅限 Android |

## 采样率与编码码率限制

每种采样率有对应的编码码率范围有效值，设置不合法的采样率或编码码率会导致录音失败，具体对应关系如下表。

| 采样率 | 编码码率 |
| --- | --- |
| 8000 | 16000 ~ 48000 |
| 11025 | 16000 ~ 48000 |
| 12000 | 24000 ~ 64000 |
| 16000 | 24000 ~ 96000 |
| 22050 | 32000 ~ 128000 |
| 24000 | 32000 ~ 128000 |
| 32000 | 48000 ~ 192000 |
| 44100 | 64000 ~ 320000 |
| 48000 | 64000 ~ 320000 |
