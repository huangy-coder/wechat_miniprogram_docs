# Class: Animation<IData, IOptions>

> 官方文档：[Class: Animation<IData, IOptions>](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Animation.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Animation
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Animation

动画资源基类，被[Animator](Animator.md)使用，可以继承它来实现具体的动画。

## Type parameters

| Name | Type | Description |
| --- | --- | --- |
| `IData` | `any` | 动画初始化接受的数据。 |
| `IOptions` | `any` | 动画播放时接受的额外追加选项。 |

## Hierarchy

- **`Animation`** ↳ [`KeyframeAnimation`](KeyframeAnimation.md)

## Table of contents

### Constructors

- [constructor](Animation.md)

### Events

- [onInit](Animation.md)
- [onPause](Animation.md)
- [onPlay](Animation.md)
- [onResume](Animation.md)
- [onStop](Animation.md)
- [onUpdate](Animation.md)

### Properties

- [clipNames](Animation.md)

### Accessors

- [scene](Animation.md)

## Constructors

### constructor

• **new Animation**<`IData`, `IOptions`>(`_scene`, `data`)

#### Type parameters

| Name | Type |
| --- | --- |
| `IData` | `any` |
| `IOptions` | `any` |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `_scene` | [`Scene`](Scene.md) | 场景实例。 |
| `data` | `IData` | 初始化动画数据。 |

## Events

### onInit

▸ **onInit**(`data`): `void`

动画初始化时执行的生命周期，只会执行一次。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `data` | `IData` | 初始化动画数据。 |

#### Returns

`void`


### onPause

▸ **onPause**(`el`): `void`

在动画暂停时执行的回调。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `el` | [`Element`](Element.md) | 本次播放作用于的`element`。 |

#### Returns

`void`


### onPlay

▸ **onPlay**(`el`, `clipName`, `options`): `Object`

动画开始播放时执行的生命周期。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `el` | [`Element`](Element.md) | 本次播放作用于的`element`，一个动画可能作用于多个`element`，可以在这里区分。 |
| `clipName` | `string` | 本次播放的片段名字。 |
| `options` | `IOptions` | 本次播放时的附加选项。 |

#### Returns

`Object`

返回本次播放片段的参数，必须包括时长`duration`(s)，可选循环次数`loop`、延迟`delay`和方向`direction`。

| Name | Type |
| --- | --- |
| `delay?` | `number` |
| `direction?` | [`TDirection`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TDirection) |
| `duration` | `number` |
| `loop?` | `number` |


### onResume

▸ **onResume**(`el`): `void`

在动画从暂停状态唤醒时执行的回调。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `el` | [`Element`](Element.md) | 本次播放作用于的`element`。 |

#### Returns

`void`


### onStop

▸ **onStop**(`el`): `void`

在动画停止时执行的回调。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `el` | [`Element`](Element.md) | 本次播放作用于的`element`。 |

#### Returns

`void`


### onUpdate

▸ **onUpdate**(`el`, `progress`, `reverse`): `void`

在动画更新时执行的回调。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `el` | [`Element`](Element.md) | 本次播放作用于的`element`。 |
| `progress` | `number` | 播放进度，范围为线性的`0~1`。 |
| `reverse` | `boolean` | 本次播放是否反向。 |

#### Returns

`void`

## Properties

### clipNames

• **clipNames**: `string`[]

动画所有的片段名字，必须在`onInit`中被初始化。

## Accessors

### scene

• `get` **scene**(): [`Scene`](Scene.md)

场景实例。

#### Returns

[`Scene`](Scene.md)
