# Class: Vector3

> 官方文档：[Class: Vector3](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Vector3.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Vector3
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Vector3

## Table of contents

### Constructors

- [constructor](Vector3.md)

### Properties

- [ForwardLH](Vector3.md)
- [ONE](Vector3.md)
- [Phys3D](Vector3.md)
- [Up](Vector3.md)
- [ZERO](Vector3.md)

### Accessors

- [x](Vector3.md)
- [y](Vector3.md)
- [z](Vector3.md)

### Methods

- [abs](Vector3.md)
- [add](Vector3.md)
- [angleTo](Vector3.md)
- [applyMatrix4](Vector3.md)
- [applyMatrix4Raw](Vector3.md)
- [applyQuaternion](Vector3.md)
- [clone](Vector3.md)
- [cross](Vector3.md)
- [distanceTo](Vector3.md)
- [dot](Vector3.md)
- [equal](Vector3.md)
- [fromArray](Vector3.md)
- [fromPhysics](Vector3.md)
- [get](Vector3.md)
- [isZero](Vector3.md)
- [length](Vector3.md)
- [lerp](Vector3.md)
- [negate](Vector3.md)
- [normalize](Vector3.md)
- [print](Vector3.md)
- [scale](Vector3.md)
- [scaleXYZ](Vector3.md)
- [set](Vector3.md)
- [setArray](Vector3.md)
- [setFromArray](Vector3.md)
- [setFromMatrixColumn](Vector3.md)
- [setFromMatrixPosition](Vector3.md)
- [setFromMatrixScale](Vector3.md)
- [setValue](Vector3.md)
- [sub](Vector3.md)
- [toArray](Vector3.md)
- [toPhysics](Vector3.md)
- [transformDirection](Vector3.md)
- [transformDirectionRaw](Vector3.md)
- [clearPhysicsPool](Vector3.md)
- [createFromArray](Vector3.md)
- [createFromNumber](Vector3.md)
- [createFromTypedArray](Vector3.md)
- [fromPhysics](Vector3.md)
- [transformCoordinate](Vector3.md)
- [transformQuat](Vector3.md)

## Constructors

### constructor

• **new Vector3**(`raw?`, `offset?`)

#### Parameters

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

## Properties

### ForwardLH

▪ `Static` `Readonly` **ForwardLH**: [`Vector3`](Vector3.md)

前方向，基于左手坐标系，不要对该对象进行修改

**`static`**

**`memberof`** Vector3


### ONE

▪ `Static` `Readonly` **ONE**: [`Vector3`](Vector3.md)

一向量，不要对该对象进行修改

**`readonly`**

**`static`**

**`memberof`** Vector3


### Phys3D

▪ `Static` `Optional` **Phys3D**: typeof `phys3D`


### Up

▪ `Static` `Readonly` **Up**: [`Vector3`](Vector3.md)

上方向，不要对该对象进行修改

**`static`**

**`memberof`** Vector3


### ZERO

▪ `Static` `Readonly` **ZERO**: [`Vector3`](Vector3.md)

零向量，不要对该对象进行修改

**`readonly`**

**`static`**

**`memberof`** Vector3

## Accessors

### x

• `get` **x**(): `number`

x值

**`memberof`** Vector3

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

**`memberof`** Vector3

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

**`memberof`** Vector3

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

### abs

▸ **abs**(): [`Vector3`](Vector3.md)

#### Returns

[`Vector3`](Vector3.md)


### add

▸ **add**(`v`, `dst?`): [`Vector3`](Vector3.md)

向量加法

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector3`](Vector3.md) | 目标向量 |
| `dst?` | [`Vector3`](Vector3.md) | - |

#### Returns

[`Vector3`](Vector3.md)

计算结果


### angleTo

▸ **angleTo**(`location`, `dst?`): [`Vector3`](Vector3.md)

获取到目标点的角度

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `location` | [`Vector3`](Vector3.md) | 目标点 |
| `dst?` | [`Vector3`](Vector3.md) | - |

#### Returns

[`Vector3`](Vector3.md)

计算结果


### applyMatrix4

▸ **applyMatrix4**(`m`): [`Vector3`](Vector3.md)

create by janzen
Multiplies this vector (with an implicit 1 in the 4th dimension) and m, and divides by perspective.

#### Parameters

| Name | Type |
| --- | --- |
| `m` | [`Matrix4`](Matrix4.md) |

#### Returns

[`Vector3`](Vector3.md)


### applyMatrix4Raw

▸ **applyMatrix4Raw**(`m`): [`Vector3`](Vector3.md)

create by roamye
Multiplies this vector (with an implicit 1 in the 4th dimension) and m, and divides by perspective.

#### Parameters

| Name | Type |
| --- | --- |
| `m` | `Float32Array` |

#### Returns

[`Vector3`](Vector3.md)


### applyQuaternion

▸ **applyQuaternion**(`q`): [`Vector3`](Vector3.md)

#### Parameters

| Name | Type |
| --- | --- |
| `q` | [`Quaternion`](Quaternion.md) |

#### Returns

[`Vector3`](Vector3.md)


### clone

▸ **clone**(): [`Vector3`](Vector3.md)

拷贝该向量

**`memberof`** Vector3

#### Returns

[`Vector3`](Vector3.md)

拷贝出来的对象


### cross

▸ **cross**(`v`, `dst?`): [`Vector3`](Vector3.md)

向量叉乘

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector3`](Vector3.md) | 目标向量 |
| `dst?` | [`Vector3`](Vector3.md) | - |

