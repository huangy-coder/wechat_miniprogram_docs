# wx.getBackgroundAudioPlayerState(Object object)

> 官方文档：[wx.getBackgroundAudioPlayerState(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.getBackgroundAudioPlayerState.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 背景音频 / wx.getBackgroundAudioPlayerState
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

从基础库 [1.2.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [wx.getBackgroundAudioManager](wx.getBackgroundAudioManager.md) 代替

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

## 功能描述

获取后台音乐播放状态。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| duration | number | 选定音频的长度（单位：s），只有在音乐播放中时返回 |
| currentPosition | number | 选定音频的播放位置（单位：s），只有在音乐播放中时返回 |
| status | number | 播放状态 |
| downloadPercent | number | 音频的下载进度百分比，只有在音乐播放中时返回 |
| dataUrl | string | 歌曲数据链接，只有在音乐播放中时返回 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 0 | 暂停中 |
| 1 | 播放中 |
| 2 | 没有音乐播放 |

## 示例代码

```js
wx.getBackgroundAudioPlayerState({
  success (res) {
    const status = res.status
    const dataUrl = res.dataUrl
    const currentPosition = res.currentPosition
    const duration = res.duration
    const downloadPercent = res.downloadPercent
  }
})
```
