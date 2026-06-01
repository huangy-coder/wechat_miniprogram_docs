# wx.compressImage(Object object)

> 官方文档：[wx.compressImage(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.compressImage.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 图片 / wx.compressImage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.4.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [2.12.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 鸿蒙 OS 版**：支持

## 功能描述

压缩图片接口，可选压缩质量。iOS 仅支持压缩 JPG 格式图片。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| src | string |   | 是 | 图片路径，图片的路径，支持本地路径、代码包路径 |   |
| quality | number | 80 | 否 | 压缩质量，范围0～100，数值越小，质量越低，压缩率越高（仅对jpg有效）。 |   |
| compressedWidth | number |   | 否 | 压缩后图片的宽度，单位为px，若不填写则默认以compressedHeight为准等比缩放。 | [2.26.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| compressedHeight | number |   | 否 | 压缩后图片的高度，单位为px，若不填写则默认以compressedWidth为准等比缩放 | [2.26.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | string | 压缩后图片的临时文件路径 (本地路径) |

## 示例代码

```js
wx.compressImage({
  src: '', // 图片路径
  quality: 80 // 压缩质量
})
```
