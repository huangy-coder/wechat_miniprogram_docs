# Class: Mesh

> 官方文档：[Class: Mesh](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Mesh.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Mesh
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Mesh

Mesh组件，整合[Geometry](Geometry.md)和[Material](Material.md)进行渲染，一般被代理到[XRMesh](XRMesh.md)元素。

## Hierarchy

- [`Component`](Component.md)<[`IMeshData`](../interfaces/IMeshData.md)> ↳ **`Mesh`**

## Table of contents

### Constructors

- [constructor](Mesh.md)

### Events

- [onAdd](Mesh.md)
- [onRelease](Mesh.md)
- [onRemove](Mesh.md)
- [onTick](Mesh.md)
- [onUpdate](Mesh.md)

### Properties

- [priority](Mesh.md)
- [schema](Mesh.md)
- [EVENTS](Mesh.md)

### Accessors

- [el](Mesh.md)
- [geometry](Mesh.md)
- [material](Mesh.md)
- [morphWeights](Mesh.md)
- [scene](Mesh.md)
- [version](Mesh.md)

### Methods

- [getData](Mesh.md)
- [setData](Mesh.md)
- [setDataOne](Mesh.md)

## Constructors

### constructor

• **new Mesh**()

#### Inherited from

[Component](Component.md).[constructor](Component.md)

## Events

### onAdd

▸ **onAdd**(`parent`, `data`): `void`

所挂载的`element`被挂载到场景时触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `parent` | [`Element`](Element.md) |
| `data` | [`IMeshData`](../interfaces/IMeshData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onAdd](Component.md)


### onRelease

▸ **onRelease**(`data`): `void`

从被挂载的`element`上被移除，或是`element`被销毁时，触发的回调。
一般用于释放持有的资源。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | [`IMeshData`](../interfaces/IMeshData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onRelease](Component.md)


### onRemove

▸ **onRemove**(`parent`, `data`): `void`

所挂载的`element`从父节点`parent`被移除时，或者自己从`element`上被移除时，触发的回调。
一般用于消除功能的运作。
**如果一个组件的元素直接被销毁了，那这个组件就不会经历onRemove而是直接进入onRelease。**

#### Parameters

| Name | Type |
| --- | --- |
| `parent` | [`Element`](Element.md) |
| `data` | [`IMeshData`](../interfaces/IMeshData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onRemove](Component.md)


### onTick

▸ **onTick**(`deltaTime`, `data`): `void`

渲染每帧触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `deltaTime` | `number` |
| `data` | [`IMeshData`](../interfaces/IMeshData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onTick](Component.md)


### onUpdate

▸ **onUpdate**(`data`, `preData`): `void`

数据更新时触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | [`IMeshData`](../interfaces/IMeshData.md) |
| `preData` | [`IMeshData`](../interfaces/IMeshData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onUpdate](Component.md)

## Properties

### priority

• `Readonly` **priority**: `number` = `300`

自定义组件的更新优先级。

#### Overrides

[Component](Component.md).[priority](Component.md)


### schema

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md)

详见[MeshSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#MeshSchema)。

#### Overrides

[Component](Component.md).[schema](Component.md)


### EVENTS

▪ `Static` **EVENTS**: `string`[] = `[]`

#### Inherited from

[Component](Component.md).[EVENTS](Component.md)

## Accessors

### el

• `get` **el**(): [`Element`](Element.md)

挂载的元素。

#### Returns

[`Element`](Element.md)


### geometry

• `get` **geometry**(): [`Geometry`](Geometry.md)

几何数据。

#### Returns

[`Geometry`](Geometry.md)


### material

• `get` **material**(): [`Material`](Material.md)

材质。

#### Returns

[`Material`](Material.md)

• `set` **material**(`value`): `void`

材质。

#### Parameters

| Name | Type |
| --- | --- |
| `value` | [`Material`](Material.md) |

#### Returns

`void`


### morphWeights

• `get` **morphWeights**(): `Float32Array`

MorphTargets的权重，最多32个，可以获取后直接修改。

#### Returns

`Float32Array`


### scene

• `get` **scene**(): [`Scene`](Scene.md)

当前场景。

#### Returns

[`Scene`](Scene.md)


### version

• `get` **version**(): `number`

当前版本，每次有数据更新都会增加，可以用作和其他组件合作的依据。

#### Returns

`number`

## Methods

### getData

▸ **getData**<`T`>(`key`): [`IMeshData`](../interfaces/IMeshData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IMeshData`](../interfaces/IMeshData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`IMeshData`](../interfaces/IMeshData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IMeshData`](../interfaces/IMeshData.md)> |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setData](Component.md)


### setDataOne

▸ **setDataOne**<`T`>(`key`, `value`): `void`

设置一个数据。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IMeshData`](../interfaces/IMeshData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IMeshData`](../interfaces/IMeshData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
