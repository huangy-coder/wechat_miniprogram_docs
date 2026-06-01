# Class: AssetRenderTexture

> 官方文档：[Class: AssetRenderTexture](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AssetRenderTexture.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / AssetRenderTexture
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / AssetRenderTexture

渲染纹理创建组件，用于在`xml`中创建[RenderTexture](RenderTexture.md)资源，一般被代理到[XRAssetRenderTexture](XRAssetRenderTexture.md)元素。

## Hierarchy

- [`Component`](Component.md)<[`IAssetRenderTextureData`](../interfaces/IAssetRenderTextureData.md)> ↳ **`AssetRenderTexture`**

## Table of contents

### Constructors

- [constructor](AssetRenderTexture.md)

### Events

- [onAdd](AssetRenderTexture.md)
- [onRelease](AssetRenderTexture.md)
- [onRemove](AssetRenderTexture.md)
- [onTick](AssetRenderTexture.md)
- [onUpdate](AssetRenderTexture.md)

### Properties

- [isAssetRenderTexture](AssetRenderTexture.md)
- [priority](AssetRenderTexture.md)
- [schema](AssetRenderTexture.md)
- [EVENTS](AssetRenderTexture.md)

### Accessors

- [el](AssetRenderTexture.md)
- [scene](AssetRenderTexture.md)
- [version](AssetRenderTexture.md)

### Methods

- [getData](AssetRenderTexture.md)
- [setData](AssetRenderTexture.md)
- [setDataOne](AssetRenderTexture.md)

## Constructors

### constructor

• **new AssetRenderTexture**()

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
| `data` | [`IAssetRenderTextureData`](../interfaces/IAssetRenderTextureData.md) |

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
| `data` | [`IAssetRenderTextureData`](../interfaces/IAssetRenderTextureData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onRelease](Component.md)


### onRemove

▸ **onRemove**(`parent`, `data`): `void`

移除AssetRenderTexture。

#### Parameters

| Name | Type |
| --- | --- |
| `parent` | [`Element`](Element.md) |
| `data` | [`IAssetRenderTextureData`](../interfaces/IAssetRenderTextureData.md) |

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
| `data` | [`IAssetRenderTextureData`](../interfaces/IAssetRenderTextureData.md) | - |

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
| `data` | [`IAssetRenderTextureData`](../interfaces/IAssetRenderTextureData.md) |
| `preData` | [`IAssetRenderTextureData`](../interfaces/IAssetRenderTextureData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onUpdate](Component.md)

## Properties

### isAssetRenderTexture

• `Readonly` **isAssetRenderTexture**: `boolean` = `true`


### priority

• `Readonly` **priority**: `number`

自定义组件的更新优先级。

#### Inherited from

[Component](Component.md).[priority](Component.md)


### schema

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md)

详见[AssetRenderTextureSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#AssetRenderTextureSchema)。

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

▸ **getData**<`T`>(`key`): [`IAssetRenderTextureData`](../interfaces/IAssetRenderTextureData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IAssetRenderTextureData`](../interfaces/IAssetRenderTextureData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`IAssetRenderTextureData`](../interfaces/IAssetRenderTextureData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IAssetRenderTextureData`](../interfaces/IAssetRenderTextureData.md)> |

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
| `T` | extends keyof [`IAssetRenderTextureData`](../interfaces/IAssetRenderTextureData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IAssetRenderTextureData`](../interfaces/IAssetRenderTextureData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
