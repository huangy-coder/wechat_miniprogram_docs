# Class: AssetsSystem

> 官方文档：[Class: AssetsSystem](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AssetsSystem.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / AssetsSystem
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / AssetsSystem

资源系统，负责整个场景的资源管理。

一般不需要手动管理，而是利用[AssetLoad](AssetLoad.md)、[registerGeometry](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#registerGeometry)之类的使用。

## Hierarchy

- [`Component`](Component.md)<[`IAssetsSystemData`](../interfaces/IAssetsSystemData.md)> ↳ **`AssetsSystem`**

## Table of contents

### Constructors

- [constructor](AssetsSystem.md)

### Events

- [onAdd](AssetsSystem.md)
- [onRelease](AssetsSystem.md)
- [onRemove](AssetsSystem.md)
- [onTick](AssetsSystem.md)
- [onUpdate](AssetsSystem.md)

### Properties

- [priority](AssetsSystem.md)
- [schema](AssetsSystem.md)
- [EVENTS](AssetsSystem.md)

### Accessors

- [el](AssetsSystem.md)
- [scene](AssetsSystem.md)
- [version](AssetsSystem.md)

### Methods

- [addAsset](AssetsSystem.md)
- [cancelAsset](AssetsSystem.md)
- [getAsset](AssetsSystem.md)
- [getAssetWithState](AssetsSystem.md)
- [getData](AssetsSystem.md)
- [loadAsset](AssetsSystem.md)
- [releaseAsset](AssetsSystem.md)
- [setData](AssetsSystem.md)
- [setDataOne](AssetsSystem.md)

## Constructors

### constructor

• **new AssetsSystem**()

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
| `data` | [`IAssetsSystemData`](../interfaces/IAssetsSystemData.md) |

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
| `data` | [`IAssetsSystemData`](../interfaces/IAssetsSystemData.md) |

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
| `data` | [`IAssetsSystemData`](../interfaces/IAssetsSystemData.md) |

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
| `data` | [`IAssetsSystemData`](../interfaces/IAssetsSystemData.md) | - |

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
| `data` | [`IAssetsSystemData`](../interfaces/IAssetsSystemData.md) |
| `preData` | [`IAssetsSystemData`](../interfaces/IAssetsSystemData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onUpdate](Component.md)

## Properties

### priority

• `Readonly` **priority**: `number` = `10`

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

### addAsset

▸ **addAsset**<`T`>(`type`, `id`, `asset`): `void`

手动添加一个资源。

#### Type parameters

| Name |
| --- |
| `T` |

#### Parameters

| Name | Type |
| --- | --- |
| `type` | `string` |
| `id` | `string` |
| `asset` | `T` |

#### Returns

`void`


### cancelAsset

▸ **cancelAsset**(`type`, `id`): `void`

取消加载一个资源。

#### Parameters

| Name | Type |
| --- | --- |
| `type` | `string` |
| `id` | `string` |

#### Returns

`void`


### getAsset

▸ **getAsset**<`T`>(`type`, `id`, `fallback?`): `T`

获取一个资源，如果尚未加载完成，也会返回`undefined`。

#### Type parameters

| Name |
| --- |
| `T` |

#### Parameters

| Name | Type |
| --- | --- |
| `type` | `string` |
| `id` | `string` |
| `fallback?` | `string` |

#### Returns

`T`


### getAssetWithState

▸ **getAssetWithState**<`T`>(`type`, `id`, `fallback?`): `IAssetWithState`<`T`>

获取一个资源以及加载状态。

#### Type parameters

| Name |
| --- |
| `T` |

#### Parameters

| Name | Type |
| --- | --- |
| `type` | `string` |
| `id` | `string` |
| `fallback?` | `string` |

#### Returns

`IAssetWithState`<`T`>


### getData

▸ **getData**<`T`>(`key`): [`IAssetsSystemData`](../interfaces/IAssetsSystemData.md)[`T`]

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

[`IAssetsSystemData`](../interfaces/IAssetsSystemData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### loadAsset

▸ **loadAsset**(`params`, `parent?`): `Promise`<`IAssetWithState`<`any`>>

手动加载一个资源。

#### Parameters

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<`any`> |
| `parent?` | [`Element`](Element.md) |

#### Returns

`Promise`<`IAssetWithState`<`any`>>


### releaseAsset

▸ **releaseAsset**(`type`, `id`): `void`

手动释放一个资源。

注意在`xml`里加载的资源不要手动释放。

#### Parameters

| Name | Type |
| --- | --- |
| `type` | `string` |
| `id` | `string` |

#### Returns

`void`


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IAssetsSystemData`](../interfaces/IAssetsSystemData.md)> |

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
| `value` | [`IAssetsSystemData`](../interfaces/IAssetsSystemData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
