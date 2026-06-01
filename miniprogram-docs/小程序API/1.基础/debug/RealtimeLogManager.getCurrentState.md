# Object RealtimeLogManager.getCurrentState()

> 官方文档：[Object RealtimeLogManager.getCurrentState()](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeLogManager.getCurrentState.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 调试 / RealtimeLogManager / RealtimeLogManager.getCurrentState
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.19.4 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

实时日志会将一定时间间隔内缓存的日志聚合上报，如果该时间内缓存的内容超出限制，则会被丢弃。此方法可以获取当前缓存剩余空间。

> 注意：基础库内部在对日志进行上报时会补充一些结构化数据，如果遇到上报溢出的情况也会补充警告日志，所以此方法获取到的当前占用信息会比预期的大一些。

## 返回值

### Object

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| size | number | 当前缓存中已使用空间，以字节为单位 |
| maxSize | number | 当前缓存最大可用空间，以字节为单位 |
| logCount | number | 当前缓存中的日志条数 |
| maxLogCount | number | 当前缓存中最大可存日志条数 |
