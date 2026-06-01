# Interface: IShapeInteractData

> 官方文档：[Interface: IShapeInteractData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IShapeInteractData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IShapeInteractData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IShapeInteractData

## Table of contents

### Properties

- [bounciness](IShapeInteractData.md)
- [collide](IShapeInteractData.md)
- [disabled](IShapeInteractData.md)
- [dynamicFriction](IShapeInteractData.md)
- [staticFriction](IShapeInteractData.md)

## Properties

### bounciness

• `Optional` **bounciness**: `number`

弹性系数，决定碰撞时的能量损失比例。

弹性系数 = 1时，碰撞无能量损失。

**`limit`** 0 <= bounciness <= 1

**`default`** 0


### collide

• `Optional` **collide**: `boolean`

是否能与其他Shape发生物理碰撞。

**`default`** false


### disabled

• `Optional` **disabled**: `boolean`

是否禁用Shape间交互。

**`default`** false


### dynamicFriction

• `Optional` **dynamicFriction**: `number`

动摩擦系数。

**`limit`** 0 <= dynamicFriction <= 1

**`default`** 0.6


### staticFriction

• `Optional` **staticFriction**: `number`

静摩擦系数

**`limit`** 0 <= staticFriction <= 1

**`default`** 0.6
