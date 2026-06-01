# Promise wx.getRendererUserAgent(Object object)

> 官方文档：[Promise wx.getRendererUserAgent(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getRendererUserAgent.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 系统 / wx.getRendererUserAgent
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.26.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [3.11.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

## 功能描述

获取 Webview 小程序的 UserAgent

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### string userAgent

UserAgent

## 返回值

### Promise.<string>

## 示例代码

```js
// v2.30.4 前，仅支持 promise 风格调用
wx.getRendererUserAgent().then(userAgent => console.log(userAgent))
// v2.30.4 起，除 promise 风格调用外，也支持 invoke 风格使用
wx.getRendererUserAgent({
  success(res) { console.log(res.userAgent) }
})
```
