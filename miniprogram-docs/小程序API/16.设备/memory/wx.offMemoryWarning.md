# wx.offMemoryWarning(function listener)

> 官方文档：[wx.offMemoryWarning(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/memory/wx.offMemoryWarning.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 内存 / wx.offMemoryWarning
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.9.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

> 相关文档: [内存优化](https://developers.weixin.qq.com/miniprogram/dev/framework/performance/tips/runtime_memory.html)

## 功能描述

移除内存不足告警事件的监听函数

## 参数

### function listener

onMemoryWarning 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```js
const listener = function (res) { console.log(res) }

wx.onMemoryWarning(listener)
wx.offMemoryWarning(listener) // 需传入与监听时同一个的函数对象
```
