# wx.offAudioInterruptionBegin(function listener)

> 官方文档：[wx.offAudioInterruptionBegin(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offAudioInterruptionBegin.html)
> 所属分类：[基础](../../基础目录.md)
> 导航路径：基础 / 小程序 / 应用级事件 / wx.offAudioInterruptionBegin
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.6.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.15.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

移除音频因为受到系统占用而被中断开始事件的监听函数

## 参数

### function listener

onAudioInterruptionBegin 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```js
const listener = function (res) { console.log(res) }

wx.onAudioInterruptionBegin(listener)
wx.offAudioInterruptionBegin(listener) // 需传入与监听时同一个的函数对象
```
