# wx.setTabBarItem(Object object)

> 官方文档：[wx.setTabBarItem(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.setTabBarItem.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / Tab Bar / wx.setTabBarItem
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.9.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **需要页面权限**：当前是插件页面时，宿主小程序不能调用该接口，反之亦然
> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

动态设置 tabBar 某一项的内容，`2.7.0` 起图片支持临时文件和网络文件。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| index | number |   | 是 | tabBar 的哪一项，从左边算起 |
| text | string |   | 否 | tab 上的按钮文字 |
| iconPath | string |   | 否 | 图片路径，icon 大小限制为 40kb，建议尺寸为 81px * 81px，当 postion 为 top 时，此参数无效 |
| selectedIconPath | string |   | 否 | 选中时的图片路径，icon 大小限制为 40kb，建议尺寸为 81px * 81px ，当 postion 为 top 时，此参数无效 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

## 示例代码

```js
wx.setTabBarItem({
  index: 0,
  text: 'text',
  iconPath: '/path/to/iconPath',
  selectedIconPath: '/path/to/selectedIconPath'
})
```
