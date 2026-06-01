# InnerAudioContext.offCanplay(function listener)

> 官方文档：[InnerAudioContext.offCanplay(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.offCanplay.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / InnerAudioContext / InnerAudioContext.offCanplay
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.9.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

## 功能描述

移除音频进入可以播放状态的事件的监听函数

## 参数

### function listener

onCanplay 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```js
const listener = function (res) { console.log(res) }

InnerAudioContext.onCanplay(listener)
InnerAudioContext.offCanplay(listener) // 需传入与监听时同一个的函数对象
```
