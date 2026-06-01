# AudioBuffer WebAudioContext.decodeAudioData(ArrayBuffer audioData, function successCallback, function errorCallback)

> 官方文档：[AudioBuffer WebAudioContext.decodeAudioData(ArrayBuffer audioData, function successCallback, function errorCallback)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.decodeAudioData.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / WebAudioContext / WebAudioContext.decodeAudioData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

## 功能描述

异步解码一段资源为AudioBuffer。

## 参数

### ArrayBuffer audioData

一个包含音频文件数据的 ArrayBuffer

### function successCallback

在音频数据解码成功时被调用，参数为解码后的AudioBuffer

### function errorCallback

在音频数据解码失败时被调用

## 返回值

### AudioBuffer

## 示例代码

示例

```javascript
wx.request({
  url: url, // 音频 url
  responseType: 'arraybuffer',
  success: res => {
    audioCtx.decodeAudioData(res.data, buffer => {
      console.log(buffer)
    }, err => {
      console.error('decodeAudioData fail', err)
    })
  }
})
```