#### Returns

[`Vector3`](Vector3.md)

计算结果


### distanceTo

▸ **distanceTo**(`p`): `number`

获取到目标点的距离

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `p` | [`Vector3`](Vector3.md) | 目标点 |

#### Returns

`number`

计算结果


### dot

▸ **dot**(`v`): `number`

向量点乘

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector3`](Vector3.md) | 目标向量 |

#### Returns

`number`

计算结果


### equal

▸ **equal**(`v`): `boolean`

判断与目标向量的值是否相等

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector3`](Vector3.md) | 目标向量 |

#### Returns

`boolean`

是否相等，这里误差小于10^-6视为相等


### fromArray

▸ **fromArray**(`array`, `offset`): [`Vector3`](Vector3.md)

#### Parameters

| Name | Type |
| --- | --- |
| `array` | `Float32Array` |
| `offset` | `number` |

#### Returns

[`Vector3`](Vector3.md)


### fromPhysics

▸ **fromPhysics**(`v`): [`Vector3`](Vector3.md)

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `any` |

#### Returns

[`Vector3`](Vector3.md)


### get

▸ **get**(`i`): `number`

#### Parameters

| Name | Type |
| --- | --- |
| `i` | `number` |

#### Returns

`number`


### isZero

▸ **isZero**(): `boolean`

是否为零向量

**`memberof`** Vector3

#### Returns

`boolean`


### length

▸ **length**(): `number`

向量的模

**`memberof`** Vector3

#### Returns

`number`

计算结果


### lerp

▸ **lerp**(`v`, `f`, `dst?`): [`Vector3`](Vector3.md)

在该向量与目标向量之间计算插值

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector3`](Vector3.md) | 目标向量 |
| `f` | `number` | 插值系数 |
| `dst?` | [`Vector3`](Vector3.md) | - |

#### Returns

[`Vector3`](Vector3.md)

计算结果


### negate

▸ **negate**(): [`Vector3`](Vector3.md)

取反

#### Returns

[`Vector3`](Vector3.md)


### normalize

▸ **normalize**(`dst?`): [`Vector3`](Vector3.md)

向量归一化

**`memberof`** Vector3

#### Parameters

| Name | Type |
| --- | --- |
| `dst?` | [`Vector3`](Vector3.md) |

#### Returns

[`Vector3`](Vector3.md)

计算结果


### print

▸ **print**(): `void`

#### Returns

`void`


### scale

▸ **scale**(`f`, `dst?`): [`Vector3`](Vector3.md)

向量缩放

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `f` | `number` | 缩放比 |
| `dst?` | [`Vector3`](Vector3.md) | - |

#### Returns

[`Vector3`](Vector3.md)

计算结果


### scaleXYZ

▸ **scaleXYZ**(`x`, `y`, `z`, `dst?`): [`Vector3`](Vector3.md)

向量缩放

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x缩放比 |
| `y` | `number` | y缩放比 |
| `z` | `number` | z缩放比 |
| `dst?` | [`Vector3`](Vector3.md) | - |

#### Returns

[`Vector3`](Vector3.md)

计算结果


### set

▸ **set**(`v`): [`Vector3`](Vector3.md)

拷贝目标向量的值到该向量

**`memberof`** Vector3

#### Parameters

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](Vector3.md) |

#### Returns

[`Vector3`](Vector3.md)

自身


### setArray

▸ **setArray**(`value`, `offset?`): [`Vector3`](Vector3.md)

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `ArrayLike`<`number`> |
| `offset?` | `number` |

#### Returns

[`Vector3`](Vector3.md)


### setFromArray

▸ **setFromArray**(`xyz`): [`Vector3`](Vector3.md)

#### Parameters

| Name | Type |
| --- | --- |
| `xyz` | `number`[] |

#### Returns

[`Vector3`](Vector3.md)


### setFromMatrixColumn

▸ **setFromMatrixColumn**(`m`, `index`): [`Vector3`](Vector3.md)

#### Parameters

| Name | Type |
| --- | --- |
| `m` | [`Matrix4`](Matrix4.md) |
| `index` | `number` |

#### Returns

[`Vector3`](Vector3.md)


### setFromMatrixPosition

▸ **setFromMatrixPosition**(`worldMatrix`): [`Vector3`](Vector3.md)

create by janzen
Sets this vector to the position elements of the transformation matrix

#### Parameters

| Name | Type |
| --- | --- |
| `worldMatrix` | [`Matrix4`](Matrix4.md) |

#### Returns

[`Vector3`](Vector3.md)


### setFromMatrixScale

▸ **setFromMatrixScale**(`m`): [`Vector3`](Vector3.md)

#### Parameters

| Name | Type |
| --- | --- |
| `m` | [`Matrix4`](Matrix4.md) |

#### Returns

[`Vector3`](Vector3.md)


### setValue

▸ **setValue**(`x`, `y`, `z`): [`Vector3`](Vector3.md)

设置向量的值

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x |
| `y` | `number` | y |
| `z` | `number` | z |

#### Returns

[`Vector3`](Vector3.md)

自身


### sub

▸ **sub**(`v`, `dst?`): [`Vector3`](Vector3.md)

向量减法

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector3`](Vector3.md) | 目标向量 |
| `dst?` | [`Vector3`](Vector3.md) | - |

