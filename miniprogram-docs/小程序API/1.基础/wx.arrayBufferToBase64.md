# string wx.arrayBufferToBase64(ArrayBuffer arrayBuffer)

> 官方文档：[string wx.arrayBufferToBase64(ArrayBuffer arrayBuffer)](https://developers.weixin.qq.com/miniprogram/dev/api/base/wx.arrayBufferToBase64.html)
> 所属分类：[基础](基础目录.md)
> 导航路径：基础 / wx.arrayBufferToBase64
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

从基础库 [2.4.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护

> 基础库 1.1.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

将 ArrayBuffer 对象转成 Base64 字符串

## 参数

### ArrayBuffer arrayBuffer

要转换成 Base64 字符串的 ArrayBuffer 对象

## 返回值

### string

Base64 字符串

## 示例代码

```javascript
const arrayBuffer = new Uint8Array([11, 22, 33])
const base64 = wx.arrayBufferToBase64(arrayBuffer)
```
