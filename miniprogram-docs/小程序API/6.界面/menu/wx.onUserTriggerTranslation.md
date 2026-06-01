# wx.onUserTriggerTranslation(function listener)

> 官方文档：[wx.onUserTriggerTranslation(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.onUserTriggerTranslation.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 菜单 / wx.onUserTriggerTranslation
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.7.9 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听用户触发小程序菜单中翻译功能的事件

## 参数

### function listener

用户触发小程序菜单中翻译功能的事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| locale | string | 翻译到的目标语言 |
| type | string | 触发来源， `button` 表示点击了菜单中的翻译按钮， `capsule` 表示点击了胶囊中的翻译提示 |

## 示例代码

```js
const callback = res => console.log('userTriggerTranslation', res)

wx.onUserTriggerTranslation(callback)
// 取消监听
wx.offUserTriggerTranslation(callback)
```
