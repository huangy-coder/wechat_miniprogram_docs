# Class: Spherical

> 官方文档：[Class: Spherical](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Spherical.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Spherical
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Spherical

球面坐标系。

## Table of contents

### Constructors

- [constructor](Spherical.md)

### Properties

- [center](Spherical.md)
- [isSpherical](Spherical.md)
- [phi](Spherical.md)
- [radius](Spherical.md)
- [theta](Spherical.md)
- [EPS](Spherical.md)

### Methods

- [clone](Spherical.md)
- [copy](Spherical.md)
- [makeSafe](Spherical.md)
- [set](Spherical.md)
- [setFromCartesianCoords](Spherical.md)
- [setFromVector3](Spherical.md)
- [toVector3](Spherical.md)

## Constructors

### constructor

• **new Spherical**(`radius?`, `phi?`, `theta?`)

#### Parameters

| Name | Type |
| --- | --- |
| `radius?` | `number` |
| `phi?` | `number` |
| `theta?` | `number` |

## Properties

### center

• **center**: [`Vector3`](Vector3.md)

球面球心。


### isSpherical

• **isSpherical**: `boolean` = `true`


### phi

• **phi**: `number`

点在球面上的横向旋转角度。


### radius

• **radius**: `number`

球面半径。


### theta

• **theta**: `number`

点在球面上的纵向旋转角度。


### EPS

▪ `Static` **EPS**: `number` = `0.000001`

## Methods

### clone

▸ **clone**(): [`Spherical`](Spherical.md)

#### Returns

[`Spherical`](Spherical.md)


### copy

▸ **copy**(`other`): [`Spherical`](Spherical.md)

#### Parameters

| Name | Type |
| --- | --- |
| `other` | [`Spherical`](Spherical.md) |

#### Returns

[`Spherical`](Spherical.md)


### makeSafe

▸ **makeSafe**(): [`Spherical`](Spherical.md)

restrict phi to be between EPS and PI-EPS。

#### Returns

[`Spherical`](Spherical.md)


### set

▸ **set**(`radius`, `phi`, `theta`): [`Spherical`](Spherical.md)

#### Parameters

| Name | Type |
| --- | --- |
| `radius` | `number` |
| `phi` | `number` |
| `theta` | `number` |

#### Returns

[`Spherical`](Spherical.md)


### setFromCartesianCoords

▸ **setFromCartesianCoords**(`x`, `y`, `z`): [`Spherical`](Spherical.md)

从笛卡尔坐标系的x、y、z转换。

#### Parameters

| Name | Type |
| --- | --- |
| `x` | `number` |
| `y` | `number` |
| `z` | `number` |

#### Returns

[`Spherical`](Spherical.md)


### setFromVector3

▸ **setFromVector3**(`vector`): [`Spherical`](Spherical.md)

从笛卡尔坐标系的Vector3转换。

#### Parameters

| Name | Type |
| --- | --- |
| `vector` | [`Vector3`](Vector3.md) |

#### Returns

[`Spherical`](Spherical.md)


### toVector3

▸ **toVector3**(`vector?`): [`Vector3`](Vector3.md)

转换到笛卡尔坐标系的Vector3。

#### Parameters

| Name | Type |
| --- | --- |
| `vector?` | [`Vector3`](Vector3.md) |

#### Returns

[`Vector3`](Vector3.md)
