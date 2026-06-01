# wx.onUnhandledRejection(function listener)

> 官方文档：[wx.onUnhandledRejection(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onUnhandledRejection.html)
> 所属分类：[基础](../../基础目录.md)
> 导航路径：基础 / 小程序 / 应用级事件 / wx.onUnhandledRejection
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.10.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听未处理的 Promise 拒绝事件。该事件与 [`App.onUnhandledRejection`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onUnhandledRejection-Object-object) 的回调时机与参数一致。

## 参数

### function listener

未处理的 Promise 拒绝事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| reason | string | 拒绝原因，一般是一个 Error 对象 |
| promise | Promise.<any> | 被拒绝的 Promise 对象 |

## 注意

- 所有的 unhandledRejection 都可以被这一监听捕获，但只有 Error 类型的才会在小程序后台触发报警。
