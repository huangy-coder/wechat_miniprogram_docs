# Class: KeyframeAnimation

> 官方文档：[Class: KeyframeAnimation](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/KeyframeAnimation.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / KeyframeAnimation
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / KeyframeAnimation

`Keyframe`动画。

## Hierarchy

- [`Animation`](Animation.md)<[`IKeyframeAnimationData`](../interfaces/IKeyframeAnimationData.md), [`IKeyframeAnimationOptions`](../interfaces/IKeyframeAnimationOptions.md)> ↳ **`KeyframeAnimation`**

## Table of contents

### Constructors

- [constructor](KeyframeAnimation.md)

### Events

- [onInit](KeyframeAnimation.md)
- [onPause](KeyframeAnimation.md)
- [onPlay](KeyframeAnimation.md)
- [onResume](KeyframeAnimation.md)
- [onStop](KeyframeAnimation.md)
- [onUpdate](KeyframeAnimation.md)

### Properties

- [clipNames](KeyframeAnimation.md)

### Accessors

- [scene](KeyframeAnimation.md)

## Constructors

### constructor

• **new KeyframeAnimation**(`_scene`, `data`)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `_scene` | [`Scene`](Scene.md) | 场景实例。 |
| `data` | [`IKeyframeAnimationData`](../interfaces/IKeyframeAnimationData.md) | 初始化动画数据。 |

#### Inherited from

[Animation](Animation.md).[constructor](Animation.md)

## Events

### onInit

▸ **onInit**(`data`): `void`

动画初始化时执行的生命周期，只会执行一次。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | [`IKeyframeAnimationData`](../interfaces/IKeyframeAnimationData.md) |

#### Returns

`void`

#### Inherited from

[Animation](Animation.md).[onInit](Animation.md)


### onPause

▸ **onPause**(`el`): `void`

在动画暂停时执行的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `el` | [`Element`](Element.md) |

#### Returns

`void`

#### Inherited from

[Animation](Animation.md).[onPause](Animation.md)


### onPlay

▸ **onPlay**(`el`, `clipName`, `options`): [`IKeyframeAnimationInfo`](../interfaces/IKeyframeAnimationInfo.md)

动画开始播放时执行的生命周期。

#### Parameters

| Name | Type |
| --- | --- |
| `el` | [`Element`](Element.md) |
| `clipName` | `string` |
| `options` | [`IKeyframeAnimationOptions`](../interfaces/IKeyframeAnimationOptions.md) |

#### Returns

[`IKeyframeAnimationInfo`](../interfaces/IKeyframeAnimationInfo.md)

返回本次播放片段的参数，必须包括时长`duration`(s)，可选循环次数`loop`、延迟`delay`和方向`direction`。

#### Inherited from

[Animation](Animation.md).[onPlay](Animation.md)


### onResume

▸ **onResume**(`el`): `void`

在动画从暂停状态唤醒时执行的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `el` | [`Element`](Element.md) |

#### Returns

`void`

#### Inherited from

[Animation](Animation.md).[onResume](Animation.md)


### onStop

▸ **onStop**(`el`): `void`

在动画停止时执行的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `el` | [`Element`](Element.md) |

#### Returns

`void`

#### Inherited from

[Animation](Animation.md).[onStop](Animation.md)


### onUpdate

▸ **onUpdate**(`el`, `progress`, `reverse`): `void`

在动画更新时执行的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `el` | [`Element`](Element.md) |
| `progress` | `number` |
| `reverse` | `boolean` |

#### Returns

`void`

#### Inherited from

[Animation](Animation.md).[onUpdate](Animation.md)

## Properties

### clipNames

• **clipNames**: `string`[]

动画所有的片段名字，必须在`onInit`中被初始化。

#### Inherited from

[Animation](Animation.md).[clipNames](Animation.md)

## Accessors

### scene

• `get` **scene**(): [`Scene`](Scene.md)

场景实例。

#### Returns

[`Scene`](Scene.md)
