# Class: OBB

> 官方文档：[Class: OBB](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/OBB.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / OBB
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / OBB

## Table of contents

### Constructors

- [constructor](OBB.md)

### Accessors

- [AxisX](OBB.md)
- [AxisY](OBB.md)
- [AxisZ](OBB.md)
- [center](OBB.md)
- [depth](OBB.md)
- [height](OBB.md)
- [width](OBB.md)

### Methods

- [setForward](OBB.md)
- [setValues](OBB.md)

## Constructors

### constructor

• **new OBB**()

## Accessors

### AxisX

• `get` **AxisX**(): [`Vector3`](Vector3.md)

#### Returns

[`Vector3`](Vector3.md)


### AxisY

• `get` **AxisY**(): [`Vector3`](Vector3.md)

#### Returns

[`Vector3`](Vector3.md)


### AxisZ

• `get` **AxisZ**(): [`Vector3`](Vector3.md)

#### Returns

[`Vector3`](Vector3.md)


### center

• `get` **center**(): [`Vector3`](Vector3.md)

#### Returns

[`Vector3`](Vector3.md)

• `set` **center**(`pos`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `pos` | [`Vector3`](Vector3.md) |

#### Returns

`void`


### depth

• `get` **depth**(): `number`

#### Returns

`number`

• `set` **depth**(`d`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `d` | `number` |

#### Returns

`void`


### height

• `get` **height**(): `number`

#### Returns

`number`

• `set` **height**(`h`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `h` | `number` |

#### Returns

`void`


### width

• `get` **width**(): `number`

#### Returns

`number`

• `set` **width**(`w`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `w` | `number` |

#### Returns

`void`

## Methods

### setForward

▸ **setForward**(`forward`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `forward` | [`Vector3`](Vector3.md) |

#### Returns

`void`


### setValues

▸ **setValues**(`cenX`, `cenY`, `cenZ`, `forward`, `w`, `h`, `d`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `cenX` | `number` |
| `cenY` | `number` |
| `cenZ` | `number` |
| `forward` | [`Vector3`](Vector3.md) |
| `w` | `number` |
| `h` | `number` |
| `d` | `number` |

#### Returns

`void`
