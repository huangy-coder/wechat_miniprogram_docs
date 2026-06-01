# PreDownloadSubpackageTask.onProgressUpdate(function listener)

> 官方文档：[PreDownloadSubpackageTask.onProgressUpdate(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/base/subpackage/PreDownloadSubpackageTask.onProgressUpdate.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 分包加载 / PreDownloadSubpackageTask / PreDownloadSubpackageTask.onProgressUpdate
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.27.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

监听分包加载进度变化事件

## 参数

### function listener

分包加载进度变化事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| progress | number | 分包下载进度百分比 |
| totalBytesWritten | number | 已经下载的数据长度，单位 Bytes |
| totalBytesExpectedToWrite | number | 预期需要下载的数据总长度，单位 Bytes |
