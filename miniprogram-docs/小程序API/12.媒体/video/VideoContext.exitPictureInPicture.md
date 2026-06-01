# VideoContext.exitPictureInPicture(Object object)

> 官方文档：[VideoContext.exitPictureInPicture(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.exitPictureInPicture.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 视频 / VideoContext / VideoContext.exitPictureInPicture
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：支持

> 相关文档: [video 组件](https://developers.weixin.qq.com/miniprogram/dev/component/video.html)

## 功能描述

退出小窗，该方法可在任意页面调用

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |
