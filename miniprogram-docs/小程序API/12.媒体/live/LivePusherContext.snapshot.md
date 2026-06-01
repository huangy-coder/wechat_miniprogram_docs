# LivePusherContext.snapshot(Object object)

> 官方文档：[LivePusherContext.snapshot(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.snapshot.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 实时音视频 / LivePusherContext / LivePusherContext.snapshot
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：支持

> 相关文档: [live-pusher 组件](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)

## 功能描述

快照

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| quality | string | raw | 否 | 图片的质量 | [2.10.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| sourceType | string | stream | 否 | 截取的源类型 | [2.25.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

补充表：
| 合法值 | 说明 |
| --- | --- |
| raw | 原图 |
| compressed | 压缩图 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| stream | 截取视频源 |
| view | 截取渲染后的画面 |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempImagePath | string | 图片文件的临时路径 |
| width | string | 图片的宽度 |
| height | string | 图片的高度 |
