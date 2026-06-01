# wx.previewImage(Object object)

> 官方文档：[wx.previewImage(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.previewImage.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 图片 / wx.previewImage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

在新页面中全屏预览图片。预览的过程中用户可以进行保存图片、发送给朋友等操作。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| urls | Array.<string> |   | 是 | 需要预览的图片链接列表。[2.2.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 起支持云文件ID。 |   |
| showmenu | boolean | true | 否 | 是否显示长按菜单。 | [2.13.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| current | string | urls 的第一张 | 否 | 当前显示图片的链接 |   |
| referrerPolicy | string | no-referrer | 否 | `origin`: 发送完整的referrer; `no-referrer`: 不发送。格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 {appid} 为小程序的 appid，{version} 为小程序的版本号，版本号为 0 表示为开发版、体验版以及审核版本，版本号为 devtools 表示为开发者工具，其余为正式版本； | [2.13.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

## 支持长按识别的码

| 类型 | 说明 | 最低版本 |
| --- | --- | --- |
| 小程序码 |   |   |
| 微信个人码 |   | [2.18.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| 企业微信个人码 |   | [2.18.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| 普通群码 | 指仅包含微信用户的群 | [2.18.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| 互通群码 | 指既有微信用户也有企业微信用户的群 | [2.18.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| 公众号二维码 |   | [2.18.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 示例代码

```js
wx.previewImage({
  current: '', // 当前显示图片的http链接
  urls: [] // 需要预览的图片http链接列表
})
```
