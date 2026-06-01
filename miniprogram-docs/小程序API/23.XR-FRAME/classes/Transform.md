# Class: Transform

> 官方文档：[Class: Transform](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Transform.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Transform
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Transform

3D变换组件，作为场景中3D节点的根基，一般被代理到[XRNode](XRNode.md)元素。

## Hierarchy

- [`Component`](Component.md)<[`ITransformData`](../interfaces/ITransformData.md)> ↳ **`Transform`**

## Table of contents

### Constructors

- [constructor](Transform.md)

### Events

- [onAdd](Transform.md)
- [onRelease](Transform.md)
- [onRemove](Transform.md)
- [onTick](Transform.md)
- [onUpdate](Transform.md)

### Properties

- [priority](Transform.md)
- [schema](Transform.md)
- [EVENTS](Transform.md)

### Accessors

- [el](Transform.md)
- [layer](Transform.md)
- [node](Transform.md)
- [position](Transform.md)
- [quaternion](Transform.md)
- [rotation](Transform.md)
- [scale](Transform.md)
- [scene](Transform.md)
- [version](Transform.md)
- [visible](Transform.md)
- [worldForward](Transform.md)
- [worldMatrix](Transform.md)
- [worldPosition](Transform.md)
- [worldQuaternion](Transform.md)
- [worldRight](Transform.md)
- [worldScale](Transform.md)
- [worldUp](Transform.md)

### Methods

- [getData](Transform.md)
- [setData](Transform.md)
- [setDataOne](Transform.md)
- [setLocalMatrix](Transform.md)

## Constructors

### constructor

• **new Transform**()

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
| `data` | [`ITransformData`](../interfaces/ITransformData.md) |

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
| `data` | [`ITransformData`](../interfaces/ITransformData.md) |

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
| `data` | [`ITransformData`](../interfaces/ITransformData.md) |

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
| `data` | [`ITransformData`](../interfaces/ITransformData.md) | - |

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
| `data` | [`ITransformData`](../interfaces/ITransformData.md) |
| `preData` | [`ITransformData`](../interfaces/ITransformData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onUpdate](Component.md)

## Properties

### priority

• `Readonly` **priority**: `number` = `100`

自定义组件的更新优先级。

#### Overrides

[Component](Component.md).[priority](Component.md)


### schema

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md)

详见[TransformSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TransformSchema)。

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


### layer

• `get` **layer**(): `number`

#### Returns

`number`

• `set` **layer**(`value`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `number` |

#### Returns

`void`


### node

• `get` **node**(): `default`

#### Returns

`default`


### position

• `get` **position**(): [`Vector3`](Vector3.md)

#### Returns

[`Vector3`](Vector3.md)


### quaternion

• `get` **quaternion**(): [`Quaternion`](Quaternion.md)

#### Returns

[`Quaternion`](Quaternion.md)


### rotation

• `get` **rotation**(): [`Vector3`](Vector3.md)

注意如果这里直接修改，使用**弧度**。

#### Returns

[`Vector3`](Vector3.md)


### scale

• `get` **scale**(): [`Vector3`](Vector3.md)

#### Returns

[`Vector3`](Vector3.md)


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


### visible

• `get` **visible**(): `boolean`

#### Returns

`boolean`

• `set` **visible**(`value`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `boolean` |

#### Returns

`void`


### worldForward

• `get` **worldForward**(): [`Vector3`](Vector3.md)

获取世界前向向量，**注意不可修改**。

#### Returns

[`Vector3`](Vector3.md)


### worldMatrix

• `get` **worldMatrix**(): [`Matrix4`](Matrix4.md)

获取世界矩阵，**注意不可修改**。

#### Returns

[`Matrix4`](Matrix4.md)


### worldPosition

• `get` **worldPosition**(): [`Vector3`](Vector3.md)

获取世界绝对位移，**注意不可修改**。

#### Returns

[`Vector3`](Vector3.md)


### worldQuaternion

• `get` **worldQuaternion**(): [`Quaternion`](Quaternion.md)

获取世界绝对旋转，**注意不可修改**。

#### Returns

[`Quaternion`](Quaternion.md)


### worldRight

• `get` **worldRight**(): [`Vector3`](Vector3.md)

获取世界右向向量，**注意不可修改**。

#### Returns

[`Vector3`](Vector3.md)


### worldScale

• `get` **worldScale**(): [`Vector3`](Vector3.md)

获取世界绝对缩放，**注意不可修改**。

#### Returns

[`Vector3`](Vector3.md)


### worldUp

• `get` **worldUp**(): [`Vector3`](Vector3.md)

获取世界上向向量，**注意不可修改**。

#### Returns

[`Vector3`](Vector3.md)

## Methods

### getData

▸ **getData**<`T`>(`key`): [`ITransformData`](../interfaces/ITransformData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ITransformData`](../interfaces/ITransformData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`ITransformData`](../interfaces/ITransformData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`ITransformData`](../interfaces/ITransformData.md)> |

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
| `T` | extends keyof [`ITransformData`](../interfaces/ITransformData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`ITransformData`](../interfaces/ITransformData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)


### setLocalMatrix

▸ **setLocalMatrix**(`mat`): `void`

直接设置本地矩阵。

#### Parameters

| Name | Type |
| --- | --- |
| `mat` | [`Matrix4`](Matrix4.md) |

#### Returns

`void`
