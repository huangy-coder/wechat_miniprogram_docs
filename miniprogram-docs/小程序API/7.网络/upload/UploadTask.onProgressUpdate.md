# UploadTask.onProgressUpdate(function listener)

> 官方文档：[UploadTask.onProgressUpdate(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/UploadTask.onProgressUpdate.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / 上传 / UploadTask / UploadTask.onProgressUpdate
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.4.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)、[局域网通信](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/mDNS.html)

## 功能描述

监听上传进度变化事件

## 参数

### function listener

上传进度变化事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| progress | number | 上传进度百分比 |
| totalBytesSent | number | 已经上传的数据长度，单位 Bytes |
| totalBytesExpectedToSend | number | 预期需要上传的数据总长度，单位 Bytes |
