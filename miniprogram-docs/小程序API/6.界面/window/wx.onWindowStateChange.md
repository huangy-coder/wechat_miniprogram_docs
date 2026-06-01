# wx.onWindowStateChange(function listener)

> 官方文档：[wx.onWindowStateChange(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.onWindowStateChange.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 窗口 / wx.onWindowStateChange
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.8.8 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

监听小程序窗口状态变化事件。仅适用于 PC 平台

## 参数

### function listener

小程序窗口状态变化事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| state | string | 改变的窗口状态，可能的值为： |

- 'minimize'：窗口最小化
- 'normalize'：窗口恢复正常尺寸
- 'maximize'：窗口最大化 |
