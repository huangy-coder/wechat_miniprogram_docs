# wx.rewriteRoute(Object object)

> 官方文档：[wx.rewriteRoute(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.rewriteRoute.html)
> 所属分类：[路由](路由目录.md)
> 导航路径：路由 / wx.rewriteRoute
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.8.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：支持
> 在小程序插件中使用时，只能重写目标为当前插件的页面的路由事件

## 功能描述

重写正在进行中的路由事件，详见 [路由重写](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-rewrite.html)

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | string |   | 是 | 重写目标页面的路径 (代码包路径), 路径后可以带参数。参数与路径之间使用 `?` 分隔，参数键与参数值用 `=` 相连，不同参数用 `&` 分隔；如 `'path?key=value&key2=value2'` |
| preserveQuery | boolean | false | 否 | 是否直接保留当前路由事件的参数，默认为 `false`；开启时，`url` 里面传入的参数会被丢弃 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

## 示例代码

```js
wx.onBeforeAppRoute(res => {
  if (res.path === '/pages/do/not/access/me') {
    wx.rewriteRoute({
      url: '/pages/index/index'
    })
  }
})
```
