# LivePusherContext.onCustomRendererEvent(string event, function|function callback)

> 官方文档：[LivePusherContext.onCustomRendererEvent(string event, function|function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.onCustomRendererEvent.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 实时音视频 / LivePusherContext / LivePusherContext.onCustomRendererEvent
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.29.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

> 相关文档: [live-pusher 组件](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)

## 功能描述

开启自定义渲染时，开发者通过此方法订阅相关事件，客户端 8.0.31 版本开始支持。

## 参数

### string event

事件类型，后订阅的监听器会取消之前的监听器

**event 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| frame | 采集到视频帧后触发 |   |
| update | 推流尺寸变更时触发 |   |

### function|function callback

自定义渲染事件处理回调函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 推流宽度 |
| height | number | 推流高度 |
