# Interface: ICollideEvent

> 官方文档：[Interface: ICollideEvent](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ICollideEvent.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / ICollideEvent
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / ICollideEvent

物理碰撞事件（collide-begin等）的信息。

**`readonly`**

## Table of contents

### Properties

- [contacts](ICollideEvent.md)
- [impulse](ICollideEvent.md)
- [relativeVelocity](ICollideEvent.md)
- [shape](ICollideEvent.md)

## Properties

### contacts

• `Readonly` **contacts**: [`IContactPoint`](IContactPoint.md)[]

本次碰撞的接触点。


### impulse

• `Readonly` **impulse**: `Vector3_READONLY`

从碰撞到分离所用的冲量之和。


### relativeVelocity

• `Readonly` **relativeVelocity**: `Vector3_READONLY`

两个刚体的相对线性碰撞速度。


### shape

• `Readonly` **shape**: [`Shape`](../classes/Shape.md)<`any`>

发生碰撞的另一个轮廓。
