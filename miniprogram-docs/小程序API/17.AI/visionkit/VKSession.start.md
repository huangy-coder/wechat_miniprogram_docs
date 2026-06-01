# VKSession.start(function callback)

> 官方文档：[VKSession.start(function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.start.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKSession / VKSession.start
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.20.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

开启会话。

## 参数

### function callback

开启会话回调

#### 参数

##### number status

**status 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 成功 |   |
| 104 | 用户取消授权 |   |
| 112 | 接口未在隐私协议中声明 |   |
| 1025 | 小程序隐私接口被封禁，[解决方案参考链接](https://developers.weixin.qq.com/community/develop/doc/00062a6d514c88baacdf52e8a56009) |   |
| 1026 | 小游戏隐私接口被封禁，[解决方案参考链接](https://developers.weixin.qq.com/community/minigame/doc/0004c84925817819b7ffd8b2356008) |   |
| 2000001 | 参数错误 |   |
| 2003000 | 会话不可用 |   |
| 2000000 | 系统错误 |   |
| 2000002 | 设备不支持 |   |
| 2000003 | 系统不支持 |   |
| 2000004 | 设备不支持 |   |
| 2003001 | 未开启系统相机权限 |   |
| 2003002 | 未开启小程序相机权限 |   |
