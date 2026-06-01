# Interface: IARTrackerRawData

> 官方文档：[Interface: IARTrackerRawData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IARTrackerRawData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IARTrackerRawData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IARTrackerRawData

`Face`/`Body`/`Hand`模式下，[ARTracker](../classes/ARTracker.md)存储的原始数据类型。

## Table of contents

### Properties

- [angle](IARTrackerRawData.md)
- [confidence](IARTrackerRawData.md)
- [gesture](IARTrackerRawData.md)
- [origin](IARTrackerRawData.md)
- [points](IARTrackerRawData.md)
- [points3d](IARTrackerRawData.md)
- [score](IARTrackerRawData.md)
- [size](IARTrackerRawData.md)

## Properties

### angle

• `Optional` **angle**: `Object`

在`Face`模式下，人脸旋转角度。

#### Type declaration

| Name | Type |
| --- | --- |
| `pitch` | `number` |
| `roll` | `number` |
| `yaw` | `number` |
| `z_score` | `number` |


### confidence

• **confidence**: `number`[]

关键点置信度。


### gesture

• `Optional` **gesture**: `number`

在`Hand`模式下，手势分类，正常`0~18`，无效为`-1`。


### origin

• **origin**: `Object`

原点，屏幕空间。

#### Type declaration

| Name | Type |
| --- | --- |
| `x` | `number` |
| `y` | `number` |


### points

• **points**: { `x`: `number` ; `y`: `number` }[]

关键点，屏幕空间。


### points3d

• **points3d**: { `x`: `number` ; `y`: `number` ; `z`: `number` }[]

支持3D时，3D关键点，世界空间。


### score

• **score**: `number`

置信度。


### size

• **size**: `Object`

尺寸，屏幕空间。

#### Type declaration

| Name | Type |
| --- | --- |
| `height` | `number` |
| `width` | `number` |
