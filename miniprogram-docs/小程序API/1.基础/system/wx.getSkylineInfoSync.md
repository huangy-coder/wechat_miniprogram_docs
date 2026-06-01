# Object wx.getSkylineInfoSync()

> 官方文档：[Object wx.getSkylineInfoSync()](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSkylineInfoSync.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 系统 / wx.getSkylineInfoSync
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.26.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.26.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

## 功能描述

获取当前运行环境对于 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html) 的支持情况

## 返回值

### Object

当前运行环境对于 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html) 的支持情况

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| isSupported | boolean | 当前运行环境是否支持 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html) |
| version | string | 当前运行环境 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html) 的版本号，形如 `0.9.7` |
| reason | string | 当前运行环境不支持 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html) 的原因，仅在 `isSupported` 为 `false` 时出现 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| client not supported | 当前微信客户端不支持 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)，可以尝试通过升级微信客户端解决 |
| baselib not supported | 当前基础库不支持 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)，基础库会自动更新到当前客户端所能支持的最新的版本，基础库不支持时也可以尝试通过升级微信客户端解决 |
| a-b test not enabled | 命中了 _We 分析_ 平台上的 AB 实验关闭的情况。详细可以查看 [Skyline 起步 > 配置 We 分析 AB 实验](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/migration.html#%E9%85%8D%E7%BD%AE-We-%E5%88%86%E6%9E%90-AB-%E5%AE%9E%E9%AA%8C) 一节 |
| SwitchRender option set to webview | 本地调试的快捷切换入口被设置为了强制使用 Webview. 详情可以查看 [Skyline 起步 > 快捷切换入口](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/migration.html#快捷切换入口) 一节 |
