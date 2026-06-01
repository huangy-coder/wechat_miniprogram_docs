# MediaQueryObserver

> 官方文档：[MediaQueryObserver](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/MediaQueryObserver.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / MediaQueryObserver
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

MediaQueryObserver 对象，用于监听页面 media query 状态的变化，如界面的长宽是不是在某个指定的范围内。

## 方法

### MediaQueryObserver.observe(Object descriptor, MediaQueryObserver.observeCallback callback)

开始监听页面 media query 变化情况

### MediaQueryObserver.disconnect()

停止监听。回调函数将不再触发
