# MediaTrack

> 官方文档：[MediaTrack](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/MediaTrack.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音视频合成 / MediaTrack
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.9.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

可通过 [MediaContainer.extractDataSource](MediaContainer.extractDataSource.md) 返回。

[MediaTrack](MediaTrack.md) 音频或视频轨道，可以对轨道进行一些操作

## 属性

### string kind

轨道类型，只读

**kind 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| audio | 音频轨道 |   |
| video | 视频轨道 |   |

### number duration

轨道长度，只读

### number volume

音量，音频轨道下有效，可写
