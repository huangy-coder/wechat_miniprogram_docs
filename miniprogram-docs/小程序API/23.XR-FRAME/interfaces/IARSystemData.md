# Interface: IARSystemData

> 官方文档：[Interface: IARSystemData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IARSystemData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IARSystemData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IARSystemData

`ARSystem`系统数据接口。

## Table of contents

### Properties

- [camera](IARSystemData.md)
- [depthDebug](IARSystemData.md)
- [depthFar](IARSystemData.md)
- [depthMask](IARSystemData.md)
- [depthNear](IARSystemData.md)
- [modes](IARSystemData.md)
- [planeMode](IARSystemData.md)
- [pose3d](IARSystemData.md)

## Properties

### camera

• `Optional` **camera**: `"Front"` | `"Back"`

使用前置还是后置相机，默认后置`Back`。


### depthDebug

• `Optional` **depthDebug**: `boolean`

开启实时深度遮挡时，显示一个用于Debug的图层。
**目前暂时不可用！**


### depthFar

• `Optional` **depthFar**: `number`

开启实时深度遮挡时，遮挡的远处阈值。
值是空间实际尺度（m），默认为`20`。


### depthMask

• `Optional` **depthMask**: `boolean`

在支持的情况下，是否开启实时深度遮挡。
**目前暂时不可用！**


### depthNear

• `Optional` **depthNear**: `number`

开启实时深度遮挡时，遮挡的近处阈值。
值是空间实际尺度（m），默认为`0.02`。


### modes

• **modes**: [`TTrackMode`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TTrackMode)[]

系统支持的追踪模式，目前仅支持一个！
`xml`中数据类型为`array`，默认值为`Plane`。


### planeMode

• `Optional` **planeMode**: `number`

在`v2`平面模式下，平面检测模式。
`1`为水平面，`2`为垂直平面，`3`为两个都支持。
默认为`3`。


### pose3d

• `Optional` **pose3d**: `boolean`

在`Face`/`Body`/`Hand`模式下，使用原生的AI3D推理估计。
默认为`false`。
**目前暂时不可用！**
