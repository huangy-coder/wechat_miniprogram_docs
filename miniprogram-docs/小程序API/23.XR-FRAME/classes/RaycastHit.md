# Class: RaycastHit

> 官方文档：[Class: RaycastHit](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/RaycastHit.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / RaycastHit
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / RaycastHit

## Table of contents

### Constructors

- [constructor](RaycastHit.md)

### Accessors

- [distance](RaycastHit.md)
- [normal](RaycastHit.md)
- [point](RaycastHit.md)
- [shape](RaycastHit.md)

## Constructors

### constructor

• **new RaycastHit**(`scene`, `nativeComp?`)

#### Parameters

| Name | Type |
| --- | --- |
| `scene` | [`Scene`](Scene.md) |
| `nativeComp?` | `RaycastHit` |

## Accessors

### distance

• `get` **distance**(): `number`

从射线的原点到碰撞点的距离。

#### Returns

`number`

• `set` **distance**(`v`): `void`

从射线的原点到碰撞点的距离。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `number` |

#### Returns

`void`


### normal

• `get` **normal**(): [`Vector3`](Vector3.md)

射线与轮廓的交点表面的法线。

#### Returns

[`Vector3`](Vector3.md)

• `set` **normal**(`v`): `void`

射线与轮廓的交点表面的法线。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](Vector3.md) |

#### Returns

`void`


### point

• `get` **point**(): [`Vector3`](Vector3.md)

在世界空间中，射线与轮廓的交点。

#### Returns

[`Vector3`](Vector3.md)

• `set` **point**(`v`): `void`

在世界空间中，射线与轮廓的交点。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](Vector3.md) |

#### Returns

`void`


### shape

• `get` **shape**(): [`Shape`](Shape.md)<`any`>

与射线相交的Shape。

#### Returns

[`Shape`](Shape.md)<`any`>
