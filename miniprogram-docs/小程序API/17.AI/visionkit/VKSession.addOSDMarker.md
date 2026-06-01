# number VKSession.addOSDMarker(string path)

> 官方文档：[number VKSession.addOSDMarker(string path)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.addOSDMarker.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKSession / VKSession.addOSDMarker
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.24.5 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.24.5](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

添加一个 OSD marker（one-shot detection marker），要求调 [wx.createVKSession](wx.createVKSession.md) 时传入的 track.OSD 为 true

## 参数

### string path

图片路径，目前只支持本地用户图片

## 返回值

### number

marker id

## 使用提示

注意事项：

1. 使用 addOSDMarker 接口之前，需要在 createVKSession 的时候声明开启 OSD 跟踪。即 wx.createVKSession({ track: { OSD: true } })
2. 可以添加多个 OSDMarker 图片，但不能重复添加相同的 OSDMarker 图片。

对传入的图片有如下要求：

1. 格式：jpg 格式彩色图片
2. 分辨率：尺寸不低于 240x240
3. 宽高比：在 1:1 ~ 16:9 之间，要求尽量方正，避免狭长的图片
4. 质量：目标物体需要占画面主体，避免大面积留白，避免大面积文字，不能含其他物体。

示例：







建议：

1. 具有丰富的细节，避免纯色且形状特点不鲜明的物体，例如：


1. 避免模糊，最好采用高清图片
