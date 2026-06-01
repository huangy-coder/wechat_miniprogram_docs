# CameraFrameListener CameraContext.onCameraFrame(function callback)

> 官方文档：[CameraFrameListener CameraContext.onCameraFrame(function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraContext.onCameraFrame.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 相机 / CameraContext / CameraContext.onCameraFrame
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

> 相关文档: [camera 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/camera.html)

## 功能描述

获取 Camera 实时帧数据

## 参数

### function callback

回调函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 图像数据矩形的宽度 |
| height | number | 图像数据矩形的高度 |
| data | ArrayBuffer | 图像像素点数据，一维数组，每四项表示一个像素点的 rgba |

## 返回值

### CameraFrameListener

注： 使用该接口需同时在 [camera](https://developers.weixin.qq.com/miniprogram/dev/component/camera.html) 组件属性中指定 frame-size。

## 示例代码

```js
const context = wx.createCameraContext()
const listener = context.onCameraFrame((frame) => {
  console.log(frame.data instanceof ArrayBuffer, frame.width, frame.height)
})
listener.start()
```
