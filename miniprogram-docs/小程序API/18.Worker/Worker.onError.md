# Worker.onError(function listener)

> 官方文档：[Worker.onError(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.onError.html)
> 所属分类：[Worker](Worker目录.md)
> 导航路径：Worker / Worker / Worker.onError
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

> 相关文档: [多线程 Worker](https://developers.weixin.qq.com/miniprogram/dev/framework/workers.html)

## 功能描述

监听 Worker 线程错误事件。当 Worker 线程中发生脚本错误时会触发此事件。

## 参数

### function listener

Worker 线程错误事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| error | Object | 错误对象 |

## 示例代码

```js
const worker = wx.createWorker('workers/request/index.js')

worker.onError(function (error) {
  console.error('Worker 错误:', error)
})
```
