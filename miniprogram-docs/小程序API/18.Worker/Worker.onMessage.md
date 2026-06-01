# Worker.onMessage(function listener)

> 官方文档：[Worker.onMessage(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.onMessage.html)
> 所属分类：[Worker](Worker目录.md)
> 导航路径：Worker / Worker / Worker.onMessage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

> 相关文档: [多线程 Worker](https://developers.weixin.qq.com/miniprogram/dev/framework/workers.html)

## 功能描述

监听主线程/Worker 线程向当前线程发送的消息的事件。

## 参数

### function listener

主线程/Worker 线程向当前线程发送的消息的事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| message | Object | 主线程/Worker 线程向当前线程发送的消息 |
