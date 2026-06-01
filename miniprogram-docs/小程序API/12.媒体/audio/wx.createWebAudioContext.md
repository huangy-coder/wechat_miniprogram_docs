# WebAudioContext wx.createWebAudioContext()

> 官方文档：[WebAudioContext wx.createWebAudioContext()](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createWebAudioContext.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / wx.createWebAudioContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.19.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

创建 WebAudio 上下文。

## 返回值

### WebAudioContext

## 示例代码

一个简单的播放demo

```javascript
const audioCtx = wx.createWebAudioContext()

const loadAudio = (url) => {
  return new Promise((resolve) => {
    wx.request({
      url,
      responseType: 'arraybuffer',
      success: res => {
        console.log('res.data', res.data)
        audioCtx.decodeAudioData(res.data, buffer => {
          resolve(buffer)
        }, err => {
          console.error('decodeAudioData fail', err)
          reject()
        })
      },
      fail: res => {
        console.error('request fail', res)
        reject()
      }
    })
  })
}

const play = () => {
  loadAudio('xxx-test.mp3').then(buffer => {
    let source = audioCtx.createBufferSource()
    source.buffer = buffer
    source.connect(audioCtx.destination)
    source.start()
  }).catch(() => {
    console.log('fail')
  })
}

play()
```
