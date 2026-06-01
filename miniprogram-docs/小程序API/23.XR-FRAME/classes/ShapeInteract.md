# Class: ShapeInteract

> 官方文档：[Class: ShapeInteract](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/ShapeInteract.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / ShapeInteract
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / ShapeInteract

拥有ShapeInterace组件的Shape才能与其他Shape发生交互。
将`collide`属性设置为true来与其他Shape进行物理碰撞，仅当两个Shape的collide属性**都为true**时它们才能发生碰撞。

## Hierarchy

- [`Component`](Component.md)<[`IShapeInteractData`](../interfaces/IShapeInteractData.md)> ↳ **`ShapeInteract`**

## Table of contents

### Constructors

- [constructor](ShapeInteract.md)

### Events

- [onAdd](ShapeInteract.md)
- [onRelease](ShapeInteract.md)
- [onRemove](ShapeInteract.md)
- [onTick](ShapeInteract.md)
- [onUpdate](ShapeInteract.md)

### Properties

- [priority](ShapeInteract.md)
- [schema](ShapeInteract.md)
- [EVENTS](ShapeInteract.md)

### Accessors

- [bounceCombine](ShapeInteract.md)
- [bounciness](ShapeInteract.md)
- [dynamicFriction](ShapeInteract.md)
- [el](ShapeInteract.md)
- [frictionCombine](ShapeInteract.md)
- [scene](ShapeInteract.md)
- [staticFriction](ShapeInteract.md)
- [version](ShapeInteract.md)

### Methods

- [getData](ShapeInteract.md)
- [getInteractType](ShapeInteract.md)
- [setData](ShapeInteract.md)
- [setDataOne](ShapeInteract.md)

## Constructors

### constructor

• **new ShapeInteract**()

#### Overrides

[Component](Component.md).[constructor](Component.md)

## Events

### onAdd

▸ **onAdd**(`parent`, `data`): `void`

所挂载的`element`被挂载到场景时触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `parent` | [`Element`](Element.md) |
| `data` | [`IShapeInteractData`](../interfaces/IShapeInteractData.md) |

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
| `data` | [`IShapeInteractData`](../interfaces/IShapeInteractData.md) |

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
| `data` | [`IShapeInteractData`](../interfaces/IShapeInteractData.md) |

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
| `data` | [`IShapeInteractData`](../interfaces/IShapeInteractData.md) | - |

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
| `data` | [`IShapeInteractData`](../interfaces/IShapeInteractData.md) |
| `preData` | [`IShapeInteractData`](../interfaces/IShapeInteractData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onUpdate](Component.md)

## Properties

### priority

• `Readonly` **priority**: `number`

自定义组件的更新优先级。

#### Inherited from

[Component](Component.md).[priority](Component.md)


### schema

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md)

自定义组件的`schema`。

#### Overrides

[Component](Component.md).[schema](Component.md)


### EVENTS

▪ `Static` **EVENTS**: `string`[] = `[]`

#### Inherited from

[Component](Component.md).[EVENTS](Component.md)

## Accessors

### bounceCombine

• `get` **bounceCombine**(): `CombineMode`

如何结合发生碰撞的两个物体的弹性系数。

**`default`** {@link CombineMode.Average}

#### Returns

`CombineMode`

• `set` **bounceCombine**(`v`): `void`

如何结合发生碰撞的两个物体的弹性系数。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `CombineMode` |

#### Returns

`void`


### bounciness

• `get` **bounciness**(): `number`

弹性系数，决定碰撞时的能量损失比例。

弹性系数 = 1时，碰撞无能量损失。

**`limit`** 0 <= bounciness <= 1

**`default`** 0

#### Returns

`number`

• `set` **bounciness**(): `void`

弹性系数，决定碰撞时的能量损失比例。

弹性系数 = 1时，碰撞无能量损失。

#### Returns

`void`


### dynamicFriction

• `get` **dynamicFriction**(): `number`

动摩擦系数。

**`limit`** 0 <= dynamicFriction <= 1

**`default`** 0.6

#### Returns

`number`

• `set` **dynamicFriction**(): `void`

动摩擦系数。

#### Returns

`void`


### el

• `get` **el**(): [`Element`](Element.md)

挂载的元素。

#### Returns

[`Element`](Element.md)


### frictionCombine

• `get` **frictionCombine**(): `CombineMode`

如何结合发生碰撞的两个物体的摩擦系数。

**`default`** {@link CombineMode.Average}

#### Returns

`CombineMode`

• `set` **frictionCombine**(`v`): `void`

如何结合发生碰撞的两个物体的摩擦系数。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `CombineMode` |

#### Returns

`void`


### scene

• `get` **scene**(): [`Scene`](Scene.md)

当前场景。

#### Returns

[`Scene`](Scene.md)


### staticFriction

• `get` **staticFriction**(): `number`

静摩擦系数

**`limit`** 0 <= staticFriction <= 1

**`default`** 0.6

#### Returns

`number`

• `set` **staticFriction**(): `void`

静摩擦系数

#### Returns

`void`


### version

• `get` **version**(): `number`

当前版本，每次有数据更新都会增加，可以用作和其他组件合作的依据。

#### Returns

`number`

## Methods

### getData

▸ **getData**<`T`>(`key`): [`IShapeInteractData`](../interfaces/IShapeInteractData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeInteractData`](../interfaces/IShapeInteractData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`IShapeInteractData`](../interfaces/IShapeInteractData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### getInteractType

▸ **getInteractType**(): `EShapeInteractType`

#### Returns

`EShapeInteractType`


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IShapeInteractData`](../interfaces/IShapeInteractData.md)> |

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
| `T` | extends keyof [`IShapeInteractData`](../interfaces/IShapeInteractData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IShapeInteractData`](../interfaces/IShapeInteractData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
