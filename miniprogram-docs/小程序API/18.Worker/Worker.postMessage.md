# Worker.postMessage(Object message)

> 官方文档：[Worker.postMessage(Object message)](https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.postMessage.html)
> 所属分类：[Worker](Worker目录.md)
> 导航路径：Worker / Worker / Worker.postMessage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

> 相关文档: [多线程 Worker](https://developers.weixin.qq.com/miniprogram/dev/framework/workers.html)

## 功能描述

向主线程/Worker 线程发送的消息。

## 参数

### Object message

需要发送的消息。

## 示例代码

worker 线程中

```js
worker.postMessage({
  msg: 'hello from worker'
})
```

主线程中

```js
const worker = wx.createWorker('workers/request/index.js')

worker.postMessage({
  msg: 'hello from main'
})
```

## 提醒

在基础库版本2.20.2之前，postMessage仅支持传递可序列化的key-value对象。
在基础库2.20.2之后，postMessage支持传递任意类型的数据。
