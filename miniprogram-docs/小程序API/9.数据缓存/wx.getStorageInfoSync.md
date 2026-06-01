# Object wx.getStorageInfoSync()

> 官方文档：[Object wx.getStorageInfoSync()](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.getStorageInfoSync.html)
> 所属分类：[数据缓存](数据缓存目录.md)
> 导航路径：数据缓存 / wx.getStorageInfoSync
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [存储策略](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/storage.html)

## 功能描述

[wx.getStorageInfo](wx.getStorageInfo.md) 的同步版本

## 返回值

### Object object

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| keys | Array.<string> | 当前 storage 中所有的 key |
| currentSize | number | 当前占用的空间大小, 单位 KB |
| limitSize | number | 限制的空间大小，单位 KB |

## 示例代码

```js
wx.getStorageInfo({
  success (res) {
    console.log(res.keys)
    console.log(res.currentSize)
    console.log(res.limitSize)
  }
})
```

```js
try {
  const res = wx.getStorageInfoSync()
  console.log(res.keys)
  console.log(res.currentSize)
  console.log(res.limitSize)
} catch (e) {
  // Do something when catch error
}
```
