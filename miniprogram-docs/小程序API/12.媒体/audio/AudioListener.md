# AudioListener

> 官方文档：[AudioListener](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioListener.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / AudioListener
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

空间音频监听器，代表在一个音频场景内唯一的位置和方向信息。

## 属性

### number positionX

右手笛卡尔坐标系中X轴的位置。

### number positionY

右手笛卡尔坐标系中Y轴的位置。

### number positionZ

右手笛卡尔坐标系中Z轴的位置。

### number forwardX

表示监听器的前向系统在同一笛卡尔坐标系中的水平位置，作为位置（位置x，位置和位置和位置）值。

### number forwardY

表示听众的前向方向在同一笛卡尔坐标系中作为位置（位置x，位置和位置和位置）值的垂直位置。

### number forwardZ

表示与position (positionX、positionY和positionZ)值在同一笛卡尔坐标系下的听者前进方向的纵向(前后)位置。

### number upX

表示在与position (positionX、positionY和positionZ)值相同的笛卡尔坐标系中侦听器向前方向的水平位置。

### number upY

表示在与position (positionX、positionY和positionZ)值相同的笛卡尔坐标系中侦听器向上方向的水平位置。

### number upZ

表示在与position (positionX、positionY和positionZ)值相同的笛卡尔坐标系中侦听器向后方向的水平位置。

### function setOrientation

设置监听器的方向

### function setPosition

设置监听器的位置
