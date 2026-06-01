# Class: GLTF

> 官方文档：[Class: GLTF](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GLTF.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / GLTF
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / GLTF

将一个[GLTF模型](GLTFModel.md)实例化并渲染出来。
[xr-gltf](XRGLTF.md)标签会自动生成该组件。

> 会在当前元素下新建一系列子元素，作为GLTF模型的每个场景的根节点。
会在当前元素上新建[Animator](Animator.md)组件，并向其添加实例化生成的动画片段。

**`see`** [IGLTFData](../interfaces/IGLTFData.md)

## Hierarchy

- [`Component`](Component.md)<[`IGLTFData`](../interfaces/IGLTFData.md)> ↳ **`GLTF`**

## Table of contents

### Constructors

- [constructor](GLTF.md)

### Events

- [onAdd](GLTF.md)
- [onRelease](GLTF.md)
- [onRemove](GLTF.md)
- [onTick](GLTF.md)
- [onUpdate](GLTF.md)

### Properties

- [priority](GLTF.md)
- [schema](GLTF.md)
- [EVENTS](GLTF.md)

### Accessors

- [el](GLTF.md)
- [meshes](GLTF.md)
- [scene](GLTF.md)
- [version](GLTF.md)

### Methods

- [calcTotalBoundBox](GLTF.md)
- [getData](GLTF.md)
- [getInternalNodeByName](GLTF.md)
- [getPrimitivesByMeshName](GLTF.md)
- [getPrimitivesByNodeName](GLTF.md)
- [setData](GLTF.md)
- [setDataOne](GLTF.md)

## Constructors

### constructor

• **new GLTF**()

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
| `data` | [`IGLTFData`](../interfaces/IGLTFData.md) |

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
| `data` | [`IGLTFData`](../interfaces/IGLTFData.md) |

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
| `data` | [`IGLTFData`](../interfaces/IGLTFData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onRemove](Component.md)


### onTick

▸ **onTick**(`deltaTime`, `data`): `void`

渲染每帧触发的回调。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | [`IGLTFData`](../interfaces/IGLTFData.md) | - |

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
| `data` | [`IGLTFData`](../interfaces/IGLTFData.md) |
| `preData` | [`IGLTFData`](../interfaces/IGLTFData.md) |

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

自定义组件的`schema`。

#### Overrides

[Component](Component.md).[schema](Component.md)


### EVENTS

▪ `Static` **EVENTS**: `string`[]

#### Overrides

[Component](Component.md).[EVENTS](Component.md)

## Accessors

### el

• `get` **el**(): [`Element`](Element.md)

挂载的元素。

#### Returns

[`Element`](Element.md)


### meshes

• `get` **meshes**(): [`Mesh`](Mesh.md)[]

获取GLTF模型实例化过程中生成的所有[Mesh](Mesh.md)组件。

#### Returns

[`Mesh`](Mesh.md)[]


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

### calcTotalBoundBox

▸ **calcTotalBoundBox**(): [`BoundBox`](BoundBox.md)

计算GLTF模型整体的包围盒，返回**模型空间**内的计算结果。
每次调用都会重新计算。

#### Returns

[`BoundBox`](BoundBox.md)


### getData

▸ **getData**<`T`>(`key`): [`IGLTFData`](../interfaces/IGLTFData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IGLTFData`](../interfaces/IGLTFData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`IGLTFData`](../interfaces/IGLTFData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### getInternalNodeByName

▸ **getInternalNodeByName**(`name`): [`Element`](Element.md)

根据GLTF模型中节点的`name`字段来获取内部元素。

#### Parameters

| Name | Type |
| --- | --- |
| `name` | `string` |

#### Returns

[`Element`](Element.md)


### getPrimitivesByMeshName

▸ **getPrimitivesByMeshName**(`name`): { `nodeName`: `string` ; `primitives`: [`Mesh`](Mesh.md)[] }[]

根据GLTF模型中Mesh节点的`name`字段，来获取引用了该Mesh的**所有**Node节点下的所有Primitive。
在xr-frame实现中，每个引用了该Mesh的GLTFNode节点拥有**独立**的一份Primitives副本，**每个**Node节点下的**每个**Primitive对应一个`xr-frame Mesh组件`。
**如果没有引用了该Mesh的Node节点，会返回空数组。*

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | Mesh节点的`name` |

#### Returns

{ `nodeName`: `string` ; `primitives`: [`Mesh`](Mesh.md)[] }[]

一个数组，数组中的一个元素对应一个引用了该Mesh的GLTFNode节点，元素中nodeName为GLTFNode节点的`name`字段。


### getPrimitivesByNodeName

▸ **getPrimitivesByNodeName**(`name`): [`Mesh`](Mesh.md)[]

根据GLTF模型中**引用**了Mesh的**Node节点**的`name`字段，来获取对应Mesh下的所有Primitive。
一个GLTF模型中的Primitive节点对应返回中的一个`xr-frame Mesh组件`实例。
**如果没有该名字的节点，或者节点未引用Mesh，会返回空数组。*

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | Node节点的`name`（而非Mesh节点） |

#### Returns

[`Mesh`](Mesh.md)[]


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IGLTFData`](../interfaces/IGLTFData.md)> |

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
| `T` | extends keyof [`IGLTFData`](../interfaces/IGLTFData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IGLTFData`](../interfaces/IGLTFData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
