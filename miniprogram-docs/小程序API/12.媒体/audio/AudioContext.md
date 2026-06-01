# AudioContext

> 官方文档：[AudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioContext.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / AudioContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[AudioContext](AudioContext.md) 实例，可通过 [wx.createAudioContext](wx.createAudioContext.md) 获取。

[AudioContext](AudioContext.md) 通过 `id` 跟一个 [audio](https://developers.weixin.qq.com/miniprogram/dev/component/audio.html) 组件绑定，操作对应的 [audio](https://developers.weixin.qq.com/miniprogram/dev/component/audio.html) 组件。

## 方法

### AudioContext.setSrc(string src)

设置音频地址

### AudioContext.play()

播放音频。

### AudioContext.pause()

暂停音频。

### AudioContext.seek(number position)

跳转到指定位置。

## 示例代码

```html
<!-- audio.wxml -->
<audio  src="{{src}}" id="myAudio" ></audio>

<button type="primary" bindtap="audioPlay">播放</button>
<button type="primary" bindtap="audioPause">暂停</button>
<button type="primary" bindtap="audio14">设置当前播放时间为14秒</button>
<button type="primary" bindtap="audioStart">回到开头</button>
```

```js
// audio.js
Page({
  onReady (e) {
    // 使用 wx.createAudioContext 获取 audio 上下文 context
    this.audioCtx = wx.createAudioContext('myAudio')
    this.audioCtx.setSrc('http://ws.stream.qqmusic.qq.com/M500001VfvsJ21xFqb.mp3?guid=ffffffff82def4af4b12b3cd9337d5e7&uin=346897220&vkey=6292F51E1E384E06DCBDC9AB7C49FD713D632D313AC4858BACB8DDD29067D3C601481D36E62053BF8DFEAF74C0A5CCFADD6471160CAF3E6A&fromtag=46')
    this.audioCtx.play()
  },
  data: {
    src: ''
  },
  audioPlay () {
    this.audioCtx.play()
  },
  audioPause () {
    this.audioCtx.pause()
  },
  audio14 () {
    this.audioCtx.seek(14)
  },
  audioStart () {
    this.audioCtx.seek(0)
  }
})
```
