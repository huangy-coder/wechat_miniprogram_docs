# MediaAudioPlayer wx.createMediaAudioPlayer()

> 官方文档：[MediaAudioPlayer wx.createMediaAudioPlayer()](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createMediaAudioPlayer.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / wx.createMediaAudioPlayer
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.13.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

## 功能描述

创建媒体音频播放器对象 [MediaAudioPlayer](MediaAudioPlayer.md) 对象，可用于播放视频解码器 [VideoDecoder](../video-decoder/VideoDecoder.md) 输出的音频。

## 返回值

### MediaAudioPlayer

## 注意事项

- iOS 7.0.15 mediaAudioPlayer 播放网络视频资源会出现音频卡顿，本地视频没有这个问题，将下一个客户端版本修复。

## 示例代码

```js
  // 创建视频解码器，具体参数见 createVideoDecoder 文档
  const videoDecoder = wx.createVideoDecoder()
  // 创建媒体音频播放器
  const mediaAudioPlayer = wx.createMediaAudioPlayer()
  // 启动视频解码器
  videoDecoder.start()
  // 启动播放器
  mediaAudioPlayer.start().then(() => {
    // 添加播放器音频来源
    mediaAudioPlayer.addAudioSource(videoDecoder).then(res => {
      videoDecoder.getFrameData() // 建议在 requestAnimationFrame 里获取每一帧视频数据
      console.log(res)
    })

    // 移除播放器音频来源
    mediaAudioPlayer.removeAudioSource(videoDecoder).then()
    // 停止播放器
    mediaAudioPlayer.stop().then()
    // 销毁播放器
    mediaAudioPlayer.destroy().then()
    // 设置播放器音量
    mediaAudioPlayer.volume = 0.5
  })
```

## 完整demo（小游戏）

- https://developers.weixin.qq.com/s/SF2duHmb7MjI
