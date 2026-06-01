# VideoContext.requestFullScreen(Object object)

> 官方文档：[VideoContext.requestFullScreen(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.requestFullScreen.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 视频 / VideoContext / VideoContext.requestFullScreen
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.4.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [video 组件](https://developers.weixin.qq.com/miniprogram/dev/component/video.html)

## 功能描述

进入全屏。若有自定义内容需在全屏时展示，需将内容节点放置到 video 节点内。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| direction | number |   | 否 | 设置全屏时视频的方向，不指定则根据宽高比自动判断。 | [1.7.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 0 | 正常竖向 |
| 90 | 屏幕逆时针90度 |
| -90 | 屏幕顺时针90度 |
