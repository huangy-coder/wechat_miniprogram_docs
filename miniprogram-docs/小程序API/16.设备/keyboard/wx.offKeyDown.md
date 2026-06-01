# wx.offKeyDown(function listener)

> 官方文档：[wx.offKeyDown(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.offKeyDown.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 键盘 / wx.offKeyDown
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.6.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

移除小程序全局键盘按键按下事件的监听函数

## 参数

### function listener

onKeyDown 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```js
const listener = function (res) { console.log(res) }

wx.onKeyDown(listener)
wx.offKeyDown(listener) // 需传入与监听时同一个的函数对象
```
