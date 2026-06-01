# InnerAudioContext

> 官方文档：[InnerAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / InnerAudioContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

InnerAudioContext 实例，可通过 [wx.createInnerAudioContext](wx.createInnerAudioContext.md) 接口获取实例。注意，音频播放过程中，可能被系统中断，可通过 [wx.onAudioInterruptionBegin](../../1.基础/app/app-event/wx.onAudioInterruptionBegin.md)、[wx.onAudioInterruptionEnd](../../1.基础/app/app-event/wx.onAudioInterruptionEnd.md)事件来处理这种情况。

## 属性

### string src

音频资源的地址，用于直接播放。[2.2.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始支持云文件ID

### number startTime

开始播放的位置（单位：s），默认为 0

### boolean autoplay

是否自动开始播放，默认为 `false`

### boolean loop

是否循环播放，默认为 `false`

### boolean obeyMuteSwitch

是否遵循系统静音开关，默认为 `true`。当此参数为 `false` 时，即使用户打开了静音开关，也能继续发出声音。从 2.3.0 版本开始此参数不生效，使用 [wx.setInnerAudioOption](wx.setInnerAudioOption.md) 接口统一设置。

### number volume

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

音量。范围 0~1。默认为 1

### number playbackRate

> 基础库 2.11.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

播放速度。范围 0.5-2.0，默认为 1。（Android 需要 6 及以上版本）

### number duration

当前音频的长度（单位 s）。只有在当前有合法的 src 时返回（只读）

### number currentTime

当前音频的播放位置（单位 s）。只有在当前有合法的 src 时返回，时间保留小数点后 6 位（currentTime 属性在基础库 2.26.2 之前只读，基础库 2.26.2 开始可读可写，改变 currentTime 值等同于调用 seek）

### boolean paused

当前是是否暂停或停止状态（只读）

### number buffered

音频缓冲的时间点，仅保证当前播放时间点到此时间点内容已缓冲（只读）

### string referrerPolicy

> 基础库 2.13.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

`origin`: 发送完整的referrer; `no-referrer`: 不发送。格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 {appid} 为小程序的 appid，{version} 为小程序的版本号，版本号为 0 表示为开发版、体验版以及审核版本，版本号为 devtools 表示为开发者工具，其余为正式版本；

## 方法

### InnerAudioContext.play()

播放

### InnerAudioContext.pause()

暂停。暂停后的音频再播放会从暂停处开始播放

### InnerAudioContext.stop()

停止。停止后的音频再播放会从头开始播放。

### InnerAudioContext.seek(number position)

跳转到指定位置

### InnerAudioContext.destroy()

销毁当前实例

### InnerAudioContext.onCanplay(function listener)

监听音频进入可以播放状态的事件。但不保证后面可以流畅播放

### InnerAudioContext.offCanplay(function listener)

移除音频进入可以播放状态的事件的监听函数

### InnerAudioContext.onPlay(function listener)

监听音频播放事件

### InnerAudioContext.offPlay(function listener)

移除音频播放事件的监听函数

### InnerAudioContext.onPause(function listener)

监听音频暂停事件

### InnerAudioContext.offPause(function listener)

移除音频暂停事件的监听函数

### InnerAudioContext.onStop(function listener)

监听音频停止事件

### InnerAudioContext.offStop(function listener)

移除音频停止事件的监听函数

### InnerAudioContext.onEnded(function listener)

监听音频自然播放至结束的事件

### InnerAudioContext.offEnded(function listener)

移除音频自然播放至结束的事件的监听函数

### InnerAudioContext.onTimeUpdate(function listener)

监听音频播放进度更新事件

### InnerAudioContext.offTimeUpdate(function listener)

移除音频播放进度更新事件的监听函数

### InnerAudioContext.onError(function listener)

监听音频播放错误事件

### InnerAudioContext.offError(function listener)

移除音频播放错误事件的监听函数

### InnerAudioContext.onWaiting(function listener)

监听音频加载中事件。当音频因为数据不足，需要停下来加载时会触发

### InnerAudioContext.offWaiting(function listener)

移除音频加载中事件的监听函数

### InnerAudioContext.onSeeking(function listener)

监听音频进行跳转操作的事件

### InnerAudioContext.offSeeking(function listener)

移除音频进行跳转操作的事件的监听函数

### InnerAudioContext.onSeeked(function listener)

监听音频完成跳转操作的事件

### InnerAudioContext.offSeeked(function listener)

移除音频完成跳转操作的事件的监听函数

## 支持格式

| 格式 | iOS | Android |
| --- | --- | --- |
| flac | x | √ |
| m4a | √ | √ |
| ogg | x | √ |
| ape | x | √ |
| amr | x | √ |
| wma | x | √ |
| wav | √ | √ |
| mp3 | √ | √ |
| mp4 | x | √ |
| aac | √ | √ |
| aiff | √ | x |
| caf | √ | x |

## 示例代码

```js
const innerAudioContext = wx.createInnerAudioContext()
innerAudioContext.autoplay = true
innerAudioContext.src = 'https://wx_test.mp3'
innerAudioContext.onPlay(() => {
  console.log('开始播放')
})
innerAudioContext.onError((res) => {
  console.log(res.errMsg)
  console.log(res.errCode)
})
```
