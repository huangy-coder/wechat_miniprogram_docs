# RequestTask.onHeadersReceived(function listener)

> 官方文档：[RequestTask.onHeadersReceived(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/RequestTask.onHeadersReceived.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / 发起请求 / RequestTask / RequestTask.onHeadersReceived
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.1.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)、[局域网通信](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/mDNS.html)、[移动解析HttpDNS](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/HTTPDNS.html)

## 功能描述

监听 HTTP Response Header 事件。会比请求完成事件更早

## 参数

### function listener

HTTP Response Header 事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| header | Object | 开发者服务器返回的 HTTP Response Header |
| statusCode | Number | 开发者服务器返回的 HTTP 状态码 （目前开发者工具上不会返回 statusCode 字段，可用真机查看该字段，后续将会支持） |
| cookies | Array.<string> | 开发者服务器返回的 cookies，格式为字符串数组 |
