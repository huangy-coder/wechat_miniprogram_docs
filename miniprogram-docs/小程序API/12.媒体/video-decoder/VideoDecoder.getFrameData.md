# Object VideoDecoder.getFrameData()

> 官方文档：[Object VideoDecoder.getFrameData()](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/VideoDecoder.getFrameData.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 视频解码器 / VideoDecoder / VideoDecoder.getFrameData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

## 功能描述

获取下一帧的解码数据

## 返回值

### Object

视频帧数据，若取不到则返回 null。当缓冲区为空的时候可能暂停取不到数据。

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 帧数据宽度 |
| height | number | 帧数据高度 |
| data | ArrayBuffer | 帧数据 |
| pkPts | number | 帧原始 pts |
| pkDts | number | 帧原始 dts |
