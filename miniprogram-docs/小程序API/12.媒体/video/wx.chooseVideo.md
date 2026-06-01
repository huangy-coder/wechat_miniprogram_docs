# wx.chooseVideo(Object object)

> 官方文档：[wx.chooseVideo(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.chooseVideo.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 视频 / wx.chooseVideo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

从基础库 [2.21.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [wx.chooseMedia](wx.chooseMedia.md) 代替

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

拍摄视频或从手机相册中选视频。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| sourceType | Array.<string> | ['album', 'camera'] | 否 | 视频选择的来源 |   |
| compressed | boolean | true | 否 | 是否压缩所选择的视频文件 | [1.6.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| maxDuration | number | 60 | 否 | 拍摄视频最长拍摄时间，单位秒 |   |
| camera | string | 'back' | 否 | 默认拉起的是前置或者后置摄像头。部分 Android 手机下由于系统 ROM 不支持无法生效 |   |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

补充表：
| 合法值 | 说明 |
| --- | --- |
| album | 从相册选择视频 |
| camera | 使用相机拍摄视频 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| back | 默认拉起后置摄像头 |
| front | 默认拉起前置摄像头 |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | string | 选定视频的临时文件路径 (本地路径) |
| duration | number | 选定视频的时间长度 |
| size | number | 选定视频的数据量大小 |
| height | number | 返回选定视频的高度 |
| width | number | 返回选定视频的宽度 |

## 示例代码

```js
wx.chooseVideo({
  sourceType: ['album','camera'],
  maxDuration: 60,
  camera: 'back',
  success(res) {
    console.log(res.tempFilePath)
  }
})
```
