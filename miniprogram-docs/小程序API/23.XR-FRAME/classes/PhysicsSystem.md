# Class: PhysicsSystem

> 官方文档：[Class: PhysicsSystem](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/PhysicsSystem.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / PhysicsSystem
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / PhysicsSystem

物理系统，管理着场景中的所有[轮廓](Shape.md)和[刚体](Rigidbody.md)。

## Hierarchy

- [`Component`](Component.md)<[`IPhysicsSystemData`](../interfaces/IPhysicsSystemData.md)> ↳ **`PhysicsSystem`**

## Table of contents

### Constructors

- [constructor](PhysicsSystem.md)

### Events

- [onAdd](PhysicsSystem.md)
- [onRelease](PhysicsSystem.md)
- [onRemove](PhysicsSystem.md)
- [onTick](PhysicsSystem.md)
- [onUpdate](PhysicsSystem.md)

### Properties

- [enableSimulation](PhysicsSystem.md)
- [fixedDeltaTime](PhysicsSystem.md)
- [maxPhysicsDeltaTime](PhysicsSystem.md)
- [priority](PhysicsSystem.md)
- [schema](PhysicsSystem.md)
- [EVENTS](PhysicsSystem.md)

### Accessors

- [el](PhysicsSystem.md)
- [gravity](PhysicsSystem.md)
- [scene](PhysicsSystem.md)
- [version](PhysicsSystem.md)

### Methods

- [getData](PhysicsSystem.md)
- [ignoreLayerCollision](PhysicsSystem.md)
- [raycast](PhysicsSystem.md)
- [setData](PhysicsSystem.md)
- [setDataOne](PhysicsSystem.md)

## Constructors

### constructor

• **new PhysicsSystem**()

#### Overrides

[Component](Component.md).[constructor](Component.md)

## Events

### onAdd

▸ **onAdd**(): `void`

所挂载的`element`被挂载到场景时触发的回调。

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
| `data` | [`IPhysicsSystemData`](../interfaces/IPhysicsSystemData.md) |

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
| `data` | [`IPhysicsSystemData`](../interfaces/IPhysicsSystemData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onRemove](Component.md)


### onTick

• **onTick**:

#### Inherited from

[Component](Component.md).[onTick](Component.md)


### onUpdate

▸ **onUpdate**(`data`, `preData`): `void`

数据更新时触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | [`IPhysicsSystemData`](../interfaces/IPhysicsSystemData.md) |
| `preData` | [`IPhysicsSystemData`](../interfaces/IPhysicsSystemData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onUpdate](Component.md)

## Properties

### enableSimulation

• **enableSimulation**: `boolean` = `false`

是否进行物理模拟。


### fixedDeltaTime

• **fixedDeltaTime**: `number` = `0.02`


### maxPhysicsDeltaTime

• **maxPhysicsDeltaTime**: `number` = `0.1`


### priority

• `Readonly` **priority**: `number`

自定义组件的更新优先级。

#### Inherited from

[Component](Component.md).[priority](Component.md)


### schema

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md) = `{}`

自定义组件的`schema`。

#### Inherited from

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


### gravity

• `get` **gravity**(): [`Vector3`](Vector3.md)

全局重力。

**`default`** [0, -9.8, 0]

#### Returns

[`Vector3`](Vector3.md)

• `set` **gravity**(`v`): `void`

全局重力。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](Vector3.md) |

#### Returns

`void`


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

▸ **getData**<`T`>(`key`): [`IPhysicsSystemData`](../interfaces/IPhysicsSystemData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends `never` |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`IPhysicsSystemData`](../interfaces/IPhysicsSystemData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### ignoreLayerCollision

▸ **ignoreLayerCollision**(`layer1`, `layer2`, `ignore?`): `void`

设定某一对layer之间是否会发生碰撞。

#### Parameters

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `layer1` | `number` | `undefined` | - |
| `layer2` | `number` | `undefined` | - |
| `ignore` | `boolean` | `true` | `true`表示**不**碰撞。 |

#### Returns

`void`


### raycast

▸ **raycast**(`desc`): `boolean`

射线检测，判断给定射线是否与至少一个轮廓相交，并返回与**最近**的那个轮廓相交的信息。
返回的信息记录在desc.hit里，需要事先创建一个RaycastHit对象来负责接收。

#### Parameters

| Name | Type |
| --- | --- |
| `desc` | [`RaycastDesc`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#RaycastDesc) |

#### Returns

`boolean`


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IPhysicsSystemData`](../interfaces/IPhysicsSystemData.md)> |

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
| `T` | extends `never` |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IPhysicsSystemData`](../interfaces/IPhysicsSystemData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
