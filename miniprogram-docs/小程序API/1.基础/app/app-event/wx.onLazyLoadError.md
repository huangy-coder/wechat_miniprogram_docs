# wx.onLazyLoadError(function listener)

> 官方文档：[wx.onLazyLoadError(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onLazyLoadError.html)
> 所属分类：[基础](../../基础目录.md)
> 导航路径：基础 / 小程序 / 应用级事件 / wx.onLazyLoadError
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.24.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [分包异步化](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/async.html)

## 功能描述

监听小程序异步组件加载失败事件。

## 参数

### function listener

小程序异步组件加载失败事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| type | string | 'subpackage' 失败类型 |
| subpackage | Array | 异步组件所属的分包 |
| errMsg | string | 详细信息 |

## 注意

- 加载异步组件通常需要下载分包，若分包下载超时，则会触发 errMsg 为 "loadSubpackage: timeout" 的回调，默认超时等待时间为 10 秒。
- 可以通过第二个参数指定超时时间（单位：ms），该设置全局有效，多次指定超时时间则覆盖前面。
- 分包确认下载失败时，会再次触发 errMsg 为 "loadSubpackage: fail" 的回调。
- 若在页面中使用该接口进行监听，请确保在必要时手动调用 offLazyLoadError 取消监听，以避免非预期的内存泄漏。
