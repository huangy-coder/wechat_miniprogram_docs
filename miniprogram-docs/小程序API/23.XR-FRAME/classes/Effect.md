# Class: Effect

> 官方文档：[Class: Effect](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Effect.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Effect
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Effect

特效资源，定义了渲染所需的大部分参数，被[Material](Material.md)所引用。

## Table of contents

### Constructors

- [constructor](Effect.md)

### Properties

- [description](Effect.md)

### Accessors

- [name](Effect.md)
- [passCount](Effect.md)
- [scene](Effect.md)

### Methods

- [warmUp](Effect.md)

## Constructors

### constructor

• **new Effect**(`_scene`, `description`)

根据特效配置生成特效资源。
**注意，不建议自己创建，请使用`scene.createEffect`。**

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `_scene` | [`Scene`](Scene.md) | - |
| `description` | [`IEffectAsset`](../interfaces/IEffectAsset.md) | 配置。 |

## Properties

### description

• `Readonly` **description**: [`IEffectAsset`](../interfaces/IEffectAsset.md)

## Accessors

### name

• `get` **name**(): `string`

获取名称。

#### Returns

`string`


### passCount

• `get` **passCount**(): `number`

有几个Pass。

#### Returns

`number`


### scene

• `get` **scene**(): [`Scene`](Scene.md)

获取场景实例。

#### Returns

[`Scene`](Scene.md)

## Methods

### warmUp

▸ **warmUp**(): `boolean`

预编译

#### Returns

`boolean`
