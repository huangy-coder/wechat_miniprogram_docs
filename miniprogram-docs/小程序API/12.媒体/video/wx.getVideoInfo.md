# wx.getVideoInfo(Object object)

> 官方文档：[wx.getVideoInfo(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.getVideoInfo.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 视频 / wx.getVideoInfo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **小程序插件**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

获取视频详细信息。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| src | string |   | 是 | 视频文件路径，可以是临时文件路径也可以是永久文件路径 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| orientation | string | 画面方向 |
| type | string | 视频格式 |
| duration | number | 视频长度 |
| size | number | 视频大小，单位 kB |
| height | number | 视频的长，单位 px |
| width | number | 视频的宽，单位 px |
| fps | number | 视频帧率 |
| bitrate | number | 视频码率，单位 kbps |

补充表：
| 合法值 | 说明 |
| --- | --- |
| up | 默认 |
| down | 180度旋转 |
| left | 逆时针旋转90度 |
| right | 顺时针旋转90度 |
| up-mirrored | 同up，但水平翻转 |
| down-mirrored | 同down，但水平翻转 |
| left-mirrored | 同left，但垂直翻转 |
| right-mirrored | 同right，但垂直翻转 |
