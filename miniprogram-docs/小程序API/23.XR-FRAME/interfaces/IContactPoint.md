# Interface: IContactPoint

> 官方文档：[Interface: IContactPoint](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IContactPoint.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IContactPoint
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IContactPoint

物理事件返回的[碰撞信息](ICollideEvent.md)中的碰撞点。

## Table of contents

### Properties

- [normal](IContactPoint.md)
- [otherShape](IContactPoint.md)
- [point](IContactPoint.md)
- [separation](IContactPoint.md)
- [thisShape](IContactPoint.md)

## Properties

### normal

• `Readonly` **normal**: `Vector3_READONLY`

碰撞平面的法线。


### otherShape

• `Readonly` **otherShape**: [`Shape`](../classes/Shape.md)<`any`>

另一个轮廓。


### point

• `Readonly` **point**: `Vector3_READONLY`

碰撞点的位置。


### separation

• `Readonly` **separation**: `number`

在该碰撞点处，两个物体的距离。

不一定是0或小于0，因为只要两个物体的距离小于{@link Collider.contactOffset}之和，就会判定为碰撞。


### thisShape

• `Readonly` **thisShape**: [`Shape`](../classes/Shape.md)<`any`>

接收碰撞事件的轮廓。
