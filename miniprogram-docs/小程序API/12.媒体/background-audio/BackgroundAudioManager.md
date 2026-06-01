# BackgroundAudioManager

> 官方文档：[BackgroundAudioManager](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 背景音频 / BackgroundAudioManager
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

BackgroundAudioManager 实例，可通过 [wx.getBackgroundAudioManager](wx.getBackgroundAudioManager.md) 获取。

## 属性

### string src

音频的数据源（[2.2.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始支持云文件ID）。默认为空字符串，**当设置了新的 src 时，会自动开始播放**，目前支持的格式有 m4a, aac, mp3, wav。

### number startTime

音频开始播放的位置（单位：s）。

### string title

音频标题，用于原生音频播放器音频标题（必填）。原生音频播放器中的分享功能，分享出去的卡片标题，也将使用该值。

### string epname

专辑名，原生音频播放器中的分享功能，分享出去的卡片简介，也将使用该值。

### string singer

歌手名，原生音频播放器中的分享功能，分享出去的卡片简介，也将使用该值。

### string coverImgUrl

封面图 URL，用于做原生音频播放器背景图。原生音频播放器中的分享功能，分享出去的卡片配图及背景也将使用该图。

### string webUrl

页面链接，原生音频播放器中的分享功能，分享出去的卡片简介，也将使用该值。

### string protocol

> 基础库 1.9.94 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

音频协议。默认值为 'http'，设置 'hls' 可以支持播放 HLS 协议的直播音频。

### number playbackRate

> 基础库 2.11.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

播放速度。范围 0.5-2.0，默认为 1。（Android 需要 6 及以上版本）

### number duration

当前音频的长度（单位：s），只有在有合法 src 时返回。（只读）

### number currentTime

当前音频的播放位置（单位：s），只有在有合法 src 时返回。（只读）

### boolean paused

当前是否暂停或停止。（只读）

### number buffered

音频已缓冲的时间，仅保证当前播放时间点到此时间点内容已缓冲。（只读）

### string referrerPolicy

> 基础库 2.13.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

`origin`: 发送完整的referrer; `no-referrer`: 不发送。格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 {appid} 为小程序的 appid，{version} 为小程序的版本号，版本号为 0 表示为开发版、体验版以及审核版本，版本号为 devtools 表示为开发者工具，其余为正式版本；

### string referrerPath

> 基础库 3.4.8 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

关联页面路径。设置后，当点击播放器上的小程序跳转链接时，将跳转到这个关联页面路径（实验特性，目前仅Android端支持）

### string audioType

> 基础库 3.4.8 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

音频类型。可设置 "audio" 和 "music" 两种值，默认为 "audio"。不同音频类型对应的播放器样式不一样（实验特性，目前仅iOS和Android端支持）

## 方法

### BackgroundAudioManager.play()

播放音乐

### BackgroundAudioManager.pause()

暂停音乐

### BackgroundAudioManager.seek(number currentTime)

跳转到指定位置

### BackgroundAudioManager.stop()

停止音乐

### BackgroundAudioManager.onCanplay(function listener)

监听背景音频进入可播放状态事件。 但不保证后面可以流畅播放

### BackgroundAudioManager.onWaiting(function listener)

监听音频加载中事件。当音频因为数据不足，需要停下来加载时会触发

### BackgroundAudioManager.onError(function listener)

监听背景音频播放错误事件

### BackgroundAudioManager.onPlay(function listener)

监听背景音频播放事件

### BackgroundAudioManager.onPause(function listener)

监听背景音频暂停事件

### BackgroundAudioManager.onSeeking(function listener)

监听背景音频开始跳转操作事件

### BackgroundAudioManager.onSeeked(function listener)

监听背景音频完成跳转操作事件

### BackgroundAudioManager.onEnded(function listener)

监听背景音频自然播放结束事件

### BackgroundAudioManager.onStop(function listener)

监听背景音频停止事件

### BackgroundAudioManager.onTimeUpdate(function listener)

监听背景音频播放进度更新事件，只有小程序在前台时会回调。

### BackgroundAudioManager.onNext(function listener)

监听用户在系统音乐播放面板点击下一曲事件

### BackgroundAudioManager.onPrev(function listener)

监听用户在系统音乐播放面板点击上一曲事件

## 示例代码

```js
const backgroundAudioManager = wx.getBackgroundAudioManager()

backgroundAudioManager.title = '此时此刻'
backgroundAudioManager.epname = '此时此刻'
backgroundAudioManager.singer = '许巍'
backgroundAudioManager.coverImgUrl = 'http://y.gtimg.cn/music/photo_new/T002R300x300M000003rsKF44GyaSk.jpg?max_age=2592000'
// 设置了 src 之后会自动播放
backgroundAudioManager.src = 'https://wx_test.mp3'
```
