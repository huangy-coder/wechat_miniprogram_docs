# PreDownloadSubpackageTask wx.preDownloadSubpackage(Object object)

> 官方文档：[PreDownloadSubpackageTask wx.preDownloadSubpackage(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/base/subpackage/wx.preDownloadSubpackage.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 分包加载 / wx.preDownloadSubpackage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.27.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

触发分包预下载。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| packageType | string |   | 是 | 分包的类型。目前仅支持填 "workers"，表示 workers 分包。 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

## 返回值

### PreDownloadSubpackageTask

预下载分包任务实例，用于获取分包预下载状态

## 注意事项

- wx.preDownloadSubpackage 目前只开放了下载 worker 分包的能力，还不支持下载普通类型的分包。

## 示例代码

```js
// 首先要在 app.json / game.json 中配置workers作为分包
{
  "workers": {
    "path": "myWorkersFolder",
    "isSubpackage": true  // true 表示把 worker 打包为分包。默认 false。填 false 时等同于 { "workers": "myWorkersFolder" }
  }
}
```

```js
// 然后调用 wx.preDownloadSubpackage 下载 worker 分包，下载成功后才可以创建 worker
var task = wx.preDownloadSubpackage({
  packageType: "workers",
  success(res) {
    console.log("load worker success", res)
    wx.createWorker("myWorkersFolder/request/index.js")   // 创建 worker。 如果 worker 分包没下载完就调 createWorker 的话将报错
  },
  fail(res) {
    console.log("load worker fail", res)
  }
})

task.onProgressUpdate(res => {
  console.log(res.progress) // 可通过 onProgressUpdate 接口监听下载进度
  console.log(res.totalBytesWritten)
  console.log(res.totalBytesExpectedToWrite)
})
```
