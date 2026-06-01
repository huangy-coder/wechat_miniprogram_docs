# boolean wx.isVKSupport(string version)

> 官方文档：[boolean wx.isVKSupport(string version)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/wx.isVKSupport.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / wx.isVKSupport
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.22.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.22.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

判断支持版本

## 参数

### string version

**version 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| v1 | 旧版本 |   |
| v2 | v2 版本，目前只有 iOS 基础库 2.22.0 以上支持 |   |

## 返回值

### boolean

是否支持对应版本的 vision kit

## 示例代码

```js
const isSupportV2 = wx.isVKSupport('v2')
```
