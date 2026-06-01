# wx.setWindowSize(Object object)

> 官方文档：[wx.setWindowSize(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.setWindowSize.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 窗口 / wx.setWindowSize
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

从基础库 [2.11.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护

> 基础库 2.10.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

设置窗口大小，该接口仅适用于 PC 平台，使用细则请参见指南

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| width | number |   | 是 | 窗口宽度，以像素为单位 |
| height | number |   | 是 | 窗口高度，以像素为单位 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |
