# Array.<any> wx.batchGetStorageSync(Array.<string> keyList)

> 官方文档：[Array.<any> wx.batchGetStorageSync(Array.<string> keyList)](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.batchGetStorageSync.html)
> 所属分类：[数据缓存](数据缓存目录.md)
> 导航路径：数据缓存 / wx.batchGetStorageSync
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.25.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [存储策略](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/storage.html)

## 功能描述

从本地缓存中同步批量获取指定 key 的内容。

## 参数

### Array.<string> keyList

本地缓存中指定的 key 数组

## 返回值

### Array.<any>

key对应的内容

## 示例代码

```js
try {
  var valueList = wx.batchGetStorageSync(['key'])
  if (valueList) {
    // Do something with return value
  }
} catch (e) {
  // Do something when catch error
}
```

对于多个key的读取, 批量读取在性能上优于多次getStorageSync读取
