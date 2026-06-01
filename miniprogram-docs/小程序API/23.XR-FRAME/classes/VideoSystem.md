# Class: VideoSystem

> 官方文档：[Class: VideoSystem](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/VideoSystem.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / VideoSystem
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / VideoSystem

视频系统，负责整个场景视频的管理。

## Hierarchy

- [`Component`](Component.md)<[`IVideoSystemData`](../interfaces/IVideoSystemData.md)> ↳ **`VideoSystem`**

## Table of contents

### Constructors

- [constructor](VideoSystem.md)

### Events

- [onAdd](VideoSystem.md)
- [onRelease](VideoSystem.md)
- [onRemove](VideoSystem.md)
- [onTick](VideoSystem.md)
- [onUpdate](VideoSystem.md)

### Properties

- [priority](VideoSystem.md)
- [schema](VideoSystem.md)
- [EVENTS](VideoSystem.md)

### Accessors

- [el](VideoSystem.md)
- [scene](VideoSystem.md)
- [version](VideoSystem.md)

### Methods

- [getData](VideoSystem.md)
- [setData](VideoSystem.md)
- [setDataOne](VideoSystem.md)

## Constructors

### constructor

• **new VideoSystem**()

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
| `data` | [`IVideoSystemData`](../interfaces/IVideoSystemData.md) |

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
| `data` | [`IVideoSystemData`](../interfaces/IVideoSystemData.md) |

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
| `data` | [`IVideoSystemData`](../interfaces/IVideoSystemData.md) |

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
| `data` | [`IVideoSystemData`](../interfaces/IVideoSystemData.md) |

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
| `data` | [`IVideoSystemData`](../interfaces/IVideoSystemData.md) |
| `preData` | [`IVideoSystemData`](../interfaces/IVideoSystemData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onUpdate](Component.md)

## Properties

### priority

• `Readonly` **priority**: `number` = `110`

自定义组件的更新优先级。

#### Overrides

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

▸ **getData**<`T`>(`key`): [`IVideoSystemData`](../interfaces/IVideoSystemData.md)[`T`]

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

[`IVideoSystemData`](../interfaces/IVideoSystemData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IVideoSystemData`](../interfaces/IVideoSystemData.md)> |

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
| `value` | [`IVideoSystemData`](../interfaces/IVideoSystemData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
