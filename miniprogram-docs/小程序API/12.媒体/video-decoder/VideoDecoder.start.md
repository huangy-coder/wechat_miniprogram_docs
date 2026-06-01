# Promise VideoDecoder.start(Object object)

> 官方文档：[Promise VideoDecoder.start(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/VideoDecoder.start.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 视频解码器 / VideoDecoder / VideoDecoder.start
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

## 功能描述

开始解码

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| source | string |   | 是 | 需要解码的视频源文件。基础库 2.13.0 以下的版本只支持本地路径。 2.13.0 开始支持 http:// 和 https:// 协议的远程路径。 |   |
| mode | number | 1 | 否 | 解码模式。0：按 pts 解码；1：以最快速度解码 |   |
| abortAudio | boolean | false | 否 | 是否不需要音频轨道 | [2.15.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| abortVideo | boolean | false | 否 | 是否不需要视频轨道 | [2.15.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 返回值

### Promise

> 基础库 2.16.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。
