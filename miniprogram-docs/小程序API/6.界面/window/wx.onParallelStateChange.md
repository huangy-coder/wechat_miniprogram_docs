# wx.onParallelStateChange(function listener)

> 官方文档：[wx.onParallelStateChange(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.onParallelStateChange.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 窗口 / wx.onParallelStateChange
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.12.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

监听小程序分栏状态变化事件。仅适用于 PC 平台

## 参数

### function listener

小程序分栏状态变化事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| isOnParallel | boolean | 当前是否分栏 |
| rightPage | Page | 分栏右侧页面对象（非分栏状态时返回当前页面） |
| leftPage | Page | 分栏左侧页面对象（非分栏状态时返回当前页面） |
