# wx.showToast(Object object)

> 官方文档：[wx.showToast(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showToast.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 交互 / wx.showToast
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

显示消息提示框

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| title | string |   | 是 | 提示的内容 |   |
| icon | string | success | 否 | 图标 |   |
| image | string |   | 否 | 自定义图标的本地路径，image 的优先级高于 icon | [1.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| duration | number | 1500 | 否 | 提示的延迟时间 |   |
| mask | boolean | false | 否 | 是否显示透明蒙层，防止触摸穿透 |   |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

补充表：
| 合法值 | 说明 | 最低版本 |
| --- | --- | --- |
| success | 显示成功图标，此时 title 文本最多显示 7 个汉字长度 |   |
| error | 显示失败图标，此时 title 文本最多显示 7 个汉字长度 | [2.14.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| loading | 显示加载图标，此时 title 文本最多显示 7 个汉字长度 |   |
| none | 不显示图标，此时 title 文本最多可显示两行，[1.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)及以上版本支持 |   |

## 示例代码

```js
wx.showToast({
  title: '成功',
  icon: 'success',
  duration: 2000
})
```

## 注意

- [wx.showLoading](wx.showLoading.md) 和 [wx.showToast](wx.showToast.md) 同时只能显示一个
- [wx.showToast](wx.showToast.md) 应与 [wx.hideToast](wx.hideToast.md) 配对使用
