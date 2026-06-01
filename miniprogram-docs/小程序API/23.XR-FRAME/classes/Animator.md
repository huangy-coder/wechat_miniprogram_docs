# Class: Animator

> 官方文档：[Class: Animator](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Animator.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Animator
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Animator

## Hierarchy

- [`Component`](Component.md)<[`IAnimatorData`](../interfaces/IAnimatorData.md)> ↳ **`Animator`**

## Table of contents

### Constructors

- [constructor](Animator.md)

### Events

- [onAdd](Animator.md)
- [onRelease](Animator.md)
- [onRemove](Animator.md)
- [onTick](Animator.md)
- [onUpdate](Animator.md)

### Properties

- [priority](Animator.md)
- [schema](Animator.md)
- [EVENTS](Animator.md)

### Accessors

- [el](Animator.md)
- [scene](Animator.md)
- [version](Animator.md)

### Methods

- [addAnimation](Animator.md)
- [createAnimation](Animator.md)
- [getData](Animator.md)
- [pause](Animator.md)
- [pauseToFrame](Animator.md)
- [play](Animator.md)
- [removeAnimation](Animator.md)
- [resume](Animator.md)
- [setData](Animator.md)
- [setDataOne](Animator.md)
- [stop](Animator.md)

## Constructors

### constructor

• **new Animator**()

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
| `data` | [`IAnimatorData`](../interfaces/IAnimatorData.md) |

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
| `data` | [`IAnimatorData`](../interfaces/IAnimatorData.md) |

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
| `data` | [`IAnimatorData`](../interfaces/IAnimatorData.md) |

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
| `data` | [`IAnimatorData`](../interfaces/IAnimatorData.md) | - |

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
| `data` | [`IAnimatorData`](../interfaces/IAnimatorData.md) |
| `preData` | [`IAnimatorData`](../interfaces/IAnimatorData.md) |

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

详见[AnimatorSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#AnimatorSchema)。

#### Overrides

[Component](Component.md).[schema](Component.md)


### EVENTS

▪ `Static` **EVENTS**: `string`[]

#### Overrides

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

### addAnimation

▸ **addAnimation**<`T`>(`anim`, `clipMap?`): `T`

手动添加一个动画。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends [`Animation`](Animation.md)<`any`, `any`, `T`> |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `anim` | `T` | - |
| `clipMap?` | `Object` | 可选的动画片段名字映射。 |

#### Returns

`T`


### createAnimation

▸ **createAnimation**<`T`>(`clz`, `data`, `clipMap?`): `T`

直接通过类`clz`和初始化数据`data`创建一个动画并添加到自身内。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends [`Animation`](Animation.md)<`any`, `any`, `T`> |

#### Parameters

| Name | Type |
| --- | --- |
| `clz` | (`scene`: [`Scene`](Scene.md), `data`: `T`[`"__DATA_TYPE"`]) => `T` |
| `data` | `T`[`"__DATA_TYPE"`] |
| `clipMap?` | `Object` |

#### Returns

`T`


### getData

▸ **getData**<`T`>(`key`): [`IAnimatorData`](../interfaces/IAnimatorData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IAnimatorData`](../interfaces/IAnimatorData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`IAnimatorData`](../interfaces/IAnimatorData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### pause

▸ **pause**(`name?`): `void`

暂停播放。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `name?` | `string` | 需要暂停的片段，如果不填则暂停所有正在播放的片段。 |

#### Returns

`void`


### pauseToFrame

▸ **pauseToFrame**(`name`, `progress`): `void`

播放动画片段到某一进度并停下。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | 片段名称。 |
| `progress` | `number` | 停到的某个进度，0~1。 |

#### Returns

`void`


### play

▸ **play**(`name`, `options?`): `void`

播放一个动画片段，**可以同时播放多个片段**。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | 动画片段名称。 |
| `options?` | [`IAnimationPlayOptions`](../interfaces/IAnimationPlayOptions.md) & { `[key: string]`: `any`; } | 播放选项。 |

#### Returns

`void`


### removeAnimation

▸ **removeAnimation**(`anim`): `void`

移除一个动画

#### Parameters

| Name | Type |
| --- | --- |
| `anim` | [`Animation`](Animation.md)<`any`, `any`> |

#### Returns

`void`


### resume

▸ **resume**(`name?`): `void`

唤醒暂停的动画。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `name?` | `string` | 需要唤醒的片段，如果不填则唤醒所有暂停的片段。 |

#### Returns

`void`


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IAnimatorData`](../interfaces/IAnimatorData.md)> |

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
| `T` | extends keyof [`IAnimatorData`](../interfaces/IAnimatorData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IAnimatorData`](../interfaces/IAnimatorData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)


### stop

▸ **stop**(`name?`): `void`

停止播放。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `name?` | `string` | 需要停止的片段，如果不填则停止所有正在播放的片段。 |

#### Returns

`void`
