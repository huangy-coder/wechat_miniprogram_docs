# wx.subscribeVoIPVideoMembers(Object object)

> 官方文档：[wx.subscribeVoIPVideoMembers(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.subscribeVoIPVideoMembers.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 实时语音 / wx.subscribeVoIPVideoMembers
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [2.11.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [多人音视频对话](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/voip-chat.html)

## 功能描述

订阅视频画面成员。对于视频房间，当成员超过两人时需进行订阅，否则只能看到最先加入房间的两人画面。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| openIdList | Array.<String> |   | 是 | 订阅的成员列表 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |
