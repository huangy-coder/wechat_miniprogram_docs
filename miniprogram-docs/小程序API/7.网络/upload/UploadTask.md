# UploadTask

> 官方文档：[UploadTask](https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/UploadTask.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / 上传 / UploadTask
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.4.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)、[局域网通信](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/mDNS.html)

一个可以监听上传进度变化事件，以及取消上传任务的对象

## 方法

### UploadTask.abort()

中断上传任务

### UploadTask.onProgressUpdate(function listener)

监听上传进度变化事件

### UploadTask.offProgressUpdate(function listener)

移除上传进度变化事件的监听函数

### UploadTask.onHeadersReceived(function listener)

监听 HTTP Response Header 事件。会比请求完成事件更早

### UploadTask.offHeadersReceived(function listener)

移除 HTTP Response Header 事件的监听函数

## 示例代码

```js
const uploadTask = wx.uploadFile({
  url: 'http://example.weixin.qq.com/upload', //仅为示例，非真实的接口地址
  filePath: tempFilePaths[0],
  name: 'file',
  formData:{
    'user': 'test'
  },
  success (res){
    const data = res.data
    //do something
  }
})

uploadTask.onProgressUpdate((res) => {
  console.log('上传进度', res.progress)
  console.log('已经上传的数据长度', res.totalBytesSent)
  console.log('预期需要上传的数据总长度', res.totalBytesExpectedToSend)
})

uploadTask.abort() // 取消上传任务
```
