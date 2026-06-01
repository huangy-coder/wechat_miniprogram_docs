# InterstitialAd

> 官方文档：[InterstitialAd](https://developers.weixin.qq.com/miniprogram/dev/api/ad/InterstitialAd.html)
> 所属分类：[广告](广告目录.md)
> 导航路径：广告 / InterstitialAd
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

插屏广告组件。插屏广告组件是一个原生组件，层级比普通组件高。插屏广告组件每次创建都会返回一个全新的实例（小程序端的插屏广告实例不允许跨页面使用），默认是隐藏的，需要调用 InterstitialAd.show() 将其显示。

## 方法

### Promise InterstitialAd.show()

显示插屏广告。

### Promise InterstitialAd.load()

加载插屏广告。

### InterstitialAd.destroy()

销毁插屏广告实例。

### InterstitialAd.onLoad(function listener)

监听插屏广告加载事件。

### InterstitialAd.offLoad(function listener)

移除插屏广告加载事件的监听函数

### InterstitialAd.onError(function listener)

监听插屏错误事件。

### InterstitialAd.offError(function listener)

移除插屏错误事件的监听函数

### InterstitialAd.onClose(function listener)

监听插屏广告关闭事件。

### InterstitialAd.offClose(function listener)

移除插屏广告关闭事件的监听函数
