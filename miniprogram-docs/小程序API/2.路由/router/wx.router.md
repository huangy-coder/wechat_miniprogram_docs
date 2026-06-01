# wx.router

> 官方文档：[wx.router](https://developers.weixin.qq.com/miniprogram/dev/api/route/router/wx.router.html)
> 所属分类：[路由](../路由目录.md)
> 导航路径：路由 / 自定义路由 / wx.router
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.29.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [自定义路由](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/custom-route.html)

router 对象，可以通过 `wx.router` 获取。

## 方法

### router.addRouteBuilder(string routeType, CustomRouteBuilder routeBuilder)

添加自定义路由配置

### router.removeRouteBuilder(string routeType)

移除自定义路由配置

### router.getRouteContext(Object this)

获取页面对应的自定义路由上下文对象
