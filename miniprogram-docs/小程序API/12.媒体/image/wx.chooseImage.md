# wx.chooseImage(Object object)

> 官方文档：[wx.chooseImage(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.chooseImage.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 图片 / wx.chooseImage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

从基础库 [2.21.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [wx.chooseMedia](../video/wx.chooseMedia.md) 代替

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

从本地相册选择图片或使用相机拍照。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| count | number | 9 | 否 | 最多可以选择的图片张数 |
| sizeType | Array.<string> | ['original', 'compressed'] | 否 | 所选的图片的尺寸 |
| sourceType | Array.<string> | ['album', 'camera'] | 否 | 选择图片的来源 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

补充表：
| 合法值 | 说明 |
| --- | --- |
| original | 原图 |
| compressed | 压缩图 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| album | 从相册选图 |
| camera | 使用相机 |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| tempFilePaths | Array.<string> | 图片的本地临时文件路径列表 (本地路径) |   |
| tempFiles | Array.<Object> | 图片的本地临时文件列表 | [1.2.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

补充表：
| 结构属性 | 类型 | 说明 |
| --- | --- | --- |
| path | string | 本地临时文件路径 (本地路径) |
| size | number | 本地临时文件大小，单位 B |

```js
wx.chooseImage({
  count: 1,
  sizeType: ['original', 'compressed'],
  sourceType: ['album', 'camera'],
  success (res) {
    // tempFilePath可以作为img标签的src属性显示图片
    const tempFilePaths = res.tempFilePaths
  }
})
```
