# LivePlayerContext.requestFullScreen(Object object)

> 官方文档：[LivePlayerContext.requestFullScreen(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.requestFullScreen.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 实时音视频 / LivePlayerContext / LivePlayerContext.requestFullScreen
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：支持

> 相关文档: [live-player 组件](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html)

## 功能描述

进入全屏

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| direction | number | 0 | 否 | 设置全屏时的方向 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 0 | 正常竖向 |
| 90 | 屏幕逆时针90度 |
| -90 | 屏幕顺时针90度 |
