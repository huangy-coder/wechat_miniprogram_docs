# Object wx.getAccountInfoSync()

> 官方文档：[Object wx.getAccountInfoSync()](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/account-info/wx.getAccountInfoSync.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 账号信息 / wx.getAccountInfoSync
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.2.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.2.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

获取当前账号信息。线上小程序版本号仅支持在正式版小程序中获取，开发版和体验版中无法获取。

## 返回值

### Object

账号信息

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| miniProgram | Object | 小程序账号信息 |
| plugin | Object | 插件账号信息（仅在插件中调用时包含这一项） |

补充表：
| 结构属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| appId | string | 小程序 appId |   |
| envVersion | string | 小程序版本 | [2.10.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| version | string | 线上小程序版本号 | [2.10.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

补充表：
| 合法值 | 说明 |
| --- | --- |
| develop | 开发版，提交代码审核时默认使用开发版进行审核。 |
| trial | 体验版 |
| release | 正式版 |

补充表：
| 结构属性 | 类型 | 说明 |
| --- | --- | --- |
| appId | string | 插件 appId |
| version | string | 插件版本号 |

## 示例代码

```js
const accountInfo = wx.getAccountInfoSync();
console.log(accountInfo.miniProgram.appId) // 小程序 appId
console.log(accountInfo.plugin.appId) // 插件 appId
console.log(accountInfo.plugin.version) // 插件版本号， 'a.b.c' 这样的形式
```
