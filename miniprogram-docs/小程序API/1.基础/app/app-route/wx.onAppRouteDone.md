# wx.onAppRouteDone(function listener)

> 官方文档：[wx.onAppRouteDone(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAppRouteDone.html)
> 所属分类：[基础](../../基础目录.md)
> 导航路径：基础 / 小程序 / 路由事件 / wx.onAppRouteDone
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.5.5 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [3.5.5](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听当前路由动画执行完成的事件监听，详见 [页面路由监听](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-event-listener.html)。

## 参数

### function listener

当前路由动画执行完成的事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| path | string | 页面路径 |
| query | Object | 路由参数 |
| openType | string | 路由打开类型 |
| webviewId | number | 当前页面 id |
| timeStamp | number | 路由下发的时间戳 |
| routeEventId | string | 路由事件 id |

## 注意

在低于 3.5.5 版本的基础库中也存在此接口，但参数可能与当前文档不同，请注意。

## 示例代码

```js
const func = function (res) {
  console.log(res)
}
wx.onAppRouteDone(func)
// 取消监听
wx.offAppRouteDone(func)
```
