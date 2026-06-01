# Class: EventManager

> 官方文档：[Class: EventManager](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/EventManager.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / EventManager
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / EventManager

事件管理器。

每个`Element`都有自己的事件管理器，通过参数可以触发到`xml`。

## Table of contents

### Constructors

- [constructor](EventManager.md)

### Properties

- [isEventManager](EventManager.md)

### Methods

- [add](EventManager.md)
- [addOnce](EventManager.md)
- [clear](EventManager.md)
- [flush](EventManager.md)
- [flushAll](EventManager.md)
- [has](EventManager.md)
- [remove](EventManager.md)
- [trigger](EventManager.md)

## Constructors

### constructor

• **new EventManager**(`_el`, `_triggerElementEvent`)

#### Parameters

| Name | Type |
| --- | --- |
| `_el` | [`Element`](Element.md) |
| `_triggerElementEvent` | `TFrameworkEventTrigger` |

## Properties

### isEventManager

• **isEventManager**: `boolean` = `true`

## Methods

### add

▸ **add**<`TEvent`>(`type`, `callback`, `priority?`): [`EventManager`](EventManager.md)

添加一个事件监听器。

#### Type parameters

| Name | Type |
| --- | --- |
| `TEvent` | `any` |

#### Parameters

| Name | Type |
| --- | --- |
| `type` | `string` |
| `callback` | [`TEventCallback`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TEventCallback)<`TEvent`> |
| `priority?` | `number` |

#### Returns

[`EventManager`](EventManager.md)


### addOnce

▸ **addOnce**<`TEvent`>(`type`, `callback`, `priority?`): [`EventManager`](EventManager.md)

添加一个事件监听器，触发一次后自动移除。

#### Type parameters

| Name | Type |
| --- | --- |
| `TEvent` | `any` |

#### Parameters

| Name | Type |
| --- | --- |
| `type` | `string` |
| `callback` | [`TEventCallback`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TEventCallback)<`TEvent`> |
| `priority?` | `number` |

#### Returns

[`EventManager`](EventManager.md)


### clear

▸ **clear**(`type`): [`EventManager`](EventManager.md)

清空某事件的所有监听器。

#### Parameters

| Name | Type |
| --- | --- |
| `type` | `string` |

#### Returns

[`EventManager`](EventManager.md)


### flush

▸ **flush**(`type`): [`EventManager`](EventManager.md)

分发某个缓存的事件，一般不需要自行触发。

#### Parameters

| Name | Type |
| --- | --- |
| `type` | `string` |

#### Returns

[`EventManager`](EventManager.md)


### flushAll

▸ **flushAll**(): [`EventManager`](EventManager.md)

分发所有缓存的事件，一般不需要自行触发。

#### Returns

[`EventManager`](EventManager.md)


### has

▸ **has**(`type`): `boolean`

判断一个事件是否被注册。
注册是指用户绑定过了至少一个事件处理器，无论是来自于wxml还是JS。

#### Parameters

| Name | Type |
| --- | --- |
| `type` | `string` |

#### Returns

`boolean`


### remove

▸ **remove**<`TEvent`>(`type`, `callback`): [`EventManager`](EventManager.md)

移除一个事件监听器。

#### Type parameters

| Name | Type |
| --- | --- |
| `TEvent` | `any` |

#### Parameters

| Name | Type |
| --- | --- |
| `type` | `string` |
| `callback` | [`TEventCallback`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TEventCallback)<`TEvent`> |

#### Returns

[`EventManager`](EventManager.md)


### trigger

▸ **trigger**<`TEvent`>(`type`, `event?`, `immediately?`, `toXML?`, `bubbles?`): [`EventManager`](EventManager.md)

触发一个事件。

#### Type parameters

| Name | Type |
| --- | --- |
| `TEvent` | `any` |

#### Parameters

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `type` | `string` | `undefined` | 要触发的事件类型。 |
| `event?` | `TEvent` | `undefined` | 事件的值。 |
| `immediately` | `boolean` | `true` | 是否要将事件立即分发，如果不则会先缓存，之后在每一帧更新前统一分发，避免不必要的分发。 |
| `toXML` | `boolean` | `true` | 是否要派发到`xml`绑定的事件中。 |
| `bubbles` | `boolean` | `false` | 是否要进行事件冒泡。 |

#### Returns

[`EventManager`](EventManager.md)
