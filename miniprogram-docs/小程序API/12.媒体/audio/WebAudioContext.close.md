# Promise WebAudioContext.close()

> 官方文档：[Promise WebAudioContext.close()](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.close.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / WebAudioContext / WebAudioContext.close
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

## 功能描述

关闭WebAudioContext

## 返回值

### Promise

## 注意事项

同步关闭对应的WebAudio上下文。close后会立即释放当前上下文的资源，**不要在close后再次访问state属性。**

```js
const audioCtx = wx.createWebAudioContext()
audioCtx.close().then(() => {
  console.log(audioCtx.state) // bad case：不应该在close后再访问state
})
```
