# wx.onWindowResize(function listener)

> 官方文档：[wx.onWindowResize(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.onWindowResize.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 窗口 / wx.onWindowResize
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.3.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听窗口尺寸变化事件

## 参数

### function listener

窗口尺寸变化事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| size | Object |   |

补充表：
| 结构属性 | 类型 | 说明 |
| --- | --- | --- |
| windowWidth | number | 变化后的窗口宽度，单位 px |
| windowHeight | number | 变化后的窗口高度，单位 px |
