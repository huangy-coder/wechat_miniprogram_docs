# Class: ShareSystem

> 官方文档：[Class: ShareSystem](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/ShareSystem.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / ShareSystem
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / ShareSystem

分享系统，负责分享相关功能。

## Hierarchy

- [`Component`](Component.md)<[`IShareSystemData`](../interfaces/IShareSystemData.md)> ↳ **`ShareSystem`**

## Table of contents

### Constructors

- [constructor](ShareSystem.md)

### Events

- [onAdd](ShareSystem.md)
- [onRelease](ShareSystem.md)
- [onRemove](ShareSystem.md)
- [onTick](ShareSystem.md)
- [onUpdate](ShareSystem.md)

### Properties

- [priority](ShareSystem.md)
- [schema](ShareSystem.md)
- [EVENTS](ShareSystem.md)

### Accessors

- [el](ShareSystem.md)
- [recordState](ShareSystem.md)
- [scene](ShareSystem.md)
- [supported](ShareSystem.md)
- [version](ShareSystem.md)

### Methods

- [captureToArrayBuffer](ShareSystem.md)
- [captureToArrayBufferAsync](ShareSystem.md)
- [captureToDataURL](ShareSystem.md)
- [captureToDataURLAsync](ShareSystem.md)
- [captureToFriends](ShareSystem.md)
- [captureToLocalPath](ShareSystem.md)
- [getData](ShareSystem.md)
- [recordFinishToAlbum](ShareSystem.md)
- [recordFinishToTempFile](ShareSystem.md)
- [recordPause](ShareSystem.md)
- [recordResume](ShareSystem.md)
- [recordStart](ShareSystem.md)
- [setData](ShareSystem.md)
- [setDataOne](ShareSystem.md)

## Constructors

### constructor

• **new ShareSystem**()

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
| `data` | [`IShareSystemData`](../interfaces/IShareSystemData.md) |

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
| `data` | [`IShareSystemData`](../interfaces/IShareSystemData.md) |

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
| `data` | [`IShareSystemData`](../interfaces/IShareSystemData.md) |

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
| `data` | [`IShareSystemData`](../interfaces/IShareSystemData.md) |

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
| `data` | [`IShareSystemData`](../interfaces/IShareSystemData.md) |
| `preData` | [`IShareSystemData`](../interfaces/IShareSystemData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onUpdate](Component.md)

## Properties

### priority

• `Readonly` **priority**: `number`

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


### recordState

• `get` **recordState**(): [`EShareRecordState`](../enums/EShareRecordState.md)

当前录屏状态。

#### Returns

[`EShareRecordState`](../enums/EShareRecordState.md)


### scene

• `get` **scene**(): [`Scene`](Scene.md)

当前场景。

#### Returns

[`Scene`](Scene.md)


### supported

• `get` **supported**(): `boolean`

当前是否支持分享系统。

#### Returns

`boolean`


### version

• `get` **version**(): `number`

当前版本，每次有数据更新都会增加，可以用作和其他组件合作的依据。

#### Returns

`number`

## Methods

### captureToArrayBuffer

▸ **captureToArrayBuffer**(`options?`): `ArrayBuffer`

**`deprecated`** 请在`v3.0.2`后使用异步版本，同步版本不再维护，请使用`captureToArrayBufferAsync`。
截屏输出为`ArrayBuffer`。

#### Parameters

| Name | Type |
| --- | --- |
| `options` | [`IShareCaptureOptions`](../interfaces/IShareCaptureOptions.md) |

#### Returns

`ArrayBuffer`


### captureToArrayBufferAsync

▸ **captureToArrayBufferAsync**(`options?`): `Promise`<`ArrayBuffer`>

截屏输出为`ArrayBuffer`。

#### Parameters

| Name | Type |
| --- | --- |
| `options` | [`IShareCaptureOptions`](../interfaces/IShareCaptureOptions.md) |

#### Returns

`Promise`<`ArrayBuffer`>


### captureToDataURL

▸ **captureToDataURL**(`options?`): `string`

**`deprecated`** 请在`v3.0.2`后使用异步版本，同步版本不再维护，请使用`captureToDataURLAsync`。
截屏输出为`base64`。

#### Parameters

| Name | Type |
| --- | --- |
| `options` | [`IShareCaptureOptions`](../interfaces/IShareCaptureOptions.md) |

#### Returns

`string`


### captureToDataURLAsync

▸ **captureToDataURLAsync**(`options?`): `Promise`<`string`>

截屏输出为`base64`。

#### Parameters

| Name | Type |
| --- | --- |
| `options` | [`IShareCaptureOptions`](../interfaces/IShareCaptureOptions.md) |

#### Returns

`Promise`<`string`>


### captureToFriends

▸ **captureToFriends**(`options?`): `Promise`<`void`>

直接截屏分享给好友。

#### Parameters

| Name | Type |
| --- | --- |
| `options` | [`IShareCaptureOptions`](../interfaces/IShareCaptureOptions.md) |

#### Returns

`Promise`<`void`>


### captureToLocalPath

▸ **captureToLocalPath**(`options?`, `callback`): `Promise`<`void`>

截屏输出为本地路径，回调完成后会自动释放。

**`params`** callback 接受结果的回调，处理完后会释放文件。在v2.27.1前是异步，之后兼容同步和异步。

#### Parameters

| Name | Type |
| --- | --- |
| `options` | [`IShareCaptureOptions`](../interfaces/IShareCaptureOptions.md) |
| `callback` | (`fp`: `string`) => `void` \| `Promise`<`void`> |

#### Returns

`Promise`<`void`>


### getData

▸ **getData**<`T`>(`key`): [`IShareSystemData`](../interfaces/IShareSystemData.md)[`T`]

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

[`IShareSystemData`](../interfaces/IShareSystemData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### recordFinishToAlbum

▸ **recordFinishToAlbum**(): `Promise`<`void`>

录屏完成，直接保存到用户相册。

#### Returns

`Promise`<`void`>


### recordFinishToTempFile

▸ **recordFinishToTempFile**(): `Promise`<`string`>

录屏完成，输出到临时文件。

#### Returns

`Promise`<`string`>

临时文件地址


### recordPause

▸ **recordPause**(): `Promise`<`void`>

暂停本次录屏。

#### Returns

`Promise`<`void`>


### recordResume

▸ **recordResume**(): `Promise`<`void`>

唤醒本次录屏。

#### Returns

`Promise`<`void`>


### recordStart

▸ **recordStart**(`options?`): `Promise`<`void`>

启动录屏。

#### Parameters

| Name | Type |
| --- | --- |
| `options?` | [`IShareRecordOptions`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IShareRecordOptions.html) |

#### Returns

`Promise`<`void`>


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IShareSystemData`](../interfaces/IShareSystemData.md)> |

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
| `value` | [`IShareSystemData`](../interfaces/IShareSystemData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
