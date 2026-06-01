# Class: Vector2

> 官方文档：[Class: Vector2](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Vector2.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Vector2
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Vector2

## Table of contents

### Constructors

- [constructor](Vector2.md)

### Properties

- [ONE](Vector2.md)
- [ZERO](Vector2.md)

### Accessors

- [x](Vector2.md)
- [y](Vector2.md)

### Methods

- [add](Vector2.md)
- [clone](Vector2.md)
- [dot](Vector2.md)
- [equal](Vector2.md)
- [getAngle](Vector2.md)
- [isZero](Vector2.md)
- [length](Vector2.md)
- [lerp](Vector2.md)
- [negate](Vector2.md)
- [normalize](Vector2.md)
- [scale](Vector2.md)
- [set](Vector2.md)
- [setArray](Vector2.md)
- [setValue](Vector2.md)
- [sub](Vector2.md)
- [toArray](Vector2.md)
- [createFromArray](Vector2.md)
- [createFromNumber](Vector2.md)
- [createFromTypedArray](Vector2.md)

## Constructors

### constructor

• **new Vector2**(`raw?`, `offset?`)

#### Parameters

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

## Properties

### ONE

▪ `Static` `Readonly` **ONE**: [`Vector2`](Vector2.md)

一向量，不要对该对象进行修改

**`readonly`**

**`static`**

**`memberof`** Vector3


### ZERO

▪ `Static` `Readonly` **ZERO**: [`Vector2`](Vector2.md)

零向量，不要对该对象进行修改

**`readonly`**

**`static`**

**`memberof`** Vector3

## Accessors

### x

• `get` **x**(): `number`

x值

**`memberof`** Vector2

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

**`memberof`** Vector2

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

## Methods

### add

▸ **add**(`v`, `dst?`): [`Vector2`](Vector2.md)

向量加法

**`memberof`** Vector2

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector2`](Vector2.md) | 目标向量 |
| `dst?` | [`Vector2`](Vector2.md) | - |

#### Returns

[`Vector2`](Vector2.md)

计算结果


### clone

▸ **clone**(): [`Vector2`](Vector2.md)

拷贝该向量

**`memberof`** Vector2

#### Returns

[`Vector2`](Vector2.md)

拷贝出来的对象


### dot

▸ **dot**(`v`): `number`

向量点乘

**`memberof`** Vector2

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector2`](Vector2.md) | 目标向量 |

#### Returns

`number`

计算结果


### equal

▸ **equal**(`v`): `boolean`

判断与目标向量的值是否相等

**`memberof`** Vector2

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector2`](Vector2.md) | 目标向量 |

#### Returns

`boolean`

是否相等，这里误差小于10^-6视为相等


### getAngle

▸ **getAngle**(): `number`

获取向量旋转角，以角度表示

**`memberof`** Vector2

#### Returns

`number`

旋转角，以角度表示


### isZero

▸ **isZero**(): `boolean`

是否为零向量

**`memberof`** Vector2

#### Returns

`boolean`


### length

▸ **length**(): `number`

向量的模

**`memberof`** Vector2

#### Returns

`number`

计算结果


### lerp

▸ **lerp**(`v`, `f`, `dst?`): [`Vector2`](Vector2.md)

在该向量与目标向量之间计算插值

**`memberof`** Vector2

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector2`](Vector2.md) | 目标向量 |
| `f` | `number` | 插值系数 |
| `dst?` | [`Vector2`](Vector2.md) | - |

#### Returns

[`Vector2`](Vector2.md)

计算结果


### negate

▸ **negate**(): [`Vector2`](Vector2.md)

取反

#### Returns

[`Vector2`](Vector2.md)


### normalize

▸ **normalize**(`dst?`): [`Vector2`](Vector2.md)

向量归一化，如该向量为零向量，则结果依然为零向量

**`memberof`** Vector2

#### Parameters

| Name | Type |
| --- | --- |
| `dst?` | [`Vector2`](Vector2.md) |

#### Returns

[`Vector2`](Vector2.md)

计算结果


### scale

▸ **scale**(`f`, `dst?`): [`Vector2`](Vector2.md)

向量缩放

**`memberof`** Vector2

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `f` | `number` | 缩放比 |
| `dst?` | [`Vector2`](Vector2.md) | - |

#### Returns

[`Vector2`](Vector2.md)

计算结果


### set

▸ **set**(`val`): [`Vector2`](Vector2.md)

拷贝目标向量的值到该向量

**`memberof`** Vector2

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `val` | [`Vector2`](Vector2.md) | 目标向量 |

#### Returns

[`Vector2`](Vector2.md)

自身


### setArray

▸ **setArray**(`value`, `offset?`): [`Vector2`](Vector2.md)

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `ArrayLike`<`number`> |
| `offset?` | `number` |

#### Returns

[`Vector2`](Vector2.md)


### setValue

▸ **setValue**(`x`, `y`): [`Vector2`](Vector2.md)

设置向量的值

**`memberof`** Vector2

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x值 |
| `y` | `number` | y值 |

#### Returns

[`Vector2`](Vector2.md)

自身


### sub

▸ **sub**(`v`, `dst?`): [`Vector2`](Vector2.md)

向量减法

**`memberof`** Vector2

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector2`](Vector2.md) | 目标向量 |
| `dst?` | [`Vector2`](Vector2.md) | - |

#### Returns

[`Vector2`](Vector2.md)

计算结果


### toArray

▸ **toArray**(): `number`[]

返回向量数据

**`memberof`** Vector2

#### Returns

`number`[]

矩阵数据，以JSArray返回


### createFromArray

▸ `Static` **createFromArray**(`array`): [`Vector2`](Vector2.md)

使用一个数组创建
此操作会拷贝一份数组

**`static`**

**`memberof`** Vector2

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `array` | `number`[] | 数据源，长度必须为2，否则会抛出异常 |

#### Returns

[`Vector2`](Vector2.md)

创建出来的向量


### createFromNumber

▸ `Static` **createFromNumber**(`x`, `y`): [`Vector2`](Vector2.md)

使用数值创建
推荐使用这种方式代替new Vector2

**`static`**

**`memberof`** Vector2

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x |
| `y` | `number` | y |

#### Returns

[`Vector2`](Vector2.md)

创建出来的向量


### createFromTypedArray

▸ `Static` **createFromTypedArray**(`array`, `offset?`): [`Vector2`](Vector2.md)

使用某个已有的typedArray创建
此操作不会拷贝数据，而是在原来的内存区域上操作

**`static`**

**`memberof`** Vector2

#### Parameters

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `array` | `Float32Array` | `undefined` | 数据源 |
| `offset` | `number` | `0` | - |

#### Returns

[`Vector2`](Vector2.md)

创建出来的向量
