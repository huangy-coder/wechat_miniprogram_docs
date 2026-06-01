# MediaAudioPlayer

> 官方文档：[MediaAudioPlayer](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/MediaAudioPlayer.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / MediaAudioPlayer
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

MediaAudioPlayer 实例，可通过 [wx.createMediaAudioPlayer](wx.createMediaAudioPlayer.md) 接口获取实例。

## 属性

### number volume

音量。范围 0~1。默认为 1

## 方法

### Promise MediaAudioPlayer.start()

启动播放器

### Promise MediaAudioPlayer.addAudioSource(VideoDecoder source)

添加音频源

### Promise MediaAudioPlayer.removeAudioSource(VideoDecoder source)

移除音频源

### Promise MediaAudioPlayer.stop()

停止播放器

### Promise MediaAudioPlayer.destroy()

销毁播放器
