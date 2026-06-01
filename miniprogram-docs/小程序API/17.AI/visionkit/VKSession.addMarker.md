# number VKSession.addMarker(string path)

> 官方文档：[number VKSession.addMarker(string path)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.addMarker.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKSession / VKSession.addMarker
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.24.5 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.24.5](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

添加一个 marker，要求调 [wx.createVKSession](wx.createVKSession.md) 时传入的 track.marker 为 true

## 参数

### string path

图片路径，目前只支持本地用户图片

## 返回值

### number

marker id

## 使用提示

注意事项：

1. 使用 addMarker 接口之前，需要在 createVKSession 的时候声明开启 marker 跟踪。即 wx.createVKSession({ track: { marker: true } })
2. 可以添加多个 marker 图片，但不能重复添加相同的 marker 图片。
3. 在v2模式下同时支持水平面检测与marker检测，同时可输出多个2d/3d marker位姿（需要基础库版本不低于 [2.33.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

### 2Dmarker

对传入的图片有如下要求：

1. 格式：jpg/png 格式三通道彩图或者 1 通道灰度图
2. 分辨率：尺寸在 480x480 ~ 1920x1920 之间，建议为 1080 分辨率
3. 宽高比：在 1:1 ~ 16:9 之间，要求尽量方正，避免狭长的图片
4. 质量：目标图像为平面模型，需要占画面主体，避免大面积留白，建议用扫描件

示例：


建议：

1. 图片具有丰富的细节
2. 避免重复单一的纹理，例如：







1. 避免使用柔和平滑边缘的纹理及大量渐变图像，例如：


1. 避免模糊，建议采用高清、高对比度图像作为识别对象
2. 建议图像有均匀的特征（角点）分布，正确示例：


避免角点较少、中间大量空白、没有特征及角点的图像，错误示例：


### 3Dmarker

现小程序demo支持通过上传视频, 生成对应模型的3dmarker识别文件,后缀名为.map

对传入的视频有如下要求：
1.视频长宽比为16:9或4:3; 短边大于480px
2.目标物体易于和背景物体区分出来，同时目标物体放置与背景物体一定距离，放置底面与物体易于区分，底面可以放置一张白纸，例如：


3.目标物体最好为刚体，本身不会发生较大形变， 容易变形的物体不适合用作识别对象
4.视频匀速移动，避免模糊，对目标识别面环绕物体拍摄，需要保证相机有足够的平移移动
5.marker物体要求与2d图像要求类似，具有丰富细节，避免重复单一纹理，不反光，无高光
6.拍摄视频中特征纹理丰富，如果marker本身问题较弱，可以在背景中适当添加纹理物体
服务耗时：当前版本30s视频耗时约20分钟，请静待算法返回模型

建议：

1.视频格式：视频帧率30fps，分辨率建议1080p
2.视频时长：视频建议时长在20s~30s，超过30s会被截断，时长过短会导致marker效果欠佳
