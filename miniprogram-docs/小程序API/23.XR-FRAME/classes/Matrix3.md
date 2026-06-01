# Class: Matrix3

> 官方文档：[Class: Matrix3](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Matrix3.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Matrix3
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Matrix3

## Table of contents

### Constructors

- [constructor](Matrix3.md)

### Accessors

- [raw](Matrix3.md)
- [IDENTITY](Matrix3.md)

### Methods

- [inverse](Matrix3.md)
- [multiply](Matrix3.md)
- [rotate](Matrix3.md)
- [scale](Matrix3.md)
- [setArray](Matrix3.md)
- [toArray](Matrix3.md)
- [transformPoint](Matrix3.md)
- [translate](Matrix3.md)
- [createFromArray](Matrix3.md)
- [createFromTypedArray](Matrix3.md)

## Constructors

### constructor

• **new Matrix3**(`raw?`, `offset?`)

#### Parameters

| Name | Type |
| --- | --- |
| `raw?` | `Float32Array` |
| `offset?` | `number` |

## Accessors

### raw

• `get` **raw**(): `Float32Array`

#### Returns

`Float32Array`


### IDENTITY

• `Static` `get` **IDENTITY**(): [`Matrix3`](Matrix3.md)

单位矩阵

**`readonly`**

**`static`**

**`memberof`** Matrix3

#### Returns

[`Matrix3`](Matrix3.md)

单位矩阵，每次返回都会创建新的对象

## Methods

### inverse

▸ **inverse**(`dst?`): [`Matrix3`](Matrix3.md)

求该矩阵的逆

**`memberof`** Matrix3

#### Parameters

| Name | Type |
| --- | --- |
| `dst?` | [`Matrix3`](Matrix3.md) |

#### Returns

[`Matrix3`](Matrix3.md)

计算结果


### multiply

▸ **multiply**(`m`, `dst?`): [`Matrix3`](Matrix3.md)

将该矩阵与另一个矩阵相乘

**`memberof`** Matrix3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `m` | [`Matrix3`](Matrix3.md) | 右乘矩阵 |
| `dst?` | [`Matrix3`](Matrix3.md) | - |

#### Returns

[`Matrix3`](Matrix3.md)

计算结果


### rotate

▸ **rotate**(`radians`, `dst?`): [`Matrix3`](Matrix3.md)

将该矩阵进行旋转变换

**`memberof`** Matrix3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `radians` | `number` | 旋转幅度，用弧度表示 |
| `dst?` | [`Matrix3`](Matrix3.md) | - |

#### Returns

[`Matrix3`](Matrix3.md)

计算结果


### scale

▸ **scale**(`sx`, `sy`, `dst?`): [`Matrix3`](Matrix3.md)

将该矩阵进行缩放变换

**`memberof`** Matrix3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `sx` | `number` | x轴缩放 |
| `sy` | `number` | y轴缩放 |
| `dst?` | [`Matrix3`](Matrix3.md) | - |

#### Returns

[`Matrix3`](Matrix3.md)

计算结果


### setArray

▸ **setArray**(`value`, `offset?`): [`Matrix3`](Matrix3.md)

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `ArrayLike`<`number`> |
| `offset?` | `number` |

#### Returns

[`Matrix3`](Matrix3.md)


### toArray

▸ **toArray**(): `number`[]

返回矩阵数据

**`memberof`** Matrix3

#### Returns

`number`[]

矩阵数据，以JSArray返回


### transformPoint

▸ **transformPoint**(`v`, `dst?`): [`Vector2`](Vector2.md)

矩阵变换作用于点

**`memberof`** Matrix3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `v` | [`Vector2`](Vector2.md) | 点 |
| `dst?` | [`Vector2`](Vector2.md) | - |

#### Returns

[`Vector2`](Vector2.md)

计算结果


### translate

▸ **translate**(`tx`, `ty`, `dst?`): [`Matrix3`](Matrix3.md)

将该矩阵进行位移变换

**`memberof`** Matrix3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `tx` | `number` | x轴位移 |
| `ty` | `number` | y轴位移 |
| `dst?` | [`Matrix3`](Matrix3.md) | - |

#### Returns

[`Matrix3`](Matrix3.md)

计算结果


### createFromArray

▸ `Static` **createFromArray**(`array`): [`Matrix3`](Matrix3.md)

使用一个数组创建
此操作会拷贝一份数组

**`static`**

**`memberof`** Matrix3

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `array` | `number`[] | 数据源，长度必须为9，否则会抛出异常 |

#### Returns

[`Matrix3`](Matrix3.md)

创建出来的矩阵


### createFromTypedArray

▸ `Static` **createFromTypedArray**(`array`, `offset?`): [`Matrix3`](Matrix3.md)

使用某个已有的typedArray创建
此操作不会拷贝数据，而是在原来的内存区域上操作

**`static`**

**`memberof`** Matrix3

#### Parameters

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `array` | `Float32Array` | `undefined` | 数据源 |
| `offset` | `number` | `0` | - |

#### Returns

[`Matrix3`](Matrix3.md)

创建出来的矩阵
