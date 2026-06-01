# MediaContainer.extractDataSource(Object object)

> 官方文档：[MediaContainer.extractDataSource(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/MediaContainer.extractDataSource.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音视频合成 / MediaContainer / MediaContainer.extractDataSource
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.9.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

## 功能描述

将传入的视频源分离轨道。不会自动将轨道添加到待合成的容器里。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| source | string |   | 是 | 视频源地址，只支持本地文件 |
