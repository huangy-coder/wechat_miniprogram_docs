# TCPSocket.offError(function listener)

> 官方文档：[TCPSocket.offError(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.offError.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / TCP 通信 / TCPSocket / TCPSocket.offError
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)

## 功能描述

移除当错误发生时触发的监听函数

## 参数

### function listener

onError 传入的监听函数。不传此参数则移除所有监听函数。

## 示例代码

```js
const listener = function (res) { console.log(res) }

TCPSocket.onError(listener)
TCPSocket.offError(listener) // 需传入与监听时同一个的函数对象
```
