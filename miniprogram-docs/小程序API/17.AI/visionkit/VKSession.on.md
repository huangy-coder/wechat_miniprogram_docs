# VKSession.on(string eventName, function fn)

> 官方文档：[VKSession.on(string eventName, function fn)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.on.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKSession / VKSession.on
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.20.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

监听会话事件。

## 参数

### string eventName

事件名称

**eventName 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| resize | 相机尺寸变化事件，回调参数为相机尺寸 |   |
| addAnchors | 增加 anchor 事件，回调参数为 [VKPlaneAnchor](VKPlaneAnchor.md)/[VKMarkerAnchor](VKMarkerAnchor.md)/[VKOSDAnchor](VKOSDAnchor.md) 列表（只有v2版本支持） 或 [VKFaceAnchor](VKFaceAnchor.md)/[VKOCRAnchor](VKOCRAnchor.md)/[VKHandAnchor](VKHandAnchor.md)/[VKBodyAnchor](VKBodyAnchor.md)列表（v1、v2都支持） | [2.22.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| updateAnchors | 更新 anchor 事件，回调参数为 [VKPlaneAnchor](VKPlaneAnchor.md)/[VKMarkerAnchor](VKMarkerAnchor.md)/[VKOSDAnchor](VKOSDAnchor.md) 列表（只有v2版本支持） 或 [VKFaceAnchor](VKFaceAnchor.md)/[VKOCRAnchor](VKOCRAnchor.md)/[VKHandAnchor](VKHandAnchor.md)/[VKBodyAnchor](VKBodyAnchor.md)列表（v1、v2都支持） | [2.22.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| removeAnchors | 删除 anchor 事件，回调参数为 [VKPlaneAnchor](VKPlaneAnchor.md)/[VKMarkerAnchor](VKMarkerAnchor.md)/[VKOSDAnchor](VKOSDAnchor.md) 列表（只有v2版本支持） 或 [VKFaceAnchor](VKFaceAnchor.md)/[VKOCRAnchor](VKOCRAnchor.md)/[VKHandAnchor](VKHandAnchor.md)/[VKBodyAnchor](VKBodyAnchor.md) 列表（v1、v2都支持） | [2.22.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

### function fn

事件监听函数
