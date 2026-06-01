# Class: GLTFLoader

> 官方文档：[Class: GLTFLoader](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GlTFLoader.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / GLTFLoader
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / GLTFLoader

GLTF资源加载器，加载完毕后返回一个[GLTFModel](GLTFModel.md)。

## Hierarchy

- [`AssetLoader`](AssetLoader.md)<[`GLTFModel`](GLTFModel.md), [`IGLTFLoaderOptions`](../interfaces/IGLTFLoaderOptions.md)> ↳ **`GLTFLoader`**

## Table of contents

### Constructors

- [constructor](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GLTFLoader.html#constructor)

### Properties

- [schema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GLTFLoader.html#schema)

### Accessors

- [scene](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GLTFLoader.html#scene)

### Methods

- [cancel](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GLTFLoader.html#cancel)
- [getBuiltin](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GLTFLoader.html#getBuiltin)
- [load](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GLTFLoader.html#load)
- [release](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GLTFLoader.html#release)

## Constructors

### constructor

• **new GLTFLoader**(`_scene`, `type`)

#### Parameters

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](Scene.md) |
| `type` | `string` |

#### Inherited from

[AssetLoader](AssetLoader.md).[constructor](AssetLoader.md)

## Properties

### schema

• `Readonly` **schema**: [`ILoaderOptionsSchema`](../interfaces/ILoaderOptionsSchema.md)

和[Component.schema](Component.md)类似，指定解析Options的实际`schema`，对应于`ILoadOptions`。

#### Overrides

[AssetLoader](AssetLoader.md).[schema](AssetLoader.md)

## Accessors

### scene

• `get` **scene**(): [`Scene`](Scene.md)

当前资源所属场景的实例。

#### Returns

[`Scene`](Scene.md)

## Methods

### cancel

▸ **cancel**(`params`): `void`

取消加载特定资源。一般不需要自己编写逻辑，而是使用`entity.canceled`在加载终点丢弃。
注意`entity.canceled`是在这里赋值的，所以一般继承请务必先执行`super.cancel()`！

#### Parameters

| Name | Type |
| --- | --- |
| `params` | `IGLTFLoadData` |

#### Returns

`void`

#### Overrides

[AssetLoader](AssetLoader.md).[cancel](AssetLoader.md)


### getBuiltin

▸ **getBuiltin**(): { `assetId`: `string` ; `options`: [`IGLTFLoaderOptions`](../interfaces/IGLTFLoaderOptions.md) ; `src`: `string` }[]

返回默认资源列表。
所有默认资源都是惰性加载的。

#### Returns

{ `assetId`: `string` ; `options`: [`IGLTFLoaderOptions`](../interfaces/IGLTFLoaderOptions.md) ; `src`: `string` }[]

#### Inherited from

[AssetLoader](AssetLoader.md).[getBuiltin](AssetLoader.md)


### load

▸ **load**(`param`, `callbacks`): `Promise`<`void`>

加载一个资源，并根据情况执行`callbacks`中的回调。
**理论上必须要实现！**

#### Parameters

| Name | Type |
| --- | --- |
| `param` | `IGLTFLoadData` |
| `callbacks` | `Object` |
| `callbacks.onError` | (`error`: `Error`) => `void` |
| `callbacks.onLoaded` | (`value`: [`GLTFModel`](GLTFModel.md)) => `void` |
| `callbacks.onLoading` | (`progress`: `number`) => `void` |

#### Returns

`Promise`<`void`>

#### Overrides

[AssetLoader](AssetLoader.md).[load](AssetLoader.md)


### release

▸ **release**(`params`, `value`): `void`

释放资源时将会调用，用于自定义释放逻辑。

#### Parameters

| Name | Type |
| --- | --- |
| `params` | `IGLTFLoadData` |
| `value` | [`GLTFModel`](GLTFModel.md) |

#### Returns

`void`

#### Overrides

[AssetLoader](AssetLoader.md).[release](AssetLoader.md)
