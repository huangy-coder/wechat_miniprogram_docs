# wx.addVideoToFavorites(Object object)

> 官方文档：[wx.addVideoToFavorites(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/favorites/wx.addVideoToFavorites.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 收藏 / wx.addVideoToFavorites
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.16.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

收藏视频

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| videoPath | string |   | 是 | 要收藏的视频地址，必须为本地路径或临时路径 |
| thumbPath | string |   | 否 | 缩略图路径，若留空则使用视频首帧 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

## 示例代码

```javascript
  // callback 写法
  wx.downloadFile({
    url: URL, // 下载url
    success (res) {
      // 下载完成后收藏
      wx.addVideoToFavorites({
        videoPath: res.tempFilePath,
        success() {},
        fail: console.error,
      })
    },
    fail: console.error,
  })

  // async await 写法
  const { tempFilePath } = await wx.downloadFile({
    url: URL, // 下载url
  })
  // 下载完成后收藏
  await wx.addVideoToFavorites({
    videoPath: res.tempFilePath,
  })
```
