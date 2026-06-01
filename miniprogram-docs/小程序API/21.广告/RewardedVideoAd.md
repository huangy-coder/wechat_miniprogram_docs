# RewardedVideoAd

> 官方文档：[RewardedVideoAd](https://developers.weixin.qq.com/miniprogram/dev/api/ad/RewardedVideoAd.html)
> 所属分类：[广告](广告目录.md)
> 导航路径：广告 / RewardedVideoAd
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

激励视频广告组件。激励视频广告组件是一个原生组件，层级比普通组件高。激励视频广告是一个单例（小游戏端是全局单例，小程序端是页面内单例，在小程序端的单例对象不允许跨页面使用），默认是隐藏的，需要调用 RewardedVideoAd.show() 将其显示。

## 方法

### Promise RewardedVideoAd.load()

加载激励视频广告。

### Promise RewardedVideoAd.show()

显示激励视频广告。激励视频广告将从屏幕下方推入。

### RewardedVideoAd.destroy()

销毁激励视频广告实例。

### RewardedVideoAd.onLoad(function listener)

监听激励视频广告加载事件。

### RewardedVideoAd.offLoad(function listener)

移除激励视频广告加载事件的监听函数

### RewardedVideoAd.onError(function listener)

监听激励视频错误事件。

### RewardedVideoAd.offError(function listener)

移除激励视频错误事件的监听函数

### RewardedVideoAd.onClose(function listener)

监听用户点击 `关闭广告` 按钮的事件。

### RewardedVideoAd.offClose(function listener)

移除用户点击 `关闭广告` 按钮的事件的监听函数
