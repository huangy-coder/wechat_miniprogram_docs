# wx.onLocalServiceFound(function listener)

> 官方文档：[wx.onLocalServiceFound(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.onLocalServiceFound.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / mDNS / wx.onLocalServiceFound
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.4.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.15.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

> 相关文档: [局域网通信](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/mDNS.html)

## 功能描述

监听 mDNS 服务发现的事件

## 参数

### function listener

mDNS 服务发现的事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| serviceType | string | 服务的类型 |
| serviceName | string | 服务的名称 |
| ip | string | 服务的 ip 地址 |
| port | number | 服务的端口 |
