# wx.removeStorage(Object object)

> 官方文档：[wx.removeStorage(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.removeStorage.html)
> 所属分类：[数据缓存](数据缓存目录.md)
> 导航路径：数据缓存 / wx.removeStorage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [存储策略](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/storage.html)

## 功能描述

从本地缓存中移除指定 key。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | string |   | 是 | 本地缓存中指定的 key |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

## 示例代码

```js
wx.removeStorage({
  key: 'key',
  success (res) {
    console.log(res)
  }
})
```

```js
try {
  wx.removeStorageSync('key')
} catch (e) {
  // Do something when catch error
}
```
