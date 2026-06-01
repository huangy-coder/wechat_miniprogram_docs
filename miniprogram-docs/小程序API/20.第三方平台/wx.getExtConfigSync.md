# Object wx.getExtConfigSync()

> 官方文档：[Object wx.getExtConfigSync()](https://developers.weixin.qq.com/miniprogram/dev/api/ext/wx.getExtConfigSync.html)
> 所属分类：[第三方平台](第三方平台目录.md)
> 导航路径：第三方平台 / wx.getExtConfigSync
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.1.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

[wx.getExtConfig](wx.getExtConfig.md) 的同步版本。

## 返回值

### Object

第三方平台自定义的数据

## Tips

1. 本接口暂时无法通过 [wx.canIUse](../1.基础/wx.canIUse.md) 判断是否兼容，开发者需要自行判断 [wx.getExtConfigSync](wx.getExtConfigSync.md) 是否存在来兼容

```js
let extConfig = wx.getExtConfigSync? wx.getExtConfigSync(): {}
console.log(extConfig)
```
