# wx.shareVideoToGroup(Object object)

> 官方文档：[wx.shareVideoToGroup(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.shareVideoToGroup.html)
> 所属分类：[聊天工具](聊天工具目录.md)
> 导航路径：聊天工具 / wx.shareVideoToGroup
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.7.8 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：不支持

> 相关文档: [聊天工具模式](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/chatTool.html)

## 功能描述

转发视频到聊天

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| videoPath | string |   | 是 | 要分享的视频地址，必须为本地路径或临时路径 |
| thumbPath | string |   | 否 | 缩略图路径，若留空则使用视频首帧 |
| needShowEntrance | boolean | true | 否 | 分享的图片消息是否要带小程序入口 |
| entrancePath | string | '' | 否 | 从消息小程序入口打开小程序的路径，默认为聊天工具启动路径 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

## 示例代码

```javascript
  // callback 写法
  wx.downloadFile({
    url: URL, // 下载url
    success (res) {
      // 下载完成后转发
      wx.shareVideoToGroup({
        videoPath: res.tempFilePath,
        success() {},
        fail: console.error,
      })
    },
    fail: console.error,
  })
```
