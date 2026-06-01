# wx.authorizeForMiniProgram(Object object)

> 官方文档：[wx.authorizeForMiniProgram(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/authorize/wx.authorizeForMiniProgram.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 授权 / wx.authorizeForMiniProgram
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.14.4 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [2.14.4](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [授权](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/authorize.html)

## 功能描述

**仅小程序插件中能调用该接口**，用法同 [wx.authorize](wx.authorize.md)。目前仅支持三种 scope（见下）

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| scope | string |   | 是 | 需要获取权限的 scope，详见 [scope 列表](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/authorize.html#scope-列表) |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

补充表：
| 合法值 | 说明 |
| --- | --- |
| scope.record |   |
| scope.writePhotosAlbum |   |
| scope.camera |   |

## 示例代码

```js
wx.authorizeForMiniProgram({
  scope: 'scope.record',
  success () {
    // 用户已经同意小程序使用录音功能，后续调用 wx.startRecord 接口不会弹窗询问
    wx.startRecord()
  }
})
```
