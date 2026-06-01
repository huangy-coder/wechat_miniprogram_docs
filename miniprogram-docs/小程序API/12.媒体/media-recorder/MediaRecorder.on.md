# MediaRecorder.on(string eventName, function callback)

> 官方文档：[MediaRecorder.on(string eventName, function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/MediaRecorder.on.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 画面录制器 / MediaRecorder / MediaRecorder.on
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

## 功能描述

注册监听录制事件的回调函数。当对应事件触发时，回调函数会被执行。

## 参数

### string eventName

事件名

**eventName 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| start | 录制开始事件。 |   |
| stop | 录制结束事件。返回 {tempFilePath, duration, fileSize} |   |
| pause | 录制暂停事件。 |   |
| resume | 录制继续事件。 |   |
| timeupdate | 录制时间更新事件。 |   |

### function callback

事件触发时执行的回调函数
