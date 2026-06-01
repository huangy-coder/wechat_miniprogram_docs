# any wx.getStorageSync(string key)

> 官方文档：[any wx.getStorageSync(string key)](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.getStorageSync.html)
> 所属分类：[数据缓存](数据缓存目录.md)
> 导航路径：数据缓存 / wx.getStorageSync
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [存储策略](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/storage.html)

## 功能描述

从本地缓存中同步获取指定 key 的内容。

## 参数

### string key

本地缓存中指定的 key

## 返回值

### any

key对应的内容

## 注意

storage 应只用来进行数据的持久化存储，不应用于运行时的数据传递或全局状态管理。启动过程中过多的同步读写存储，会显著影响启动耗时。

## 示例代码

```js
try {
  var value = wx.getStorageSync('key')
  if (value) {
    // Do something with return value
  }
} catch (e) {
  // Do something when catch error
}
```
