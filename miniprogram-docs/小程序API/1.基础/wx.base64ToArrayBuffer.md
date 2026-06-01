# ArrayBuffer wx.base64ToArrayBuffer(string base64)

> 官方文档：[ArrayBuffer wx.base64ToArrayBuffer(string base64)](https://developers.weixin.qq.com/miniprogram/dev/api/base/wx.base64ToArrayBuffer.html)
> 所属分类：[基础](基础目录.md)
> 导航路径：基础 / wx.base64ToArrayBuffer
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

从基础库 [2.4.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护

> 基础库 1.1.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

将 Base64 字符串转成 ArrayBuffer 对象

## 参数

### string base64

要转化成 ArrayBuffer 对象的 Base64 字符串

## 返回值

### ArrayBuffer

ArrayBuffer 对象

## 示例代码

```javascript
const base64 = 'CxYh'
const arrayBuffer = wx.base64ToArrayBuffer(base64)
```
