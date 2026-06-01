# wx.onUserOffTranslation(function listener)

> 官方文档：[wx.onUserOffTranslation(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.onUserOffTranslation.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 菜单 / wx.onUserOffTranslation
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.14.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听用户主动取消翻译的事件

## 参数

### function listener

用户主动取消翻译的事件的监听函数

## 示例代码

```js
const callback = () => console.log('userTriggerTranslation')

wx.onUserOffTranslation(callback)
// 取消监听
wx.offUserOffTranslation(callback)
```
