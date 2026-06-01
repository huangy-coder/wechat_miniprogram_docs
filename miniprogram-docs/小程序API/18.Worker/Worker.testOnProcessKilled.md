# Worker.testOnProcessKilled()

> 官方文档：[Worker.testOnProcessKilled()](https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.testOnProcessKilled.html)
> 所属分类：[Worker](Worker目录.md)
> 导航路径：Worker / Worker / Worker.testOnProcessKilled
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.27.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

用于模拟 iOS ExperimentalWorker 线程被系统回收事件，以便于调试。接口仅在 worker 线程内可用。参考 [Worker.onProcessKilled](Worker.onProcessKilled.md)

## 示例代码

```js
// game.js
const worker = wx.createWorker('workers/index.js', {
  useExperimentalWorker: true
})

// 监听 ExperimentalWorker 被系统回收事件
worker.onProcessKilled(function () {
  console.log('worker has been killed')
  // 重新创建一个worker
  // wx.createWorker()
})
```

```js
// workers/index.js
setTimeout(() => {
  // 模拟 ExperimentalWorker 线程被系统回收事件
  worker.testOnProcessKilled()
}, 2000)
```
