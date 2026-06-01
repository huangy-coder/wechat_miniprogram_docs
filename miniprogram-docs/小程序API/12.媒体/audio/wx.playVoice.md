# wx.playVoice(Object object)

> 官方文档：[wx.playVoice(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.playVoice.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / wx.playVoice
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

从基础库 [1.6.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [wx.createInnerAudioContext](wx.createInnerAudioContext.md) 代替

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

开始播放语音。同时只允许一个语音文件正在播放，如果前一个语音文件还没播放完，将中断前一个语音播放。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| filePath | string |   | 是 | 需要播放的语音文件的文件路径 (本地路径) |   |
| duration | number | 60 | 否 | 指定播放时长，到达指定的播放时长后会自动停止播放，单位：秒 | [1.6.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

## 示例代码

```js
wx.startRecord({
  success (res) {
    const tempFilePath = res.tempFilePath
    wx.playVoice({
      filePath: tempFilePath,
      complete () { }
    })
  }
})
```
