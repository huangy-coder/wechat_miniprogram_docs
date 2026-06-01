# CameraContext

> 官方文档：[CameraContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraContext.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 相机 / CameraContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [camera 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/camera.html)

CameraContext 实例，可通过 [wx.createCameraContext](wx.createCameraContext.md) 获取。

[CameraContext](CameraContext.md) 与页面内唯一的 [camera](https://developers.weixin.qq.com/miniprogram/dev/component/camera.html) 组件绑定，操作对应的 [camera](https://developers.weixin.qq.com/miniprogram/dev/component/camera.html) 组件。

## 方法

### CameraFrameListener CameraContext.onCameraFrame(onCameraFrameCallback callback)

获取 Camera 实时帧数据

### CameraContext.takePhoto(Object object)

拍摄照片

### CameraContext.setZoom(Object object)

设置缩放级别

### CameraContext.startRecord(Object object)

开始录像

### CameraContext.stopRecord(Object object)

结束录像

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/VBZ3Jim26zYu)
