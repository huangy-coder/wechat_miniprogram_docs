# wx.onAfterPageUnload(function listener)

> 官方文档：[wx.onAfterPageUnload(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAfterPageUnload.html)
> 所属分类：[基础](../../基础目录.md)
> 导航路径：基础 / 小程序 / 路由事件 / wx.onAfterPageUnload
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.5.5 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [3.5.5](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听路由事件引起现有页面实例销毁时，页面实例销毁后的事件监听，详见 [页面路由监听](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-event-listener.html)。

## 参数

### function listener

路由事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| path | string | 页面路径 |
| routeEventId | string | 路由事件 id |

## 示例代码

```js
const func = function (res) {
  console.log(res)
}
wx.onAfterPageUnload(func)
// 取消监听
wx.offAfterPageUnload(func)
```
