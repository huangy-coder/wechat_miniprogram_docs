# MediaContainer

> 官方文档：[MediaContainer](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/MediaContainer.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音视频合成 / MediaContainer
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.9.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

可通过 [wx.createMediaContainer](wx.createMediaContainer.md) 创建。

[MediaContainer](MediaContainer.md) 音视频处理容器，可以进行音频混音等操作

## 方法

### MediaContainer.extractDataSource(Object object)

将传入的视频源分离轨道。不会自动将轨道添加到待合成的容器里。

### MediaContainer.addTrack(MediaTrack track)

将音频或视频轨道添加到容器

### MediaContainer.removeTrack(MediaTrack track)

将音频或视频轨道从容器中移除

### MediaContainer.export()

将容器内的轨道合并并导出视频文件

### MediaContainer.destroy()

将容器销毁，释放资源
