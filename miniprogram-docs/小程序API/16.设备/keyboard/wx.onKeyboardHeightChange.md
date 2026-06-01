# wx.onKeyboardHeightChange(function listener)

> 官方文档：[wx.onKeyboardHeightChange(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.onKeyboardHeightChange.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 键盘 / wx.onKeyboardHeightChange
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听键盘高度变化事件

## 参数

### function listener

键盘高度变化事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| height | number | 键盘高度 |

## 示例代码

```js
wx.onKeyboardHeightChange(res => {
  console.log(res.height)
})
```
