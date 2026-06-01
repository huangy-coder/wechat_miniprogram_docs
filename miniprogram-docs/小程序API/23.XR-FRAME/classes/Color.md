# Class: Color

> 官方文档：[Class: Color](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Color.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Color
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Color

## Table of contents

### Constructors

- [constructor](Color.md)

### Properties

- [BlendType](Color.md)

### Accessors

- [a](Color.md)
- [b](Color.md)
- [g](Color.md)
- [r](Color.md)
- [BLACK](Color.md)
- [TRANSPARENT](Color.md)
- [WHITE](Color.md)

### Methods

- [clone](Color.md)
- [equals](Color.md)
- [mix](Color.md)
- [set](Color.md)
- [setRGBA](Color.md)
- [setValue32](Color.md)
- [toNormalizedArray](Color.md)
- [toRGBAString](Color.md)
- [blendColorHex](Color.md)
- [diffc](Color.md)
- [fromFloatArray](Color.md)
- [fromHex](Color.md)
- [fromHexString](Color.md)
- [getValue32FromHSVA](Color.md)
- [getValue32FromRGBA](Color.md)
- [hsvV2rgb](Color.md)
- [multiplyColorHex](Color.md)
- [percentRoundFn](Color.md)
- [randomMix](Color.md)
- [rgb2hsv](Color.md)

## Constructors

### constructor

• **new Color**(`r?`, `g?`, `b?`, `a?`)

#### Parameters

| Name | Type |
| --- | --- |
| `r?` | `number` |
| `g?` | `number` |
| `b?` | `number` |
| `a?` | `number` |

## Properties

### BlendType

▪ `Static` **BlendType**: typeof `BlendType`

## Accessors

### a

• `get` **a**(): `number`

#### Returns

`number`

• `set` **a**(`val`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `val` | `number` |

#### Returns

`void`


### b

• `get` **b**(): `number`

#### Returns

`number`

• `set` **b**(`val`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `val` | `number` |

#### Returns

`void`


### g

• `get` **g**(): `number`

#### Returns

`number`

• `set` **g**(`val`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `val` | `number` |

#### Returns

`void`


### r

• `get` **r**(): `number`

#### Returns

`number`

• `set` **r**(`val`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `val` | `number` |

#### Returns

`void`


### BLACK

• `Static` `get` **BLACK**(): [`Color`](Color.md)

#### Returns

[`Color`](Color.md)


### TRANSPARENT

• `Static` `get` **TRANSPARENT**(): [`Color`](Color.md)

#### Returns

[`Color`](Color.md)


### WHITE

• `Static` `get` **WHITE**(): [`Color`](Color.md)

#### Returns

[`Color`](Color.md)

## Methods

### clone

▸ **clone**(): [`Color`](Color.md)

#### Returns

[`Color`](Color.md)


### equals

▸ **equals**(`target`): `boolean`

#### Parameters

| Name | Type |
| --- | --- |
| `target` | [`Color`](Color.md) |

#### Returns

`boolean`


### mix

▸ **mix**(`color`, `dst?`): [`Color`](Color.md)

#### Parameters

| Name | Type |
| --- | --- |
| `color` | [`Color`](Color.md) |
| `dst?` | [`Color`](Color.md) |

#### Returns

[`Color`](Color.md)


### set

▸ **set**(`val`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `val` | [`Color`](Color.md) |

#### Returns

`void`


### setRGBA

▸ **setRGBA**(`r`, `g`, `b`, `a`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `r` | `number` |
| `g` | `number` |
| `b` | `number` |
| `a` | `number` |

#### Returns

`void`


### setValue32

▸ **setValue32**(`v32`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `v32` | `number` |

#### Returns

`void`


### toNormalizedArray

▸ **toNormalizedArray**(): [`number`, `number`, `number`, `number`]

#### Returns

[`number`, `number`, `number`, `number`]


### toRGBAString

▸ **toRGBAString**(): `string`

#### Returns

`string`


### blendColorHex

▸ `Static` **blendColorHex**(`colorHexA`, `colorHexB`, `type?`): `number`

#### Parameters

| Name | Type |
| --- | --- |
| `colorHexA` | `number` |
| `colorHexB` | `number` |
| `type` | `BlendType` |

#### Returns

`number`


### diffc

▸ `Static` **diffc**(`v`, `c`, `diff`): `number`

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `number` |
| `c` | `number` |
| `diff` | `number` |

#### Returns

`number`


### fromFloatArray

▸ `Static` **fromFloatArray**(`arr`): [`Color`](Color.md)

#### Parameters

| Name | Type |
| --- | --- |
| `arr` | `number`[] |

#### Returns

[`Color`](Color.md)


### fromHex

▸ `Static` **fromHex**(`hex`): [`Color`](Color.md)

#### Parameters

| Name | Type |
| --- | --- |
| `hex` | `number` |

#### Returns

[`Color`](Color.md)


### fromHexString

▸ `Static` **fromHexString**(`hexString`): [`Color`](Color.md)

#### Parameters

| Name | Type |
| --- | --- |
| `hexString` | `string` |

#### Returns

[`Color`](Color.md)


### getValue32FromHSVA

▸ `Static` **getValue32FromHSVA**(): `void`

#### Returns

`void`


### getValue32FromRGBA

▸ `Static` **getValue32FromRGBA**(`r`, `g`, `b`, `a`): `number`

#### Parameters

| Name | Type |
| --- | --- |
| `r` | `number` |
| `g` | `number` |
| `b` | `number` |
| `a` | `number` |

#### Returns

`number`


### hsvV2rgb

▸ `Static` **hsvV2rgb**(`h`, `s`, `v`, `dst?`): [`Vector3`](Vector3.md)

#### Parameters

| Name | Type |
| --- | --- |
| `h` | `number` |
| `s` | `number` |
| `v` | `number` |
| `dst?` | [`Vector3`](Vector3.md) |

#### Returns

[`Vector3`](Vector3.md)


### multiplyColorHex

▸ `Static` **multiplyColorHex**(`colorHexA`, `colorHexB`, `type?`): `number`

#### Parameters

| Name | Type |
| --- | --- |
| `colorHexA` | `number` |
| `colorHexB` | `number` |
| `type` | `BlendType` |

#### Returns

`number`


### percentRoundFn

▸ `Static` **percentRoundFn**(`num`): `number`

#### Parameters

| Name | Type |
| --- | --- |
| `num` | `number` |

#### Returns

`number`


### randomMix

▸ `Static` **randomMix**(`colorHexA`, `colorHexB`, `randomSeed?`): `number`

#### Parameters

| Name | Type |
| --- | --- |
| `colorHexA` | `number` |
| `colorHexB` | `number` |
| `randomSeed` | `number` |

#### Returns

`number`


### rgb2hsv

▸ `Static` **rgb2hsv**(`r`, `g`, `b`, `dst?`): [`Vector3`](Vector3.md)

#### Parameters

| Name | Type |
| --- | --- |
| `r` | `number` |
| `g` | `number` |
| `b` | `number` |
| `dst?` | [`Vector3`](Vector3.md) |

#### Returns

[`Vector3`](Vector3.md)
