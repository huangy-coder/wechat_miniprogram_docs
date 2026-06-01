# Class: Light

> 官方文档：[Class: Light](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Light.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Light
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Light

灯光组件，一般被代理到[XRLight](XRLight.md)元素。

注意整个场景只能存在一个`ambient`光源，第一个`directional`光源将会成为主光源，也只有这个光源能够产生阴影。
目前最多支持四个追加光源。

## Hierarchy

- [`Component`](Component.md)<[`ILightData`](../interfaces/ILightData.md)> ↳ **`Light`**

## Table of contents

### Constructors

- [constructor](Light.md)

### Events

- [onAdd](Light.md)
- [onRelease](Light.md)
- [onRemove](Light.md)
- [onTick](Light.md)
- [onUpdate](Light.md)

### Properties

- [priority](Light.md)
- [schema](Light.md)
- [EVENTS](Light.md)

### Accessors

- [castShadow](Light.md)
- [color](Light.md)
- [el](Light.md)
- [innerConeAngle](Light.md)
- [intensity](Light.md)
- [outerConeAngle](Light.md)
- [range](Light.md)
- [scene](Light.md)
- [shadowBias](Light.md)
- [shadowDistance](Light.md)
- [type](Light.md)
- [version](Light.md)

### Methods

- [getData](Light.md)
- [setData](Light.md)
- [setDataOne](Light.md)

## Constructors

### constructor

• **new Light**()

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
| `data` | [`ILightData`](../interfaces/ILightData.md) |

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
| `data` | [`ILightData`](../interfaces/ILightData.md) |

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
| `data` | [`ILightData`](../interfaces/ILightData.md) |

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
| `data` | [`ILightData`](../interfaces/ILightData.md) |

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
| `data` | [`ILightData`](../interfaces/ILightData.md) |
| `preData` | [`ILightData`](../interfaces/ILightData.md) |

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

详见[LightSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#LightSchema)。

#### Overrides

[Component](Component.md).[schema](Component.md)


### EVENTS

▪ `Static` **EVENTS**: `string`[] = `[]`

#### Inherited from

[Component](Component.md).[EVENTS](Component.md)

## Accessors

### castShadow

• `get` **castShadow**(): `boolean`

#### Returns

`boolean`


### color

• `get` **color**(): `number`[]

#### Returns

`number`[]


### el

• `get` **el**(): [`Element`](Element.md)

挂载的元素。

#### Returns

[`Element`](Element.md)


### innerConeAngle

• `get` **innerConeAngle**(): `number`

#### Returns

`number`


### intensity

• `get` **intensity**(): `number`

#### Returns

`number`


### outerConeAngle

• `get` **outerConeAngle**(): `number`

#### Returns

`number`


### range

• `get` **range**(): `number`

#### Returns

`number`


### scene

• `get` **scene**(): [`Scene`](Scene.md)

当前场景。

#### Returns

[`Scene`](Scene.md)


### shadowBias

• `get` **shadowBias**(): `number`

#### Returns

`number`


### shadowDistance

• `get` **shadowDistance**(): `number`

#### Returns

`number`


### type

• `get` **type**(): `ELightType`

#### Returns

`ELightType`


### version

• `get` **version**(): `number`

当前版本，每次有数据更新都会增加，可以用作和其他组件合作的依据。

#### Returns

`number`

## Methods

### getData

▸ **getData**<`T`>(`key`): [`ILightData`](../interfaces/ILightData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`ILightData`](../interfaces/ILightData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`ILightData`](../interfaces/ILightData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`ILightData`](../interfaces/ILightData.md)> |

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
| `T` | extends keyof [`ILightData`](../interfaces/ILightData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`ILightData`](../interfaces/ILightData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
