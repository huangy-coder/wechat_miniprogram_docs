# wx.setNavigationBarTitle(Object object)

> 官方文档：[wx.setNavigationBarTitle(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.setNavigationBarTitle.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 导航栏 / wx.setNavigationBarTitle
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **需要页面权限**：当前是插件页面时，宿主小程序不能调用该接口，反之亦然
> **小程序插件**：支持，需要小程序基础库版本不低于 [2.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> 在小程序插件中使用时，只能在当前插件的页面中调用
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

动态设置当前页面的标题

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| title | string |   | 是 | 页面标题 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

## 示例代码

```js
wx.setNavigationBarTitle({
  title: '当前页面'
})
```
