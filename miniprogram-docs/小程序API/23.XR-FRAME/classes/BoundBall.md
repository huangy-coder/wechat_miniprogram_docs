# Class: BoundBall

> 官方文档：[Class: BoundBall](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/BoundBall.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / BoundBall
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / BoundBall

## Table of contents

### Constructors

- [constructor](BoundBall.md)

### Properties

- [OFFSETS](BoundBall.md)

### Accessors

- [center](BoundBall.md)
- [radius](BoundBall.md)

### Methods

- [initByPointRadius](BoundBall.md)
- [initByPoints](BoundBall.md)
- [setValue](BoundBall.md)
- [createFromCenterAndRadius](BoundBall.md)

## Constructors

### constructor

• **new BoundBall**(`raw?`, `offset?`)

#### Parameters

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

## Properties

### OFFSETS

▪ `Static` `Readonly` **OFFSETS**: `Readonly`<{ `center`: `number` = 0; `radius`: `number` = 3 }>

## Accessors

### center

• `get` **center**(): [`Vector3`](Vector3.md)

包围球中心

**`memberof`** BoundBall

#### Returns

[`Vector3`](Vector3.md)

• `set` **center**(`val`): `void`

包围球中心

#### Parameters

| Name | Type |
| --- | --- |
| `val` | [`Vector3`](Vector3.md) |

#### Returns

`void`


### radius

• `get` **radius**(): `number`

包围球半径

**`memberof`** BoundBall

#### Returns

`number`

• `set` **radius**(`val`): `void`

包围球半径

#### Parameters

| Name | Type |
| --- | --- |
| `val` | `number` |

#### Returns

`void`

## Methods

### initByPointRadius

▸ **initByPointRadius**(`center`, `radius`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `center` | [`Vector3`](Vector3.md) |
| `radius` | `number` |

#### Returns

`void`


### initByPoints

▸ **initByPoints**(`points`): [`BoundBall`](BoundBall.md)

使用一系列点初始化

**`memberof`** BoundBall

#### Parameters

| Name | Type |
| --- | --- |
| `points` | [`Vector3`](Vector3.md)[] |

#### Returns

[`BoundBall`](BoundBall.md)

自身


### setValue

▸ **setValue**(`center`, `radius`): [`BoundBall`](BoundBall.md)

设置值

**`memberof`** BoundBall

#### Parameters

| Name | Type |
| --- | --- |
| `center` | [`Vector3`](Vector3.md) |
| `radius` | `number` |

#### Returns

[`BoundBall`](BoundBall.md)


### createFromCenterAndRadius

▸ `Static` **createFromCenterAndRadius**(`center`, `radius`): [`BoundBall`](BoundBall.md)

使用中心和半径创建包围球

**`static`**

**`memberof`** BoundBall

#### Parameters

| Name | Type |
| --- | --- |
| `center` | [`Vector3`](Vector3.md) |
| `radius` | `number` |

#### Returns

[`BoundBall`](BoundBall.md)
