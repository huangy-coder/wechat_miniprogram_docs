# Worker.onProcessKilled(function listener)

> 官方文档：[Worker.onProcessKilled(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.onProcessKilled.html)
> 所属分类：[Worker](Worker目录.md)
> 导航路径：Worker / Worker / Worker.onProcessKilled
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

> 相关文档: [多线程 Worker](https://developers.weixin.qq.com/miniprogram/dev/framework/workers.html)

## 功能描述

监听 worker线程被系统回收事件（开启 useExperimentalWorker 后，当iOS系统资源紧张时，ExperimentalWorker 线程存在被系统回收的可能，开发者可监听此事件并重新创建一个worker）。仅限在主线程 worker 对象上调用。

## 参数

### function listener

worker线程被系统回收事件的监听函数
