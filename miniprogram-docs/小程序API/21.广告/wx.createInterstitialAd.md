# InterstitialAd wx.createInterstitialAd(Object object)

> 官方文档：[InterstitialAd wx.createInterstitialAd(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ad/wx.createInterstitialAd.html)
> 所属分类：[广告](广告目录.md)
> 导航路径：广告 / wx.createInterstitialAd
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.6.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.8.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

创建插屏广告组件。请通过 [wx.getSystemInfoSync()](../1.基础/system/wx.getSystemInfoSync.md) 返回对象的 SDKVersion 判断基础库版本号后再使用该 API。每次调用该方法创建插屏广告都会返回一个全新的实例（小程序端的插屏广告实例不允许跨页面使用）。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| adUnitId | string |   | 是 | 广告单元 id |

## 返回值

### InterstitialAd

插屏广告组件
