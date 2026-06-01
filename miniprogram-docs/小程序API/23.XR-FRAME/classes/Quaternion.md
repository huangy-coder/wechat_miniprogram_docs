# Class: Quaternion

> 官方文档：[Class: Quaternion](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Quaternion.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Quaternion
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Quaternion

## Table of contents

### Constructors

- [constructor](Quaternion.md)

### Properties

- [DEFAULT](Quaternion.md)
- [Phys3D](Quaternion.md)

### Accessors

- [w](Quaternion.md)
- [x](Quaternion.md)
- [y](Quaternion.md)
- [z](Quaternion.md)

### Methods

- [add](Quaternion.md)
- [angleTo](Quaternion.md)
- [clone](Quaternion.md)
- [dot](Quaternion.md)
- [equal](Quaternion.md)
- [fromPhysics](Quaternion.md)
- [invert](Quaternion.md)
- [isDefault](Quaternion.md)
- [length](Quaternion.md)
- [multiply](Quaternion.md)
- [normalize](Quaternion.md)
- [premultiply](Quaternion.md)
- [rotateTowards](Quaternion.md)
- [set](Quaternion.md)
- [setArray](Quaternion.md)
- [setFromEulerAngles](Quaternion.md)
- [setFromUnitVectors](Quaternion.md)
- [setFromYawRollPitch](Quaternion.md)
- [setValue](Quaternion.md)
- [slerp](Quaternion.md)
- [sub](Quaternion.md)
- [toAxisUnit](Quaternion.md)
- [toEulerAngles](Quaternion.md)
- [toPhysics](Quaternion.md)
- [transformVector3](Quaternion.md)
- [clearPhysicsPool](Quaternion.md)
- [createFromArray](Quaternion.md)
- [createFromAxisAngle](Quaternion.md)
- [createFromMatrix4](Quaternion.md)
- [createFromNumber](Quaternion.md)
- [createFromTypedArray](Quaternion.md)
- [createFromUnitVectors](Quaternion.md)
- [fromEulerAngles](Quaternion.md)
- [fromPhysics](Quaternion.md)
- [lookRotation](Quaternion.md)

## Constructors

### constructor

• **new Quaternion**(`raw?`, `offset?`)

#### Parameters

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

## Properties

### DEFAULT

▪ `Static` `Readonly` **DEFAULT**: [`Quaternion`](Quaternion.md)

默认四元数，不要对该对象进行修改

**`readonly`**

**`static`**

**`memberof`** Quaternion


### Phys3D

▪ `Static` `Optional` **Phys3D**: typeof `phys3D`

## Accessors

### w

• `get` **w**(): `number`

w值

**`memberof`** Quaternion

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

**`memberof`** Quaternion

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

**`memberof`** Quaternion

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

**`memberof`** Quaternion

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

▸ **add**(`quat`, `dst?`): [`Quaternion`](Quaternion.md)

四元数相加

**`memberof`** Quaternion

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `quat` | [`Quaternion`](Quaternion.md) | 目标四元数 |
| `dst?` | [`Quaternion`](Quaternion.md) | - |

#### Returns

[`Quaternion`](Quaternion.md)

计算结果


### angleTo

▸ **angleTo**(`q`): `number`

相对角度

#### Parameters

| Name | Type |
| --- | --- |
| `q` | [`Quaternion`](Quaternion.md) |

#### Returns

`number`


### clone

▸ **clone**(): [`Quaternion`](Quaternion.md)

拷贝四元数

**`memberof`** Quaternion

#### Returns

[`Quaternion`](Quaternion.md)

拷贝后的对象


### dot

▸ **dot**(`q`): `number`

点乘

#### Parameters

| Name | Type |
| --- | --- |
| `q` | [`Quaternion`](Quaternion.md) |

#### Returns

`number`


### equal

▸ **equal**(`quat`): `boolean`

判断与目标四元数的值是否相等

**`memberof`** Quaternion

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `quat` | [`Quaternion`](Quaternion.md) | 目标四元数 |

#### Returns

`boolean`


### fromPhysics

▸ **fromPhysics**(`v`): [`Quaternion`](Quaternion.md)

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `RawQuaternion` |

#### Returns

[`Quaternion`](Quaternion.md)


### invert

▸ **invert**(`dst?`): [`Quaternion`](Quaternion.md)

四元数反转

**`memberof`** Quaternion

#### Parameters

| Name | Type |
| --- | --- |
| `dst?` | [`Quaternion`](Quaternion.md) |

#### Returns

[`Quaternion`](Quaternion.md)

计算结果


### isDefault

▸ **isDefault**(): `boolean`

四元数是否为默认四元数（表示零旋转）

**`memberof`** Quaternion

#### Returns

`boolean`


### length

▸ **length**(): `number`

#### Returns

`number`


### multiply

▸ **multiply**(`quat`, `dst?`): [`Quaternion`](Quaternion.md)

四元数相乘

**`memberof`** Quaternion

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `quat` | [`Quaternion`](Quaternion.md) | 目标四元数 |
| `dst?` | [`Quaternion`](Quaternion.md) | - |

#### Returns

[`Quaternion`](Quaternion.md)

计算结果


### normalize

▸ **normalize**(): [`Quaternion`](Quaternion.md)

#### Returns

[`Quaternion`](Quaternion.md)


### premultiply

▸ **premultiply**(`q`): [`Quaternion`](Quaternion.md)

#### Parameters

| Name | Type |
| --- | --- |
| `q` | [`Quaternion`](Quaternion.md) |

#### Returns

[`Quaternion`](Quaternion.md)


### rotateTowards

▸ **rotateTowards**(`q`, `step`): [`Quaternion`](Quaternion.md)

转向对应的角度

#### Parameters

| Name | Type |
| --- | --- |
| `q` | `any` |
| `step` | `any` |

#### Returns

[`Quaternion`](Quaternion.md)


### set

▸ **set**(`quat`): [`Quaternion`](Quaternion.md)

拷贝目标四元数的值到自身

**`memberof`** Quaternion

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `quat` | [`Quaternion`](Quaternion.md) | 目标四元数 |

#### Returns

[`Quaternion`](Quaternion.md)

自身


### setArray

▸ **setArray**(`value`, `offset?`): [`Quaternion`](Quaternion.md)

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `ArrayLike`<`number`> |
| `offset?` | `number` |

#### Returns

[`Quaternion`](Quaternion.md)


### setFromEulerAngles

▸ **setFromEulerAngles**(`euler`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `euler` | [`Vector3`](Vector3.md) |

#### Returns

`void`


### setFromUnitVectors

▸ **setFromUnitVectors**(`vFrom`, `vTo`): [`Quaternion`](Quaternion.md)

#### Parameters

| Name | Type |
| --- | --- |
| `vFrom` | `any` |
| `vTo` | `any` |

#### Returns

[`Quaternion`](Quaternion.md)


### setFromYawRollPitch

▸ **setFromYawRollPitch**(`yaw`, `roll`, `pitch`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `yaw` | `number` |
| `roll` | `number` |
| `pitch` | `number` |

#### Returns

`void`


### setValue

▸ **setValue**(`x`, `y`, `z`, `w`): [`Quaternion`](Quaternion.md)

设置四元数的值

**`memberof`** Quaternion

#### Parameters

| Name | Type |
| --- | --- |
| `x` | `number` |
| `y` | `number` |
| `z` | `number` |
| `w` | `number` |

#### Returns

[`Quaternion`](Quaternion.md)

自身


### slerp

▸ **slerp**(`right`, `t`, `dst?`): [`Quaternion`](Quaternion.md)

球面插值

**`memberof`** Quaternion

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `right` | [`Quaternion`](Quaternion.md) | 目标四元数 |
| `t` | `number` | 插值系数，越接近 1 则结果越接近目标 |
| `dst?` | [`Quaternion`](Quaternion.md) | - |

#### Returns

[`Quaternion`](Quaternion.md)

计算结果


### sub

▸ **sub**(`quat`, `dst?`): [`Quaternion`](Quaternion.md)

四元数相减

**`memberof`** Quaternion

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `quat` | [`Quaternion`](Quaternion.md) | 目标四元数 |
| `dst?` | [`Quaternion`](Quaternion.md) | - |

#### Returns

[`Quaternion`](Quaternion.md)

计算结果


### toAxisUnit

▸ **toAxisUnit**(): [`Vector3`](Vector3.md)

对[1,1,1]向量进行转换。

#### Returns

[`Vector3`](Vector3.md)


### toEulerAngles

▸ **toEulerAngles**(`dst?`): [`Vector3`](Vector3.md)

将该四元数转换成欧拉角，x代表Pitch,y代表Yaw,z代表Roll
旋转的顺序为YXZ

**`memberof`** Quaternion

#### Parameters

| Name | Type |
| --- | --- |
| `dst?` | [`Vector3`](Vector3.md) |

#### Returns

[`Vector3`](Vector3.md)

计算结果


### toPhysics

▸ **toPhysics**(): `RawQuaternion`

created by shanexyzhou
生成物理引擎内的RawQuaternion

#### Returns

`RawQuaternion`


### transformVector3

▸ **transformVector3**(`vec`): [`Vector3`](Vector3.md)

#### Parameters

| Name | Type |
| --- | --- |
| `vec` | [`Vector3`](Vector3.md) |

#### Returns

[`Vector3`](Vector3.md)


### clearPhysicsPool

▸ `Static` **clearPhysicsPool**(): `void`

#### Returns

`void`


### createFromArray

▸ `Static` **createFromArray**(`array`): [`Quaternion`](Quaternion.md)

使用一个数组创建
此操作会拷贝一份数组

**`static`**

**`memberof`** Quaternion

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `array` | `number`[] | 数据源，长度必须为4，否则会抛出异常 |

#### Returns

[`Quaternion`](Quaternion.md)


### createFromAxisAngle

▸ `Static` **createFromAxisAngle**(`axis`, `rad`, `dst?`): [`Quaternion`](Quaternion.md)

从轴向旋转创建

**`static`**

**`memberof`** Quaternion

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `axis` | [`Vector3`](Vector3.md) | 旋转轴 |
| `rad` | `number` | 旋转幅度 |
| `dst?` | [`Quaternion`](Quaternion.md) | - |

#### Returns

[`Quaternion`](Quaternion.md)

计算结果


### createFromMatrix4

▸ `Static` **createFromMatrix4**(`mat`, `dst?`): [`Quaternion`](Quaternion.md)

从旋转矩阵创建

**`static`**

**`memberof`** Quaternion

#### Parameters

| Name | Type |
| --- | --- |
| `mat` | [`Matrix4`](Matrix4.md) |
| `dst?` | [`Quaternion`](Quaternion.md) |

#### Returns

[`Quaternion`](Quaternion.md)


### createFromNumber

▸ `Static` **createFromNumber**(`x`, `y`, `z`, `w`): [`Quaternion`](Quaternion.md)

使用数值创建

**`static`**

**`memberof`** Quaternion

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `x` | `number` | x |
| `y` | `number` | y |
| `z` | `number` | z |
| `w` | `number` | w |

#### Returns

[`Quaternion`](Quaternion.md)

创建出来的四元数


### createFromTypedArray

▸ `Static` **createFromTypedArray**(`array`, `offset?`): [`Quaternion`](Quaternion.md)

使用某个已有的typedArray创建
此操作不会拷贝数据，而是在原来的内存区域上操作

**`static`**

**`memberof`** Quaternion

#### Parameters

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `array` | `Float32Array` | `undefined` | 数据源 |
| `offset` | `number` | `0` | - |

#### Returns

[`Quaternion`](Quaternion.md)


### createFromUnitVectors

▸ `Static` **createFromUnitVectors**(`vFrom`, `vTo`): [`Quaternion`](Quaternion.md)

通过俩个向量创建四元数

#### Parameters

| Name | Type |
| --- | --- |
| `vFrom` | [`Vector3`](Vector3.md) |
| `vTo` | [`Vector3`](Vector3.md) |

#### Returns

[`Quaternion`](Quaternion.md)


### fromEulerAngles

▸ `Static` **fromEulerAngles**(`euler`, `dst?`): [`Quaternion`](Quaternion.md)

从欧拉角创建四元数

**`static`**

**`memberof`** Quaternion

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `euler` | [`Vector3`](Vector3.md) | 欧拉角，x代表pitch，y代表yaw，z代表roll |
| `dst?` | [`Quaternion`](Quaternion.md) | - |

#### Returns

[`Quaternion`](Quaternion.md)


### fromPhysics

▸ `Static` **fromPhysics**(`v`): [`Quaternion`](Quaternion.md)

created by shanexyzhou
从物理引擎内的RawQuaternion生成Quaternion

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `RawQuaternion` |

#### Returns

[`Quaternion`](Quaternion.md)


### lookRotation

▸ `Static` **lookRotation**(`forward`, `up`, `dst?`): [`Quaternion`](Quaternion.md)

由视角方向创建四元数

**`static`**

**`memberof`** Quaternion

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `forward` | [`Vector3`](Vector3.md) | 前方向 |
| `up` | [`Vector3`](Vector3.md) | 上方向 |
| `dst?` | [`Quaternion`](Quaternion.md) | - |

#### Returns

[`Quaternion`](Quaternion.md)

计算结果
