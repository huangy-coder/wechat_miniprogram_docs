# Class: Vector4

> 官方文档：[Class: Vector4](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Vector4.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Vector4
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Vector4

## Table of contents

### Constructors

- [constructor](Vector4.md)

### Properties

- [ONE](Vector4.md)
- [ZERO](Vector4.md)

### Accessors

- [w](Vector4.md)
- [x](Vector4.md)
- [y](Vector4.md)
- [z](Vector4.md)

### Methods

- [add](Vector4.md)
- [clone](Vector4.md)
- [dot](Vector4.md)
- [equal](Vector4.md)
- [isZero](Vector4.md)
- [lerp](Vector4.md)
- [negate](Vector4.md)
- [scale](Vector4.md)
- [set](Vector4.md)
- [setArray](Vector4.md)
- [setValue](Vector4.md)
- [sub](Vector4.md)
- [toArray](Vector4.md)
- [createFromArray](Vector4.md)
- [createFromNumber](Vector4.md)
- [createFromTypedArray](Vector4.md)

## Constructors

### constructor

• **new Vector4**(`raw?`, `offset?`)

#### Parameters

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

## Properties

### ONE

▪ `Static` `Readonly` **ONE**: [`Vector4`](Vector4.md)

一向量，不要对该对象进行修改

**`readonly`**

**`static`**

**`memberof`** Vector3


### ZERO

▪ `Static` `Readonly` **ZERO**: [`Vector4`](Vector4.md)

零向量，不要对该对象进行修改

**`static`**

**`readonly`**

**`memberof`** Vector4

## Accessors

### w

• `get` **w**(): `number`

w值

**`memberof`** Vector4

#### Returns

`number`

• `set` **w**(`val`): `void`

w值

#### Parameters

| Name | Type |
| --- | --- |
| `val` | `number` |

#### Returns

`void`


### x

• `get` **x**(): `number`

x值

**`memberof`** Vector4

#### Returns

`number`

• `set` **x**(`val`): `void`

x值

#### Parameters

| Name | Type |
| --- | --- |
| `val` | `number` |

#### Returns

`void`


### y

• `get` **y**(): `number`

y值

**`memberof`** Vector4

#### Returns

`number`

• `set` **y**(`val`): `void`

y值

#### Parameters

| Name | Type |
| --- | --- |
| `val` | `number` |

#### Returns

`void`


### z

• `get` **z**(): `number`

z值

**`memberof`** Vector4

#### Returns

`number`

• `set` **z**(`val`): `void`

z值

#### Parameters

| Name | Type |
| --- | --- |
| `val` | `number` |

#### Returns

`void`

## Methods

### add

▸ **add**(`v`, `dst?`): [`Vector4`](Vector4.md)

向量加法

**`memberof`** Vector4

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector4`](Vector4.md) | 目标向量 |
| `dst?` | [`Vector4`](Vector4.md) | - |

#### Returns

[`Vector4`](Vector4.md)

计算结果


### clone

▸ **clone**(): [`Vector4`](Vector4.md)

拷贝该向量

**`memberof`** Vector4

#### Returns

[`Vector4`](Vector4.md)

拷贝出来的对象


### dot

▸ **dot**(`v`): `number`

向量点乘

**`memberof`** Vector4

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector4`](Vector4.md) | 目标向量 |

#### Returns

`number`

计算结果


### equal

▸ **equal**(`v`): `boolean`

判断与目标向量的值是否相等

**`memberof`** Vector4

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector4`](Vector4.md) | 目标向量 |

#### Returns

`boolean`

是否相等，这里误差小于10^-6视为相等


### isZero

▸ **isZero**(): `boolean`

是否为零向量

**`memberof`** Vector4

#### Returns

`boolean`


### lerp

▸ **lerp**(`v`, `f`, `dst?`): [`Vector4`](Vector4.md)

在该向量与目标向量之间计算插值

**`memberof`** Vector4

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector4`](Vector4.md) | 目标向量 |
| `f` | `number` | 插值系数 |
| `dst?` | [`Vector4`](Vector4.md) | - |

#### Returns

[`Vector4`](Vector4.md)

计算结果


### negate

▸ **negate**(): [`Vector4`](Vector4.md)

取反

#### Returns

[`Vector4`](Vector4.md)


### scale

▸ **scale**(`f`, `dst?`): [`Vector4`](Vector4.md)

向量缩放

**`memberof`** Vector4

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `f` | `number` | 缩放比 |
| `dst?` | [`Vector4`](Vector4.md) | - |

#### Returns

[`Vector4`](Vector4.md)

计算结果


### set

▸ **set**(`v`): [`Vector4`](Vector4.md)

拷贝目标向量的值到该向量

**`memberof`** Vector4

#### Parameters

| Name | Type |
| --- | --- |
| `v` | [`Vector4`](Vector4.md) |

#### Returns

[`Vector4`](Vector4.md)

自身


### setArray

▸ **setArray**(`value`, `offset?`): [`Vector4`](Vector4.md)

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `ArrayLike`<`number`> |
| `offset?` | `number` |

#### Returns

[`Vector4`](Vector4.md)


### setValue

▸ **setValue**(`x`, `y`, `z`, `w`): [`Vector4`](Vector4.md)

设置向量的值

**`memberof`** Vector4

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x值 |
| `y` | `number` | y值 |
| `z` | `number` | z值 |
| `w` | `number` | w值 |

#### Returns

[`Vector4`](Vector4.md)

自身


### sub

▸ **sub**(`v`, `dst?`): [`Vector4`](Vector4.md)

向量减法

**`memberof`** Vector4

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector4`](Vector4.md) | 目标向量 |
| `dst?` | [`Vector4`](Vector4.md) | - |

#### Returns

[`Vector4`](Vector4.md)

计算结果


### toArray

▸ **toArray**(): `number`[]

返回向量数据

**`memberof`** Vector4

#### Returns

`number`[]

矩阵数据，以JSArray返回


### createFromArray

▸ `Static` **createFromArray**(`array`): [`Vector4`](Vector4.md)

使用一个数组创建
此操作会拷贝一份数组

**`static`**

**`memberof`** Vector4

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `array` | `number`[] | 数据源，长度必须为4，否则会抛出异常 |

#### Returns

[`Vector4`](Vector4.md)

创建出来的向量


### createFromNumber

▸ `Static` **createFromNumber**(`x`, `y`, `z`, `w`): [`Vector4`](Vector4.md)

使用数值创建
推荐使用这种方式代替new Vector4

**`static`**

**`memberof`** Vector4

#### Parameters

| Name | Type |
| --- | --- |
| `x` | `number` |
| `y` | `number` |
| `z` | `number` |
| `w` | `number` |

#### Returns

[`Vector4`](Vector4.md)

创建出来的向量


### createFromTypedArray

▸ `Static` **createFromTypedArray**(`array`, `offset?`): [`Vector4`](Vector4.md)

使用某个已有的typedArray创建
此操作不会拷贝数据，而是在原来的内存区域上操作

**`static`**

**`memberof`** Vector4

#### Parameters

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `array` | `Float32Array` | `undefined` | 数据源 |
| `offset` | `number` | `0` | - |

#### Returns

[`Vector4`](Vector4.md)
