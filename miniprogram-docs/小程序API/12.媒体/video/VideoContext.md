# VideoContext

> 官方文档：[VideoContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 视频 / VideoContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [video 组件](https://developers.weixin.qq.com/miniprogram/dev/component/video.html)

VideoContext 实例，可通过 [wx.createVideoContext](wx.createVideoContext.md) 获取。

[VideoContext](VideoContext.md) 通过 `id` 跟一个 [video](https://developers.weixin.qq.com/miniprogram/dev/component/video.html) 组件绑定，操作对应的 [video](https://developers.weixin.qq.com/miniprogram/dev/component/video.html) 组件。

## 方法

### VideoContext.play()

播放视频

### VideoContext.pause()

暂停视频

### VideoContext.stop()

停止视频

### VideoContext.seek(number position)

跳转到指定位置

### VideoContext.sendDanmu(Object data)

发送弹幕

### VideoContext.playbackRate(number rate)

设置倍速播放

### VideoContext.requestFullScreen(Object object)

进入全屏。若有自定义内容需在全屏时展示，需将内容节点放置到 video 节点内。

### VideoContext.exitFullScreen()

退出全屏

### VideoContext.showStatusBar()

显示状态栏，仅在iOS全屏下有效

### VideoContext.hideStatusBar()

隐藏状态栏，仅在iOS全屏下有效

### VideoContext.exitPictureInPicture()

退出小窗，该方法可在任意页面调用

### VideoContext.requestBackgroundPlayback()

进入后台小窗播放模式。

### VideoContext.exitBackgroundPlayback()

退出后台小窗播放模式。

### VideoContext.startCasting()

开始投屏, 拉起半屏搜索设备。仅支持在 tap 事件回调内调用。

### VideoContext.switchCasting()

切换投屏设备。仅支持在 tap 事件回调内调用。

### VideoContext.reconnectCasting()

重连投屏设备。仅支持在 tap 事件回调内调用。

### VideoContext.exitCasting()

退出投屏。仅支持在 tap 事件回调内调用。

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/X5V6Xmmk6xYB)

```html
<view class="section tc">
  <video id="myVideo" src="http://wxsnsdy.tc.qq.com/105/20210/snsdyvideodownload?filekey=30280201010421301f0201690402534804102ca905ce620b1241b726bc41dcff44e00204012882540400&bizid=1023&hy=SH&fileparam=302c020101042530230204136ffd93020457e3c4ff02024ef202031e8d7f02030f42400204045a320a0201000400" enable-danmu danmu-btn controls></video>
  <view class="btn-area">
    <input bindblur="bindInputBlur"/>
    <button bindtap="bindSendDanmu">发送弹幕</button>
  </view>
</view>
```

```js
function getRandomColor () {
  let rgb = []
  for (let i = 0 ; i < 3; ++i) {
    let color = Math.floor(Math.random() * 256).toString(16)
    color = color.length == 1 ? '0' + color : color
    rgb.push(color)
  }
  return '#' + rgb.join('')
}

Page({
  onReady (res) {
    this.videoContext = wx.createVideoContext('myVideo')
  },
  inputValue: '',
  bindInputBlur (e) {
    this.inputValue = e.detail.value
  },
  bindSendDanmu () {
    this.videoContext.sendDanmu({
      text: this.inputValue,
      color: getRandomColor()
    })
  }
})
```
