# Class: Camera

> 官方文档：[Class: Camera](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Camera.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Camera
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Camera

相机组件，一般被代理到[XRCamera](XRCamera.md)元素。

## Hierarchy

- [`Component`](Component.md)<[`ICameraData`](../interfaces/ICameraData.md)> ↳ **`Camera`**

## Table of contents

### Constructors

- [constructor](Camera.md)

### Events

- [onAdd](Camera.md)
- [onRelease](Camera.md)
- [onRemove](Camera.md)
- [onTick](Camera.md)
- [onUpdate](Camera.md)

### Properties

- [priority](Camera.md)
- [schema](Camera.md)
- [EVENTS](Camera.md)

### Accessors

- [allowFeatures](Camera.md)
- [background](Camera.md)
- [bgStates](Camera.md)
- [bgStatesClear](Camera.md)
- [cullMask](Camera.md)
- [depth](Camera.md)
- [el](Camera.md)
- [far](Camera.md)
- [features](Camera.md)
- [hdr](Camera.md)
- [near](Camera.md)
- [postProcess](Camera.md)
- [scene](Camera.md)
- [target](Camera.md)
- [version](Camera.md)

### Methods

- [changeProjectMatrix](Camera.md)
- [changeViewMatrix](Camera.md)
- [clearBackgroundRenderStates](Camera.md)
- [convertClipPositionToWorld](Camera.md)
- [convertWorldPositionToClip](Camera.md)
- [getData](Camera.md)
- [setBackgroundRenderStates](Camera.md)
- [setData](Camera.md)
- [setDataOne](Camera.md)

## Constructors

### constructor

• **new Camera**()

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
| `data` | [`ICameraData`](../interfaces/ICameraData.md) |

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
| `data` | [`ICameraData`](../interfaces/ICameraData.md) |

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
| `data` | [`ICameraData`](../interfaces/ICameraData.md) |

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
| `data` | [`ICameraData`](../interfaces/ICameraData.md) |

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
| `data` | [`ICameraData`](../interfaces/ICameraData.md) |
| `preData` | [`ICameraData`](../interfaces/ICameraData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onUpdate](Component.md)

## Properties

### priority

• `Readonly` **priority**: `number` = `200`

自定义组件的更新优先级。

#### Overrides

[Component](Component.md).[priority](Component.md)


### schema

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md)

详见[CameraSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#CameraSchema)。

#### Overrides

[Component](Component.md).[schema](Component.md)


### EVENTS

▪ `Static` **EVENTS**: `string`[] = `[]`

#### Inherited from

[Component](Component.md).[EVENTS](Component.md)

## Accessors

### allowFeatures

• `get` **allowFeatures**(): `string`[]

#### Returns

`string`[]


### background

• `get` **background**(): [`TCameraBackground`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TCameraBackground)

#### Returns

[`TCameraBackground`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TCameraBackground)


### bgStates

• `get` **bgStates**(): `Object`

**`internal。`**

#### Returns

`Object`


### bgStatesClear

• `get` **bgStatesClear**(): `boolean`

**`internal。`**

#### Returns

`boolean`


### cullMask

• `get` **cullMask**(): `number`

#### Returns

`number`


### depth

• `get` **depth**(): `number`

相机深度。

#### Returns

`number`


### el

• `get` **el**(): [`Element`](Element.md)

挂载的元素。

#### Returns

[`Element`](Element.md)


### far

• `get` **far**(): `number`

#### Returns

`number`


### features

• `get` **features**(): `Object`

当前渲染特性集合。

#### Returns

`Object`


### hdr

• `get` **hdr**(): `boolean`

#### Returns

`boolean`


### near

• `get` **near**(): `number`

#### Returns

`number`


### postProcess

• `get` **postProcess**(): [`PostProcess`](PostProcess.md)[]

#### Returns

[`PostProcess`](PostProcess.md)[]


### scene

• `get` **scene**(): [`Scene`](Scene.md)

当前场景。

#### Returns

[`Scene`](Scene.md)


### target

• `get` **target**(): [`Transform`](Transform.md)

#### Returns

[`Transform`](Transform.md)


### version

• `get` **version**(): `number`

当前版本，每次有数据更新都会增加，可以用作和其他组件合作的依据。

#### Returns

`number`

## Methods

### changeProjectMatrix

▸ **changeProjectMatrix**(`manual`, `mat4?`): `void`

修改projectMatrix的设置类型。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `manual` | `boolean` | 是否要设置为手动模式。 |
| `mat4?` | `Float32Array` \| [`Matrix4`](Matrix4.md) | 手动模式下，要设置的值。 |

#### Returns

`void`


### changeViewMatrix

▸ **changeViewMatrix**(`manual`, `mat4?`): `void`

修改viewMatrix的设置类型。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `manual` | `boolean` | 是否要设置为手动模式。 |
| `mat4?` | `Float32Array` \| [`Matrix4`](Matrix4.md) | 手动模式下，要设置的值。 |

#### Returns

`void`


### clearBackgroundRenderStates

▸ **clearBackgroundRenderStates**(): `void`

清空相机背景渲染状态。

#### Returns

`void`


### convertClipPositionToWorld

▸ **convertClipPositionToWorld**(`clipPos`, `dst?`): [`Vector3`](Vector3.md)

将齐次裁剪空间转换到世界坐标系位置。

#### Parameters

| Name | Type |
| --- | --- |
| `clipPos` | [`Vector3`](Vector3.md) |
| `dst?` | [`Vector3`](Vector3.md) |

#### Returns

[`Vector3`](Vector3.md)


### convertWorldPositionToClip

▸ **convertWorldPositionToClip**(`worldPos`, `dst?`): [`Vector3`](Vector3.md)

将世界坐标系位置转换到齐次裁剪空间。

#### Parameters

| Name | Type |
| --- | --- |
| `worldPos` | [`Vector3`](Vector3.md) |
| `dst?` | [`Vector3`](Vector3.md) |

#### Returns

[`Vector3`](Vector3.md)


### getData

▸ **getData**<`T`>(`key`): [`ICameraData`](../interfaces/ICameraData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ICameraData`](../interfaces/ICameraData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`ICameraData`](../interfaces/ICameraData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### setBackgroundRenderStates

▸ **setBackgroundRenderStates**(`states`): `void`

修改相机背景的渲染状态。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `states` | `Object` | 同[Material.setRenderStates](Material.md) |

#### Returns

`void`


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`ICameraData`](../interfaces/ICameraData.md)> |

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
| `T` | extends keyof [`ICameraData`](../interfaces/ICameraData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`ICameraData`](../interfaces/ICameraData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
