# Class: ARSystem

> 官方文档：[Class: ARSystem](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/ARSystem.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / ARSystem
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / ARSystem

AR系统，负责整个场景AR相关对象的管理。

代理自小程序的`VKSession`。

## Hierarchy

- [`Component`](Component.md)<[`IARSystemData`](../interfaces/IARSystemData.md)> ↳ **`ARSystem`**

## Table of contents

### Constructors

- [constructor](ARSystem.md)

### Events

- [onAdd](ARSystem.md)
- [onRelease](ARSystem.md)
- [onRemove](ARSystem.md)
- [onTick](ARSystem.md)
- [onUpdate](ARSystem.md)

### Properties

- [priority](ARSystem.md)
- [schema](ARSystem.md)
- [EVENTS](ARSystem.md)

### Accessors

- [arModes](ARSystem.md)
- [arVersion](ARSystem.md)
- [el](ARSystem.md)
- [posCount](ARSystem.md)
- [ready](ARSystem.md)
- [scene](ARSystem.md)
- [supported](ARSystem.md)
- [version](ARSystem.md)

### Methods

- [forceSetViewMatrix](ARSystem.md)
- [getARRawData](ARSystem.md)
- [getData](ARSystem.md)
- [placeHere](ARSystem.md)
- [resetPlane](ARSystem.md)
- [setData](ARSystem.md)
- [setDataOne](ARSystem.md)

## Constructors

### constructor

• **new ARSystem**()

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
| `data` | [`IARSystemData`](../interfaces/IARSystemData.md) |

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
| `data` | [`IARSystemData`](../interfaces/IARSystemData.md) |

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
| `data` | [`IARSystemData`](../interfaces/IARSystemData.md) |

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
| `data` | [`IARSystemData`](../interfaces/IARSystemData.md) |

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
| `data` | [`IARSystemData`](../interfaces/IARSystemData.md) |
| `preData` | [`IARSystemData`](../interfaces/IARSystemData.md) |

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

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md)

详见[ARSystemSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#ARSystemSchema)。

#### Overrides

[Component](Component.md).[schema](Component.md)


### EVENTS

▪ `Static` **EVENTS**: `string`[]

#### Overrides

[Component](Component.md).[EVENTS](Component.md)

## Accessors

### arModes

• `get` **arModes**(): [`TTrackMode`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TTrackMode)[]

当前启动的追踪模式。

#### Returns

[`TTrackMode`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TTrackMode)[]


### arVersion

• `get` **arVersion**(): `number`

当前启动的AR系统版本。

#### Returns

`number`


### el

• `get` **el**(): [`Element`](Element.md)

挂载的元素。

#### Returns

[`Element`](Element.md)


### posCount

• `get` **posCount**(): `number`

在`Face`/`Body`/`Hand`模式下，当前识别到的姿态数量。

#### Returns

`number`


### ready

• `get` **ready**(): `boolean`

当前是否已经可用。

#### Returns

`boolean`


### scene

• `get` **scene**(): [`Scene`](Scene.md)

当前场景。

#### Returns

[`Scene`](Scene.md)


### supported

• `get` **supported**(): `boolean`

当前设备是否启动成功。

#### Returns

`boolean`


### version

• `get` **version**(): `number`

当前版本，每次有数据更新都会增加，可以用作和其他组件合作的依据。

#### Returns

`number`

## Methods

### forceSetViewMatrix

▸ **forceSetViewMatrix**(`camera`, `mat`): `void`

提供一个修改某个设置为`isARCamera`的相机的试图矩阵的手段。

#### Parameters

| Name | Type |
| --- | --- |
| `camera` | [`Camera`](Camera.md) |
| `mat` | [`Matrix4`](Matrix4.md) |

#### Returns

`void`


### getARRawData

▸ **getARRawData**(): [`IARRawData`](../interfaces/IARRawData.md)

获取AR的追踪的原始数据。

#### Returns

[`IARRawData`](../interfaces/IARRawData.md)


### getData

▸ **getData**<`T`>(`key`): [`IARSystemData`](../interfaces/IARSystemData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IARSystemData`](../interfaces/IARSystemData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`IARSystemData`](../interfaces/IARSystemData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### placeHere

▸ **placeHere**(`nodeIdOrElement`, `switchVisible?`): `boolean`

在`Plane`模式下，同步某个节点到当前追踪到的和平面的交点。

#### Parameters

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `nodeIdOrElement` | `string` \| [`Element`](Element.md) | `undefined` | 节点的`nodeId`或是`element`引用。 |
| `switchVisible` | `boolean` | `true` | 是否要自动切换显示或隐藏。 |

#### Returns

`boolean`

是否放置成功


### resetPlane

▸ **resetPlane**(): `void`

在`Plane`模式下，重置平面。

#### Returns

`void`


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IARSystemData`](../interfaces/IARSystemData.md)> |

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
| `T` | extends keyof [`IARSystemData`](../interfaces/IARSystemData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IARSystemData`](../interfaces/IARSystemData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
