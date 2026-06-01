# Worker

> 官方文档：[Worker](https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.html)
> 所属分类：[Worker](Worker目录.md)
> 导航路径：Worker / Worker
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [多线程 Worker](https://developers.weixin.qq.com/miniprogram/dev/framework/workers.html)

Worker 实例，主线程中可通过 [wx.createWorker](wx.createWorker.md) 接口获取，worker 线程中可通过全局变量 `worker` 获取。

## 属性

### Object env

worker内的环境变量

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| USER_DATA_PATH | string | 文件系统中的用户目录路径 (本地路径) |

## 方法

### Worker.postMessage(Object message)

向主线程/Worker 线程发送的消息。

### Worker.terminate()

结束当前 Worker 线程。仅限在主线程 worker 对象上调用。

### Worker.testOnProcessKilled()

用于模拟 iOS ExperimentalWorker 线程被系统回收事件，以便于调试。接口仅在 worker 线程内可用。参考 [Worker.onProcessKilled](Worker.onProcessKilled.md)

### Worker.onMessage(function listener)

监听主线程/Worker 线程向当前线程发送的消息的事件。

### Worker.onError(function listener)

监听 Worker 线程错误事件。当 Worker 线程中发生脚本错误时会触发此事件。

### Worker.onProcessKilled(function listener)

监听 worker线程被系统回收事件（开启 useExperimentalWorker 后，当iOS系统资源紧张时，ExperimentalWorker 线程存在被系统回收的可能，开发者可监听此事件并重新创建一个worker）。仅限在主线程 worker 对象上调用。

## 示例代码

运行以下代码需先进行基础配置，详细请查阅 [多线程 Worker](https://developers.weixin.qq.com/miniprogram/dev/framework/workers.html) 文档了解基础知识和配置方法。

```js
const worker = wx.createWorker('workers/request/index.js') // 文件名指定 worker 的入口文件路径，绝对路径

worker.onMessage(function (res) {
  console.log(res)
})
// 监听worker被系统回收事件
worker.onProcessKilled(function () {
  console.log('worker has been killed')
  // 重新创建一个worker
  // wx.createWorker()
})

worker.postMessage({
  msg: 'hello worker'
})

worker.terminate()
```
