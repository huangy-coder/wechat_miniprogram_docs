# Class: AssetLoader<T, ILoadOptions>

> 官方文档：[Class: AssetLoader<T, ILoadOptions>](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AssetLoader.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / AssetLoader
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / AssetLoader

资源加载器的基类，配合[AssetsSystem](AssetsSystem.md)使用。
在基础库版本**v2.29.2**以上导出。

## Type parameters

| Name | Description |
| --- | --- |
| `T` | 加载资源的类型。 |
| `ILoadOptions` | 可接受额外配置的类型。 |

## Hierarchy

- **`AssetLoader`** ↳ [`TextureLoader`](TextureLoader.md) ↳ [`ImageLoader`](ImageLoader.md) ↳ [`CubeTextureLoader`](CubeTextureLoader.md) ↳ [`VideoTextureLoader`](VideoTextureLoader.md) ↳ [`EnvDataLoader`](EnvDataLoader.md) ↳ [`GLTFLoader`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GLTFLoader.html) ↳ [`KeyframeLoader`](KeyframeLoader.md) ↳ [`RawLoader`](RawLoader.md) ↳ [`AtlasLoader`](AtlasLoader.md)

## Table of contents

### Constructors

- [constructor](AssetLoader.md)

### Properties

- [schema](AssetLoader.md)

### Accessors

- [scene](AssetLoader.md)

### Methods

- [cancel](AssetLoader.md)
- [getBuiltin](AssetLoader.md)
- [load](AssetLoader.md)
- [release](AssetLoader.md)

## Constructors

### constructor

• **new AssetLoader**<`T`, `ILoadOptions`>(`_scene`, `type`)

#### Type parameters

| Name |
| --- |
| `T` |
| `ILoadOptions` |

#### Parameters

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](Scene.md) |
| `type` | `string` |

## Properties

### schema

• `Readonly` **schema**: [`ILoaderOptionsSchema`](../interfaces/ILoaderOptionsSchema.md) = `{}`

和[Component.schema](Component.md)类似，指定解析Options的实际`schema`，对应于`ILoadOptions`。

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
| `params` | `IAssetLoadData`<`ILoadOptions`> |

#### Returns

`void`


### getBuiltin

▸ **getBuiltin**(): { `assetId`: `string` ; `options`: `ILoadOptions` ; `src`: `string` }[]

返回默认资源列表。
所有默认资源都是惰性加载的。

#### Returns

{ `assetId`: `string` ; `options`: `ILoadOptions` ; `src`: `string` }[]


### load

▸ **load**(`data`, `callbacks`): `void`

加载一个资源，并根据情况执行`callbacks`中的回调。
**理论上必须要实现！**

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `data` | `IAssetLoadData`<`ILoadOptions`> | - |
| `callbacks` | `Object` | 开发者需要在加载进度更新时执行`onLoading`，在加载完成时执行`onLoaded`，在加载出错是执行`onError` |
| `callbacks.onError` | (`error`: `Error`) => `void` | - |
| `callbacks.onLoaded` | (`result`: `T`, `localPath?`: `string`) => `void` | - |
| `callbacks.onLoading` | (`progress`: `number`) => `void` | - |

#### Returns

`void`


### release

▸ **release**(`params`, `value`): `void`

释放资源时将会调用，用于自定义释放逻辑。

#### Parameters

| Name | Type |
| --- | --- |
| `params` | `IAssetLoadData`<`ILoadOptions`> |
| `value` | `T` |

#### Returns

`void`
