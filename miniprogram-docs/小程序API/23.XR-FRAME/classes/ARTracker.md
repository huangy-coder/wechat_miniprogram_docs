# Class: ARTracker

> 官方文档：[Class: ARTracker](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/ARTracker.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / ARTracker
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / ARTracker

AR追踪组件，配合[ARSystem](ARSystem.md)和[Camera](Camera.md)的`isARCamera`属性一起使用。
一般被代理到[XRARTracker](XRARTracker.md)元素。

其提供了追踪的能力，节点将会自动同步识别到的追踪目标的位置和旋转，

## Hierarchy

- [`Component`](Component.md)<[`IARTrackerData`](../interfaces/IARTrackerData.md)> ↳ **`ARTracker`**

## Table of contents

### Constructors

- [constructor](ARTracker.md)

### Events

- [onAdd](ARTracker.md)
- [onRelease](ARTracker.md)
- [onRemove](ARTracker.md)
- [onTick](ARTracker.md)
- [onUpdate](ARTracker.md)

### Properties

- [priority](ARTracker.md)
- [schema](ARTracker.md)
- [EVENTS](ARTracker.md)

### Accessors

- [arActive](ARTracker.md)
- [el](ARTracker.md)
- [errorMessage](ARTracker.md)
- [gesture](ARTracker.md)
- [mode](ARTracker.md)
- [scene](ARTracker.md)
- [score](ARTracker.md)
- [state](ARTracker.md)
- [version](ARTracker.md)

### Methods

- [getData](ARTracker.md)
- [getPosition](ARTracker.md)
- [setData](ARTracker.md)
- [setDataOne](ARTracker.md)

## Constructors

### constructor

• **new ARTracker**()

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
| `data` | [`IARTrackerData`](../interfaces/IARTrackerData.md) |

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
| `data` | [`IARTrackerData`](../interfaces/IARTrackerData.md) |

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
| `data` | [`IARTrackerData`](../interfaces/IARTrackerData.md) |

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
| `data` | [`IARTrackerData`](../interfaces/IARTrackerData.md) | - |

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
| `data` | [`IARTrackerData`](../interfaces/IARTrackerData.md) |
| `preData` | [`IARTrackerData`](../interfaces/IARTrackerData.md) |

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

详见[ARTrackSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#ARTrackSchema)。

#### Overrides

[Component](Component.md).[schema](Component.md)


### EVENTS

▪ `Static` **EVENTS**: `string`[]

#### Overrides

[Component](Component.md).[EVENTS](Component.md)

## Accessors

### arActive

• `get` **arActive**(): `boolean`

是否已经检测到了目标。

#### Returns

`boolean`


### el

• `get` **el**(): [`Element`](Element.md)

挂载的元素。

#### Returns

[`Element`](Element.md)


### errorMessage

• `get` **errorMessage**(): `string`

如果为错误状态，错误信息。

**`version`** v2.29.1

#### Returns

`string`


### gesture

• `get` **gesture**(): `number`

在`Hand`模式下，手势分类，正常`0~18`，无效为`-1`。

#### Returns

`number`


### mode

• `get` **mode**(): [`TTrackMode`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TTrackMode)

跟踪模式。

#### Returns

[`TTrackMode`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TTrackMode)


### scene

• `get` **scene**(): [`Scene`](Scene.md)

当前场景。

#### Returns

[`Scene`](Scene.md)


### score

• `get` **score**(): `number`

`Body`/`Hand`模式下，获取当前的置信度。
一般为`0~1`。

#### Returns

`number`


### state

• `get` **state**(): [`EARTrackerState`](../enums/EARTrackerState.md)

当前识别状态。

**`version`** v2.29.1

#### Returns

[`EARTrackerState`](../enums/EARTrackerState.md)


### version

• `get` **version**(): `number`

当前版本，每次有数据更新都会增加，可以用作和其他组件合作的依据。

#### Returns

`number`

## Methods

### getData

▸ **getData**<`T`>(`key`): [`IARTrackerData`](../interfaces/IARTrackerData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IARTrackerData`](../interfaces/IARTrackerData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`IARTrackerData`](../interfaces/IARTrackerData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### getPosition

▸ **getPosition**(`point`, `output?`, `relativeToTracker?`): [`Vector3`](Vector3.md)

在`Face`/`Body`/`Hand`模式下，获取某个特征点的位置。

#### Parameters

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `point` | `number` | `undefined` | 特征点索引，需要在`0~105`，否则返回`undefined`。 |
| `output?` | [`Vector3`](Vector3.md) | `undefined` | - |
| `relativeToTracker` | `boolean` | `true` | 仅在`ar-system`的`pose3d`属性为`false`时生效。是否相对于`ARTracker`本身，默认为`true`，否则返回世界空间坐标。 |

#### Returns

[`Vector3`](Vector3.md)

只有在`arActive`时才有值，否则返回`undefined`。


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IARTrackerData`](../interfaces/IARTrackerData.md)> |

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
| `T` | extends keyof [`IARTrackerData`](../interfaces/IARTrackerData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IARTrackerData`](../interfaces/IARTrackerData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
