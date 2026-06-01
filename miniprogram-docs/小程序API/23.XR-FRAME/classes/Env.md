# Class: Env

> 官方文档：[Class: Env](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Env.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Env
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Env

一般被代理到[XRARTracker](XRARTracker.md)元素。

## Hierarchy

- [`Component`](Component.md)<[`IEnvData`](../interfaces/IEnvData.md)> ↳ **`Env`**

## Table of contents

### Constructors

- [constructor](Env.md)

### Events

- [onAdd](Env.md)
- [onRelease](Env.md)
- [onRemove](Env.md)
- [onTick](Env.md)
- [onUpdate](Env.md)

### Properties

- [priority](Env.md)
- [schema](Env.md)
- [EVENTS](Env.md)

### Accessors

- [diffuseExp](Env.md)
- [diffuseSH](Env.md)
- [el](Env.md)
- [hasDiffuse](Env.md)
- [hasSpecular](Env.md)
- [isSky2D](Env.md)
- [isSkyRT](Env.md)
- [rotation](Env.md)
- [scene](Env.md)
- [skyMap](Env.md)
- [specularExp](Env.md)
- [specularMap](Env.md)
- [specularMipmapCount](Env.md)
- [specularMipmaps](Env.md)
- [specularRGBD](Env.md)
- [useHalfSkyMap](Env.md)
- [version](Env.md)

### Methods

- [getData](Env.md)
- [setData](Env.md)
- [setDataOne](Env.md)

## Constructors

### constructor

• **new Env**()

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
| `data` | [`IEnvData`](../interfaces/IEnvData.md) |

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
| `data` | [`IEnvData`](../interfaces/IEnvData.md) |

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
| `data` | [`IEnvData`](../interfaces/IEnvData.md) |

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
| `data` | [`IEnvData`](../interfaces/IEnvData.md) | - |

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
| `data` | [`IEnvData`](../interfaces/IEnvData.md) |
| `preData` | [`IEnvData`](../interfaces/IEnvData.md) |

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

详见[EnvSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#EnvSchema)。

#### Overrides

[Component](Component.md).[schema](Component.md)


### EVENTS

▪ `Static` **EVENTS**: `string`[] = `[]`

#### Inherited from

[Component](Component.md).[EVENTS](Component.md)

## Accessors

### diffuseExp

• `get` **diffuseExp**(): `number`

#### Returns

`number`


### diffuseSH

• `get` **diffuseSH**(): `Float32Array`

#### Returns

`Float32Array`


### el

• `get` **el**(): [`Element`](Element.md)

挂载的元素。

#### Returns

[`Element`](Element.md)


### hasDiffuse

• `get` **hasDiffuse**(): `boolean`

#### Returns

`boolean`


### hasSpecular

• `get` **hasSpecular**(): `boolean`

#### Returns

`boolean`


### isSky2D

• `get` **isSky2D**(): `boolean`

#### Returns

`boolean`


### isSkyRT

• `get` **isSkyRT**(): `boolean`

#### Returns

`boolean`


### rotation

• `get` **rotation**(): `number`

#### Returns

`number`


### scene

• `get` **scene**(): [`Scene`](Scene.md)

当前场景。

#### Returns

[`Scene`](Scene.md)


### skyMap

• `get` **skyMap**(): `default`

#### Returns

`default`


### specularExp

• `get` **specularExp**(): `number`

#### Returns

`number`


### specularMap

• `get` **specularMap**(): `default`

#### Returns

`default`


### specularMipmapCount

• `get` **specularMipmapCount**(): `number`

#### Returns

`number`


### specularMipmaps

• `get` **specularMipmaps**(): `boolean`

#### Returns

`boolean`


### specularRGBD

• `get` **specularRGBD**(): `boolean`

#### Returns

`boolean`


### useHalfSkyMap

• `get` **useHalfSkyMap**(): `boolean`

#### Returns

`boolean`


### version

• `get` **version**(): `number`

当前版本，每次有数据更新都会增加，可以用作和其他组件合作的依据。

#### Returns

`number`

## Methods

### getData

▸ **getData**<`T`>(`key`): [`IEnvData`](../interfaces/IEnvData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IEnvData`](../interfaces/IEnvData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`IEnvData`](../interfaces/IEnvData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IEnvData`](../interfaces/IEnvData.md)> |

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
| `T` | extends keyof [`IEnvData`](../interfaces/IEnvData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IEnvData`](../interfaces/IEnvData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)
