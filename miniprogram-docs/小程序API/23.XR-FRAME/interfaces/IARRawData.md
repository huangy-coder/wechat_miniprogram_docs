# Interface: IARRawData

> 官方文档：[Interface: IARRawData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IARRawData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IARRawData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IARRawData

AR追踪原始数据。

## Table of contents

### Properties

- [height](IARRawData.md)
- [intrinsics](IARRawData.md)
- [timestamp](IARRawData.md)
- [uvBuffer](IARRawData.md)
- [viewMatrix](IARRawData.md)
- [width](IARRawData.md)
- [yBuffer](IARRawData.md)

## Properties

### height

• **height**: `number`

当前相机帧画面高度。


### intrinsics

• **intrinsics**: `Float32Array`

当前相机帧内参矩阵。


### timestamp

• **timestamp**: `number`

该帧生成时间，单位是纳秒(ns)。
在版本`v2.30.1`之后支持。


### uvBuffer

• **uvBuffer**: `ArrayBuffer`

当前相机帧画面`uv`通道，yuv420。


### viewMatrix

• **viewMatrix**: `Float32Array`

当前相机帧视图矩阵。


### width

• **width**: `number`

当前相机帧画面宽度。


### yBuffer

• **yBuffer**: `ArrayBuffer`

当前相机帧画面`y`通道，yuv420。
