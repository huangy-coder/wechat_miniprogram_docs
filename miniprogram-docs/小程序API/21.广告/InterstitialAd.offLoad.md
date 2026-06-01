# InterstitialAd.offLoad(function listener)

> 官方文档：[InterstitialAd.offLoad(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/ad/InterstitialAd.offLoad.html)
> 所属分类：[广告](广告目录.md)
> 导航路径：广告 / InterstitialAd / InterstitialAd.offLoad
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

## 功能描述

移除插屏广告加载事件的监听函数

## 参数

### function listener

onLoad 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```js
const listener = function (res) { console.log(res) }

InterstitialAd.onLoad(listener)
InterstitialAd.offLoad(listener) // 需传入与监听时同一个的函数对象
```
