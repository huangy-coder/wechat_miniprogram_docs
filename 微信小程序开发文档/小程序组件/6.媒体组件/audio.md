# audio

从基础库 [1.6.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [wx.createInnerAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createInnerAudioContext.html) 代替

> 基础库 1.0.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [wx.createAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createAudioContext.html)

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）、WebView

## 功能描述

音频。

## 属性说明

| 属性           | 类型        | 默认值   | 必填 | 说明                                                         | 最低版本                                                     |
| -------------- | ----------- | -------- | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| id             | string      |          | 否   | audio 组件的唯一标识符                                       | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| src            | string      |          | 否   | 要播放音频的资源地址                                         | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| loop           | boolean     | false    | 否   | 是否循环播放                                                 | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| controls       | boolean     | false    | 否   | 是否显示默认控件                                             | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| poster         | string      |          | 否   | 默认控件上的音频封面的图片资源地址，如果 controls 属性值为 false 则设置 poster 无效 | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| name           | string      | 未知音频 | 否   | 默认控件上的音频名字，如果 controls 属性值为 false 则设置 name 无效 | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| author         | string      | 未知作者 | 否   | 默认控件上的作者名字，如果 controls 属性值为 false 则设置 author 无效 | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| binderror      | eventhandle |          | 否   | 当发生错误时触发 error 事件，detail = {errMsg:MediaError.code} | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindplay       | eventhandle |          | 否   | 当开始/继续播放时触发play事件                                | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindpause      | eventhandle |          | 否   | 当暂停播放时触发 pause 事件                                  | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindtimeupdate | eventhandle |          | 否   | 当播放进度改变时触发 timeupdate 事件，detail = {currentTime, duration} | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindended      | eventhandle |          | 否   | 当播放到末尾时触发 ended 事件                                | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## MediaError.code

| 返回错误码 | 描述               |
| ---------- | ------------------ |
| 1          | 获取资源被用户禁止 |
| 2          | 网络错误           |
| 3          | 解码错误           |
| 4          | 不合适资源         |

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/NycgqcmS6KYY)

```xml
<!-- audio.wxml -->
<audio poster="{{poster}}" name="{{name}}" author="{{author}}" src="{{src}}" id="myAudio" controls loop></audio>

<button type="primary" bindtap="audioPlay">播放</button>
<button type="primary" bindtap="audioPause">暂停</button>
<button type="primary" bindtap="audio14">设置当前播放时间为14秒</button>
<button type="primary" bindtap="audioStart">回到开头</button>
```



```js
// audio.js
Page({
  onReady: function (e) {
    // 使用 wx.createAudioContext 获取 audio 上下文 context
    this.audioCtx = wx.createAudioContext('myAudio')
  },
  data: {
    poster: 'http://y.gtimg.cn/music/photo_new/T002R300x300M000003rsKF44GyaSk.jpg?max_age=2592000',
    name: '此时此刻',
    author: '许巍',
    src: 'http://ws.stream.qqmusic.qq.com/M500001VfvsJ21xFqb.mp3?guid=ffffffff82def4af4b12b3cd9337d5e7&uin=346897220&vkey=6292F51E1E384E06DCBDC9AB7C49FD713D632D313AC4858BACB8DDD29067D3C601481D36E62053BF8DFEAF74C0A5CCFADD6471160CAF3E6A&fromtag=46',
  },
  audioPlay: function () {
    this.audioCtx.play()
  },
  audioPause: function () {
    this.audioCtx.pause()
  },
  audio14: function () {
    this.audioCtx.seek(14)
  },
  audioStart: function () {
    this.audioCtx.seek(0)
  }
})
```