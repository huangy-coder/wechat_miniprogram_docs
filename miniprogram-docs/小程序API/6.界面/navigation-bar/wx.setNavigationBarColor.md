# wx.setNavigationBarColor(Object object)

> 官方文档：[wx.setNavigationBarColor(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.setNavigationBarColor.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 导航栏 / wx.setNavigationBarColor
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.4.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **需要页面权限**：当前是插件页面时，宿主小程序不能调用该接口，反之亦然
> **小程序插件**：支持，需要小程序基础库版本不低于 [2.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> 在小程序插件中使用时，只能在当前插件的页面中调用
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

设置页面导航条颜色

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| frontColor | string |   | 是 | 前景颜色值，包括按钮、标题、状态栏的颜色，仅支持 #ffffff 和 #000000 |
| backgroundColor | string |   | 是 | 背景颜色值，有效值为十六进制颜色 |
| animation | Object |   | 否 | 动画效果 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

补充表：
| 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 0 | 否 | 动画变化时间，单位 ms |
| timingFunc | string | 'linear' | 否 | 动画变化方式 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 'linear' | 动画从头到尾的速度是相同的 |
| 'easeIn' | 动画以低速开始 |
| 'easeOut' | 动画以低速结束 |
| 'easeInOut' | 动画以低速开始和结束 |

## 示例代码

```javascript
wx.setNavigationBarColor({
  frontColor: '#ffffff',
  backgroundColor: '#ff0000',
  animation: {
    duration: 400,
    timingFunc: 'easeIn'
  }
})
```
