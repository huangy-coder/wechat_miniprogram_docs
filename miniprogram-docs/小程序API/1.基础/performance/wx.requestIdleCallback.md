# wx.requestIdleCallback(function callback, Object object)

> 官方文档：[wx.requestIdleCallback(function callback, Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.requestIdleCallback.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 性能 / wx.requestIdleCallback
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.10.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

注册一个函数，将在空闲时期被调用

## 参数

### function callback

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number |   | 否 |   |

## 示例代码

```js
const IdleCallbackId = wx.requestIdleCallback(() => {
  console.log('idle')
}, {
  timeout: 3000
})
```
