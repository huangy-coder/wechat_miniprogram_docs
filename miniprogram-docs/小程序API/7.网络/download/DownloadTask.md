# DownloadTask

> 官方文档：[DownloadTask](https://developers.weixin.qq.com/miniprogram/dev/api/network/download/DownloadTask.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / 下载 / DownloadTask
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.4.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)、[局域网通信](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/mDNS.html)

一个可以监听下载进度变化事件，以及取消下载任务的对象

## 方法

### DownloadTask.abort()

中断下载任务

### DownloadTask.onProgressUpdate(function listener)

监听下载进度变化事件

### DownloadTask.offProgressUpdate(function listener)

移除下载进度变化事件的监听函数

### DownloadTask.onHeadersReceived(function listener)

监听 HTTP Response Header 事件。会比请求完成事件更早

### DownloadTask.offHeadersReceived(function listener)

移除 HTTP Response Header 事件的监听函数

## 示例代码

```js
const downloadTask = wx.downloadFile({
  url: 'http://example.com/audio/123', //仅为示例，并非真实的资源
  success (res) {
    wx.playVoice({
      filePath: res.tempFilePath
    })
  }
})

downloadTask.onProgressUpdate((res) => {
  console.log('下载进度', res.progress)
  console.log('已经下载的数据长度', res.totalBytesWritten)
  console.log('预期需要下载的数据总长度', res.totalBytesExpectedToWrite)
})

downloadTask.abort() // 取消下载任务
```
