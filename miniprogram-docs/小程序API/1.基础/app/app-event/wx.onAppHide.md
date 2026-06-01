# wx.onAppHide(function listener)

> 官方文档：[wx.onAppHide(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAppHide.html)
> 所属分类：[基础](../../基础目录.md)
> 导航路径：基础 / 小程序 / 应用级事件 / wx.onAppHide
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.1.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听小程序切后台事件。该事件与 [`App.onHide`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onhide) 的回调参数一致。

## 参数

### function listener

小程序切后台事件的监听函数

#### 参数

##### Object options

切后台参数

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| reason | number | 原因 | [3.5.7](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 0 | 用户退出小程序 |
| 1 | 进入其他小程序 |
| 2 | 打开原生功能页 |
| 3 | 其他 |
