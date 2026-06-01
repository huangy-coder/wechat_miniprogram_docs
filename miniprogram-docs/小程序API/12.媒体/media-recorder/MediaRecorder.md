# MediaRecorder

> 官方文档：[MediaRecorder](https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/MediaRecorder.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 画面录制器 / MediaRecorder
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

可通过 [wx.createMediaRecorder](wx.createMediaRecorder.md) 创建。

[MediaRecorder](MediaRecorder.md) WebGL 画面录制器，可以进行录制相关操作，在结束录制时导出视频文件

## 方法

### Promise MediaRecorder.pause()

暂停录制

### Promise MediaRecorder.resume()

恢复录制

### Promise MediaRecorder.start()

开始录制

### Promise MediaRecorder.stop()

结束录制

### Promise MediaRecorder.requestFrame(function callback)

请求下一帧录制，在 callback 里完成一帧渲染后开始录制当前帧

### MediaRecorder.on(string eventName, function callback)

注册监听录制事件的回调函数。当对应事件触发时，回调函数会被执行。

### MediaRecorder.off(string eventName, function callback)

取消监听录制事件。当对应事件触发时，该回调函数不再执行。

### Promise MediaRecorder.destroy()

销毁录制器
