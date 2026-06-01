# DelayNode WebAudioContext.createDelay(number maxDelayTime)

> 官方文档：[DelayNode WebAudioContext.createDelay(number maxDelayTime)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createDelay.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / WebAudioContext / WebAudioContext.createDelay
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

## 功能描述

创建一个DelayNode

## 参数

### number maxDelayTime

最大延迟时间

## 返回值

### DelayNode

## 示例代码

示例代码

```javascript
let audioCtx = wx.createWebAudioContext()
const delayNode = audioCtx.createDelay(5)
```
