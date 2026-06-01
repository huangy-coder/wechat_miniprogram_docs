# Class: Text

> 官方文档：[Class: Text](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Text.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Text
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Text

## Hierarchy

- [`Component`](Component.md)<[`ITextData`](../interfaces/ITextData.md)> ↳ **`Text`**

## Table of contents

### Constructors

- [constructor](Text.md)

### Events

- [onAdd](Text.md)
- [onRelease](Text.md)
- [onRemove](Text.md)
- [onTick](Text.md)
- [onUpdate](Text.md)

### Properties

- [priority](Text.md)
- [schema](Text.md)
- [EVENTS](Text.md)
- [FillRenderData](Text.md)
- [QueryGlyphs](Text.md)
- [Typesetting](Text.md)

### Accessors

- [el](Text.md)
- [id](Text.md)
- [scene](Text.md)
- [version](Text.md)

### Methods

- [getData](Text.md)
- [setData](Text.md)
- [setDataOne](Text.md)

## Constructors

### constructor

• **new Text**()

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
| `data` | [`ITextData`](../interfaces/ITextData.md) |

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
| `data` | [`ITextData`](../interfaces/ITextData.md) |

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
| `data` | [`ITextData`](../interfaces/ITextData.md) |

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
| `data` | [`ITextData`](../interfaces/ITextData.md) |

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
| `data` | [`ITextData`](../interfaces/ITextData.md) |
| `preData` | [`ITextData`](../interfaces/ITextData.md) |

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

▪ `Static` **EVENTS**: `string`[] = `[]`

#### Inherited from

[Component](Component.md).[EVENTS](Component.md)


### FillRenderData

▪ `Static` **FillRenderData**: (`vertexF32`: `Float32Array`, `indexU16`: `Uint16Array`, `batchArray`: `ICharacterData`[]) => `void`

#### Type declaration

▸ (`vertexF32`, `indexU16`, `batchArray`): `void`

##### Parameters

| Name | Type |
| --- | --- |
| `vertexF32` | `Float32Array` |
| `indexU16` | `Uint16Array` |
| `batchArray` | `ICharacterData`[] |

##### Returns

`void`


### QueryGlyphs

▪ `Static` **QueryGlyphs**: (`scene`: [`Scene`](Scene.md), `characters`: `string`, `italic`: `boolean`, `bold`: `boolean`, `fontSize`: `number`, `fontFamily`: `string`) => `IGlyph`[]

#### Type declaration

▸ (`scene`, `characters`, `italic`, `bold`, `fontSize`, `fontFamily`): `IGlyph`[]

多字客户端纹理请求接口

##### Parameters

| Name | Type |
| --- | --- |
| `scene` | [`Scene`](Scene.md) |
| `characters` | `string` |
| `italic` | `boolean` |
| `bold` | `boolean` |
| `fontSize` | `number` |
| `fontFamily` | `string` |

##### Returns

`IGlyph`[]


### Typesetting

▪ `Static` **Typesetting**: (`glyphs`: `IGlyph`[], `batchArrays`: `ICharacterData`[][], `batchIndexs`: `number`[], `wrapWidth`: `number`, `wrapHeight`: `number`, `lineHeight`: `number`, `anchor`: `number`[], `padding`: `number`[], `vertAlign`: `EVertAlignment`, `horzAlign`: `EHorzAlignment`) => `void`

#### Type declaration

▸ (`glyphs`, `batchArrays`, `batchIndexs`, `wrapWidth`, `wrapHeight`, `lineHeight`, `anchor`, `padding`, `vertAlign`, `horzAlign`): `void`

##### Parameters

| Name | Type |
| --- | --- |
| `glyphs` | `IGlyph`[] |
| `batchArrays` | `ICharacterData`[][] |
| `batchIndexs` | `number`[] |
| `wrapWidth` | `number` |
| `wrapHeight` | `number` |
| `lineHeight` | `number` |
| `anchor` | `number`[] |
| `padding` | `number`[] |
| `vertAlign` | `EVertAlignment` |
| `horzAlign` | `EHorzAlignment` |

##### Returns

`void`

## Accessors

### el

• `get` **el**(): [`Element`](Element.md)

挂载的元素。

#### Returns

[`Element`](Element.md)


### id

• `get` **id**(): `number`

#### Returns

`number`


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

▸ **getData**<`T`>(`key`): [`ITextData`](../interfaces/ITextData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ITextData`](../interfaces/ITextData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`ITextData`](../interfaces/ITextData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`ITextData`](../interfaces/ITextData.md)> |

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
| `T` | extends keyof [`ITextData`](../interfaces/ITextData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`ITextData`](../interfaces/ITextData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
