# Class: BoundBox

> 官方文档：[Class: BoundBox](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/BoundBox.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / BoundBox
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / BoundBox

## Table of contents

### Constructors

- [constructor](BoundBox.md)

### Properties

- [OFFSETS](BoundBox.md)

### Accessors

- [center](BoundBox.md)
- [size](BoundBox.md)

### Methods

- [addPoint](BoundBox.md)
- [endInitByPoints](BoundBox.md)
- [initByPoints](BoundBox.md)
- [setValue](BoundBox.md)
- [startInitByPoints](BoundBox.md)
- [createFromCenterAndSize](BoundBox.md)

## Constructors

### constructor

• **new BoundBox**(`raw?`, `offset?`)

#### Parameters

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

## Properties

### OFFSETS

▪ `Static` `Readonly` **OFFSETS**: `Readonly`<{ `center`: `number` = 0; `size`: `number` = 3 }>

## Accessors

### center

• `get` **center**(): [`Vector3`](Vector3.md)

包围盒中心

**`memberof`** BoundBox

#### Returns

[`Vector3`](Vector3.md)

• `set` **center**(`val`): `void`

包围盒中心

#### Parameters

| Name | Type |
| --- | --- |
| `val` | [`Vector3`](Vector3.md) |

#### Returns

`void`


### size

• `get` **size**(): [`Vector3`](Vector3.md)

包围盒尺寸

**`memberof`** BoundBox

#### Returns

[`Vector3`](Vector3.md)

• `set` **size**(`val`): `void`

包围盒尺寸

#### Parameters

| Name | Type |
| --- | --- |
| `val` | [`Vector3`](Vector3.md) |

#### Returns

`void`

## Methods

### addPoint

▸ **addPoint**(`corner`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `corner` | [`Vector3`](Vector3.md) |

#### Returns

`void`


### endInitByPoints

▸ **endInitByPoints**(): `void`

#### Returns

`void`


### initByPoints

▸ **initByPoints**(`points`, `length?`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `points` | [`Vector3`](Vector3.md)[] |
| `length?` | `number` |

#### Returns

`void`


### setValue

▸ **setValue**(`center`, `size`): [`BoundBox`](BoundBox.md)

设置值

**`memberof`** BoundBox

#### Parameters

| Name | Type |
| --- | --- |
| `center` | [`Vector3`](Vector3.md) |
| `size` | [`Vector3`](Vector3.md) |

#### Returns

[`BoundBox`](BoundBox.md)


### startInitByPoints

▸ **startInitByPoints**(): `void`

#### Returns

`void`


### createFromCenterAndSize

▸ `Static` **createFromCenterAndSize**(`center`, `size`): [`BoundBox`](BoundBox.md)

使用中心和尺寸创建包围球

**`static`**

**`memberof`** BoundBall

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `center` | [`Vector3`](Vector3.md) | 中心 |
| `size` | [`Vector3`](Vector3.md) | 尺寸 |

#### Returns

[`BoundBox`](BoundBox.md)
