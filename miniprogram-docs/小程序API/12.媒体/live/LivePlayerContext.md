# LivePlayerContext

> 官方文档：[LivePlayerContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 实时音视频 / LivePlayerContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [live-player 组件](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html)

`LivePlayerContext` 实例，可通过 [wx.createLivePlayerContext](wx.createLivePlayerContext.md) 获取。

[LivePlayerContext](LivePlayerContext.md) 通过 `id` 跟一个 [live-player](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html) 组件绑定，操作对应的 [live-player](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html) 组件。

## 方法

### LivePlayerContext.play()

播放

### LivePlayerContext.stop()

停止

### LivePlayerContext.mute()

静音

### LivePlayerContext.pause()

暂停

### LivePlayerContext.resume()

恢复

### LivePlayerContext.requestFullScreen(Object object)

进入全屏

### LivePlayerContext.exitFullScreen()

退出全屏

### LivePlayerContext.exitPictureInPicture()

退出小窗，该方法可在任意页面调用

### LivePlayerContext.snapshot(Object object)

截图

### LivePlayerContext.requestBackgroundPlayback()

进入后台小窗播放模式。

### LivePlayerContext.exitBackgroundPlayback()

退出后台小窗播放模式。

### LivePlayerContext.startCasting()

开始投屏, 拉起半屏搜索设备。仅支持在 tap 事件回调内调用。

### LivePlayerContext.switchCasting()

切换投屏设备。仅支持在 tap 事件回调内调用。

### LivePlayerContext.reconnectCasting()

重连投屏设备。仅支持在 tap 事件回调内调用。

### LivePlayerContext.exitCasting()

退出投屏。仅支持在 tap 事件回调内调用。

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/UzWEzmm763Y4)
