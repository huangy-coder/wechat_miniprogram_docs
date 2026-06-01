# Class: RenderSystem

> 官方文档：[Class: RenderSystem](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/RenderSystem.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / RenderSystem
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / RenderSystem

渲染系统，负责整个场景渲染的管理。

## Hierarchy

- [`Component`](Component.md)<[`IRenderSystemData`](../interfaces/IRenderSystemData.md)> ↳ **`RenderSystem`**

## Table of contents

### Constructors

- [constructor](RenderSystem.md)

### Events

- [onAdd](RenderSystem.md)
- [onRelease](RenderSystem.md)
- [onRemove](RenderSystem.md)
- [onTick](RenderSystem.md)
- [onUpdate](RenderSystem.md)

### Properties

- [priority](RenderSystem.md)
- [schema](RenderSystem.md)
- [EVENTS](RenderSystem.md)

### Accessors

- [el](RenderSystem.md)
- [renderGraph](RenderSystem.md)
- [scene](RenderSystem.md)
- [shadowColor](RenderSystem.md)
- [version](RenderSystem.md)

### Methods

- [changeFeatures](RenderSystem.md)
- [changeMacros](RenderSystem.md)
- [disableInstance](RenderSystem.md)
- [enableInstance](RenderSystem.md)
- [getData](RenderSystem.md)
- [getFeature](RenderSystem.md)
- [getMacro](RenderSystem.md)
- [setData](RenderSystem.md)
- [setDataOne](RenderSystem.md)
- [useRenderGraph](RenderSystem.md)

## Constructors

### constructor

• **new RenderSystem**()

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
| `data` | [`IRenderSystemData`](../interfaces/IRenderSystemData.md) |

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
| `data` | [`IRenderSystemData`](../interfaces/IRenderSystemData.md) |

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
| `data` | [`IRenderSystemData`](../interfaces/IRenderSystemData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onRemove](Component.md)


### onTick

▸ **onTick**(): `void`

渲染每帧触发的回调。

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
| `data` | [`IRenderSystemData`](../interfaces/IRenderSystemData.md) |
| `preData` | [`IRenderSystemData`](../interfaces/IRenderSystemData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onUpdate](Component.md)

## Properties

### priority

• `Readonly` **priority**: `number` = `400`

自定义组件的更新优先级。

#### Overrides

[Component](Component.md).[priority](Component.md)


### schema

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md)

详见[RenderSystemSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#RenderSystemSchema)。

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


### renderGraph

• `get` **renderGraph**(): `default`<`any`>

当前正在使用的RenderGraph。

#### Returns

`default`<`any`>


### scene

• `get` **scene**(): [`Scene`](Scene.md)

当前场景。

#### Returns

[`Scene`](Scene.md)


### shadowColor

• `get` **shadowColor**(): `number`[]

#### Returns

`number`[]


### version

• `get` **version**(): `number`

当前版本，每次有数据更新都会增加，可以用作和其他组件合作的依据。

#### Returns

`number`

## Methods

### changeFeatures

▸ **changeFeatures**(`features`): `void`

修改全局渲染特性。

#### Parameters

| Name | Type |
| --- | --- |
| `features` | `Object` |

#### Returns

`void`


### changeMacros

▸ **changeMacros**(`macros`): `void`

修改全局宏信息。

#### Parameters

| Name | Type |
| --- | --- |
| `macros` | `Object` |

#### Returns

`void`


### disableInstance

▸ **disableInstance**(): `void`

关闭全局GPU实例化。

#### Returns

`void`


### enableInstance

▸ **enableInstance**(): `void`

开启全局GPU实例化。

#### Returns

`void`


### getData

▸ **getData**<`T`>(`key`): [`IRenderSystemData`](../interfaces/IRenderSystemData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IRenderSystemData`](../interfaces/IRenderSystemData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`IRenderSystemData`](../interfaces/IRenderSystemData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### getFeature

▸ **getFeature**(`key`): `string` | `number` | `boolean`

获取全局渲染特性。

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |

#### Returns

`string` | `number` | `boolean`


### getMacro

▸ **getMacro**(`key`): `string` | `number` | `boolean`

获取全局宏信息。

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |

#### Returns

`string` | `number` | `boolean`


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IRenderSystemData`](../interfaces/IRenderSystemData.md)> |

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
| `T` | extends keyof [`IRenderSystemData`](../interfaces/IRenderSystemData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IRenderSystemData`](../interfaces/IRenderSystemData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)


### useRenderGraph

▸ **useRenderGraph**(`rg`): `void`

使用某个RenderGraph，默认会使用内置的`ForwardBaseRG`。

#### Parameters

| Name | Type |
| --- | --- |
| `rg` | `default`<`any`> |

#### Returns

`void`
