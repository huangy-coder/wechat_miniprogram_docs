# RealtimeTagLogManager

> 官方文档：[RealtimeTagLogManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeTagLogManager.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 调试 / RealtimeTagLogManager
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.16.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [实时日志](https://developers.weixin.qq.com/miniprogram/dev/framework/realtimelog/index.html)

给定标签的实时日志管理器实例，可以通过 [RealtimeLogManager.tag](RealtimeLogManager.tag.md) 接口获取，目前只支持在插件使用。

## 方法

### RealtimeTagLogManager.info(string key, Object|Array.<any>|number|string value)

写 info 日志

### RealtimeTagLogManager.warn(string key, Object|Array.<any>|number|string value)

写 warn 日志

### RealtimeTagLogManager.error(string key, Object|Array.<any>|number|string value)

写 error 日志

### RealtimeTagLogManager.setFilterMsg(string msg)

设置过滤关键字

### RealtimeTagLogManager.addFilterMsg(string msg)

添加过滤关键字

## 使用说明

[RealtimeTagLogManager](RealtimeTagLogManager.md) 功能和 [RealtimeLogManager](RealtimeLogManager.md) 相似，但是为了让输出的实时日志更易于分析，其具有更严格的格式要求。
 [RealtimeTagLogManager](RealtimeTagLogManager.md) 使用时需要传入标签，调用该实例所输出的日志均会被汇集到对应标签下，同时该实例的日志只支持 key-value 格式进行输出。