#### Returns

[`Vector3`](Vector3.md)

计算结果


### toArray

▸ **toArray**(): [`number`, `number`, `number`]

返回向量数据

**`memberof`** Vector3

#### Returns

[`number`, `number`, `number`]

矩阵数据，以JSArray返回


### toPhysics

▸ **toPhysics**(): `any`

created by shanexyzhou
生成物理引擎内的RawVec3f

#### Returns

`any`


### transformDirection

▸ **transformDirection**(`m`): [`Vector3`](Vector3.md)

create by janzen
Transforms the direction of this vector by a matrix (the upper left 3 x 3 subset of a m) and then normalizes the result.

#### Parameters

| Name | Type |
| --- | --- |
| `m` | [`Matrix4`](Matrix4.md) |

#### Returns

[`Vector3`](Vector3.md)


### transformDirectionRaw

▸ **transformDirectionRaw**(`raw`): [`Vector3`](Vector3.md)

create by roamye
Transforms the direction of this vector by a matrix (the upper left 3 x 3 subset of a m) and then normalizes the result.

#### Parameters

| Name | Type |
| --- | --- |
| `raw` | `Float32Array` |

#### Returns

[`Vector3`](Vector3.md)


### clearPhysicsPool

▸ `Static` **clearPhysicsPool**(): `void`

#### Returns

`void`


### createFromArray

▸ `Static` **createFromArray**(`array`): [`Vector3`](Vector3.md)

使用一个数组创建
此操作会拷贝一份数组

**`static`**

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `array` | `number`[] | 数据源，长度必须为3，否则会抛出异常 |

#### Returns

[`Vector3`](Vector3.md)

创建出来的向量


### createFromNumber

▸ `Static` **createFromNumber**(`x`, `y`, `z`): [`Vector3`](Vector3.md)

使用数值创建
推荐使用这种方式代替new Vector3

**`static`**

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x |
| `y` | `number` | y |
| `z` | `number` | z |

#### Returns

[`Vector3`](Vector3.md)

创建出来的向量


### createFromTypedArray

▸ `Static` **createFromTypedArray**(`array`, `offset?`): [`Vector3`](Vector3.md)

使用某个已有的typedArray创建
此操作不会拷贝数据，而是在原来的内存区域上操作

**`static`**

**`memberof`** Vector3

#### Parameters

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `array` | `Float32Array` | `undefined` | 数据源 |
| `offset` | `number` | `0` | - |

#### Returns

[`Vector3`](Vector3.md)


### fromPhysics

▸ `Static` **fromPhysics**(`v`): [`Vector3`](Vector3.md)

created by shanexyzhou
从物理引擎内的RawVec3f生成Vector3

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `any` |

#### Returns

[`Vector3`](Vector3.md)


### transformCoordinate

▸ `Static` **transformCoordinate**(`coordinate`, `transform`, `dst?`): [`Vector3`](Vector3.md)

#### Parameters

| Name | Type |
| --- | --- |
| `coordinate` | [`Vector3`](Vector3.md) |
| `transform` | [`Matrix4`](Matrix4.md) |
| `dst?` | [`Vector3`](Vector3.md) |

#### Returns

[`Vector3`](Vector3.md)


### transformQuat

▸ `Static` **transformQuat**(`source`, `rotation`, `dst?`): [`Vector3`](Vector3.md)

使用四元数进行向量旋转

**`static`**

**`memberof`** Vector3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `source` | [`Vector3`](Vector3.md) | 源向量 |
| `rotation` | [`Quaternion`](Quaternion.md) | 用于旋转的四元数 |
| `dst?` | [`Vector3`](Vector3.md) | - |

#### Returns

[`Vector3`](Vector3.md)

计算结果
