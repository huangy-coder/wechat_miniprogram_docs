# Class: Component<IData>

> 官方文档：[Class: Component<IData>](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Component.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Component
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Component

组件，系统核心之一。

组件就是`wxml`的标签上写的那些`attribute`，比如`<xr-element transform="position: 1 1 1" />`中，`transform`就是一个组件，`position`是它的一个属性。
这些属性可以在`schema`中被定义，变化时会触发对应的生命周期。
自定义组件最后使用[registerComponent](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#registerComponent)，组件的属性可以使用代理规则来简化，比如以上的标签可以简化为`<xr-element position="1 1 1" />`，详见[Element](Element.md)。

## Type parameters

| Name | Description |
| --- | --- |
| `IData` | 组件数据的类型，应当和`schema`中一致，用于TS类型推断。 |

## Hierarchy

- **`Component`** ↳ [`Transform`](Transform.md) ↳ [`AssetLoad`](AssetLoad.md) ↳ [`Assets`](Assets.md) ↳ [`Camera`](Camera.md) ↳ [`GLTF`](GLTF.md) ↳ [`Light`](Light.md) ↳ [`AssetMaterial`](AssetMaterial.md) ↳ [`Mesh`](Mesh.md) ↳ [`Text`](Text.md) ↳ [`AssetRenderTexture`](AssetRenderTexture.md) ↳ [`Env`](Env.md) ↳ [`Animator`](Animator.md) ↳ [`CameraOrbitControl`](CameraOrbitControl.md) ↳ [`ARTracker`](ARTracker.md) ↳ [`Shape`](Shape.md) ↳ [`Rigidbody`](Rigidbody.md) ↳ [`ShapeInteract`](ShapeInteract.md) ↳ [`ShapeGizmos`](ShapeGizmos.md) ↳ [`AssetPostProcess`](AssetPostProcess.md) ↳ [`AssetsSystem`](AssetsSystem.md) ↳ [`NodeSystem`](NodeSystem.md) ↳ [`TickSystem`](TickSystem.md) ↳ [`AnimationSystem`](AnimationSystem.md) ↳ [`VideoSystem`](VideoSystem.md) ↳ [`RenderSystem`](RenderSystem.md) ↳ [`PhysicsSystem`](PhysicsSystem.md) ↳ [`ARSystem`](ARSystem.md) ↳ [`ShareSystem`](ShareSystem.md) ↳ [`GizmoSystem`](GizmoSystem.md)

## Table of contents

### Constructors

- [constructor](Component.md)

### Events

- [onAdd](Component.md)
- [onRelease](Component.md)
- [onRemove](Component.md)
- [onTick](Component.md)
- [onUpdate](Component.md)

### Properties

- [priority](Component.md)
- [schema](Component.md)
- [EVENTS](Component.md)

### Accessors

- [el](Component.md)
- [scene](Component.md)
- [version](Component.md)

### Methods

- [getData](Component.md)
- [setData](Component.md)
- [setDataOne](Component.md)

## Constructors

### constructor

• **new Component**<`IData`>()

#### Type parameters

| Name |
| --- |
| `IData` |

## Events

### onAdd

▸ **onAdd**(`parent`, `data`): `void`

所挂载的`element`被挂载到场景时触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `parent` | [`Element`](Element.md) |
| `data` | `IData` |

#### Returns

`void`


### onRelease

▸ **onRelease**(`data`): `void`

从被挂载的`element`上被移除，或是`element`被销毁时，触发的回调。
一般用于释放持有的资源。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `IData` |

#### Returns

`void`


### onRemove

▸ **onRemove**(`parent`, `data`): `void`

所挂载的`element`从父节点`parent`被移除时，或者自己从`element`上被移除时，触发的回调。
一般用于消除功能的运作。
**如果一个组件的元素直接被销毁了，那这个组件就不会经历onRemove而是直接进入onRelease。**

#### Parameters

| Name | Type |
| --- | --- |
| `parent` | [`Element`](Element.md) |
| `data` | `IData` |

#### Returns

`void`


### onTick

▸ **onTick**(`deltaTime`, `data`): `void`

渲染每帧触发的回调。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `deltaTime` | `number` | 单位为毫秒(ms)。 |
| `data` | `IData` | - |

#### Returns

`void`


### onUpdate

▸ **onUpdate**(`data`, `preData`): `void`

数据更新时触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `IData` |
| `preData` | `IData` |

#### Returns

`void`

## Properties

### priority

• `Readonly` **priority**: `number`

自定义组件的更新优先级。


### schema

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md) = `{}`

自定义组件的`schema`。


### EVENTS

▪ `Static` **EVENTS**: `string`[] = `[]`

## Accessors

### el

• `get` **el**(): [`Element`](Element.md)

挂载的元素。

#### Returns

[`Element`](Element.md)


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

▸ **getData**<`T`>(`key`): `IData`[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends `string` \| `number` \| `symbol` |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

`IData`[`T`]


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<`IData`> |

#### Returns

`void`


### setDataOne

▸ **setDataOne**<`T`>(`key`, `value`): `void`

设置一个数据。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends `string` \| `number` \| `symbol` |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | `IData`[`T`] |

#### Returns

`void`
