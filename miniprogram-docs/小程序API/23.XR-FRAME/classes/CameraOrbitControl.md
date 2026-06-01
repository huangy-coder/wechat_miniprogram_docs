# Class: CameraOrbitControl

> 官方文档：[Class: CameraOrbitControl](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/CameraOrbitControl.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / CameraOrbitControl
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / CameraOrbitControl

## Hierarchy

- [`Component`](Component.md)<[`ICameraOrbitControlData`](../interfaces/ICameraOrbitControlData.md)> ↳ **`CameraOrbitControl`**

## Table of contents

### Constructors

- [constructor](CameraOrbitControl.md)

### Events

- [onAdd](CameraOrbitControl.md)
- [onRelease](CameraOrbitControl.md)
- [onRemove](CameraOrbitControl.md)
- [onTick](CameraOrbitControl.md)
- [onUpdate](CameraOrbitControl.md)

### Properties

- [dampingFactor](CameraOrbitControl.md)
- [enableDamping](CameraOrbitControl.md)
- [isEnabled](CameraOrbitControl.md)
- [isLockMove](CameraOrbitControl.md)
- [isLockRotate](CameraOrbitControl.md)
- [isLockX](CameraOrbitControl.md)
- [isLockY](CameraOrbitControl.md)
- [isLockZoom](CameraOrbitControl.md)
- [panMax](CameraOrbitControl.md)
- [panMin](CameraOrbitControl.md)
- [panSpeed](CameraOrbitControl.md)
- [priority](CameraOrbitControl.md)
- [rotateSpeed](CameraOrbitControl.md)
- [schema](CameraOrbitControl.md)
- [zoomMax](CameraOrbitControl.md)
- [zoomMin](CameraOrbitControl.md)
- [zoomSpeed](CameraOrbitControl.md)
- [EVENTS](CameraOrbitControl.md)

### Accessors

- [damping](CameraOrbitControl.md)
- [el](CameraOrbitControl.md)
- [scene](CameraOrbitControl.md)
- [target](CameraOrbitControl.md)
- [version](CameraOrbitControl.md)

### Methods

- [disable](CameraOrbitControl.md)
- [enable](CameraOrbitControl.md)
- [getData](CameraOrbitControl.md)
- [setData](CameraOrbitControl.md)
- [setDataOne](CameraOrbitControl.md)

## Constructors

### constructor

• **new CameraOrbitControl**()

#### Inherited from

[Component](Component.md).[constructor](Component.md)

## Events

### onAdd

▸ **onAdd**(`parent`, `data`): `void`

添加到世界，继承请先`super.onAdd()`。

#### Parameters

| Name | Type |
| --- | --- |
| `parent` | [`Element`](Element.md) |
| `data` | [`ICameraOrbitControlData`](../interfaces/ICameraOrbitControlData.md) |

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
| `data` | [`ICameraOrbitControlData`](../interfaces/ICameraOrbitControlData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onRelease](Component.md)


### onRemove

▸ **onRemove**(): `void`

销毁，继承请先`super.onUpdate()`。

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
| `data` | [`ICameraOrbitControlData`](../interfaces/ICameraOrbitControlData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onTick](Component.md)


### onUpdate

▸ **onUpdate**(`data`): `void`

每一帧更新，继承请先`super.onUpdate()`。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | [`ICameraOrbitControlData`](../interfaces/ICameraOrbitControlData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onUpdate](Component.md)

## Properties

### dampingFactor

• **dampingFactor**: `number` = `0.1`

阻尼系数。


### enableDamping

• **enableDamping**: `boolean` = `true`

开启阻尼缓动。


### isEnabled

• **isEnabled**: `boolean` = `false`

是否已经开启。


### isLockMove

• **isLockMove**: `boolean` = `false`

是否锁定移动。


### isLockRotate

• **isLockRotate**: `boolean` = `false`

是否锁定旋转。


### isLockX

• **isLockX**: `boolean` = `false`

是否锁定横向旋转。


### isLockY

• **isLockY**: `boolean` = `false`

是否锁定纵向旋转。


### isLockZoom

• **isLockZoom**: `boolean` = `false`

是否锁定缩放。


### panMax

• **panMax**: [`Vector3`](Vector3.md)

允许的最大平移边界。


### panMin

• **panMin**: [`Vector3`](Vector3.md)

允许的最小平移边界。


### panSpeed

• **panSpeed**: `number` = `1`

平移速度。


### priority

• `Readonly` **priority**: `number`

自定义组件的更新优先级。

#### Inherited from

[Component](Component.md).[priority](Component.md)


### rotateSpeed

• **rotateSpeed**: `number` = `1`

旋转速度。


### schema

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md)

详见[CameraOrbitControlSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#CameraOrbitControlSchema)。

#### Overrides

[Component](Component.md).[schema](Component.md)


### zoomMax

• **zoomMax**: `number`

允许的最大缩放值。


### zoomMin

• **zoomMin**: `number` = `-Infinity`

允许的最小缩放值。


### zoomSpeed

• **zoomSpeed**: `number` = `1`

缩放速度。


### EVENTS

▪ `Static` **EVENTS**: `string`[] = `[]`

#### Inherited from

[Component](Component.md).[EVENTS](Component.md)

## Accessors

### damping

• `get` **damping**(): `boolean`

当前是否正在缓动。

#### Returns

`boolean`


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


### target

• `get` **target**(): [`Vector3`](Vector3.md)

获取当前目标。

#### Returns

[`Vector3`](Vector3.md)


### version

• `get` **version**(): `number`

当前版本，每次有数据更新都会增加，可以用作和其他组件合作的依据。

#### Returns

`number`

## Methods

### disable

▸ **disable**(): `void`

关闭控制器。

#### Returns

`void`


### enable

▸ **enable**(): `void`

启动控制器。

#### Returns

`void`


### getData

▸ **getData**<`T`>(`key`): [`ICameraOrbitControlData`](../interfaces/ICameraOrbitControlData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ICameraOrbitControlData`](../interfaces/ICameraOrbitControlData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`ICameraOrbitControlData`](../interfaces/ICameraOrbitControlData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`ICameraOrbitControlData`](../interfaces/ICameraOrbitControlData.md)> |

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
| `T` | extends keyof [`ICameraOrbitControlData`](../interfaces/ICameraOrbitControlData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`ICameraOrbitControlData`](../interfaces/ICameraOrbitControlData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
