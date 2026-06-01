# Class: CubeTextureLoader

> 官方文档：[Class: CubeTextureLoader](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/CubeTextureLoader.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / CubeTextureLoader
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / CubeTextureLoader

立方体资源{@link CubeTexture}的加载器。

内置资源可以通过{@link registerTextureCube}注册，拥有内置资源`brdf-lut`、`white`、`transparent`、`black`、`red`、`green`、`blue`、`yellow`。

## Hierarchy

- [`AssetLoader`](AssetLoader.md)<`Kanata.Texture`, [`ICubeTextureLoaderOptions`](../interfaces/ICubeTextureLoaderOptions.md)> ↳ **`CubeTextureLoader`**

## Table of contents

### Constructors

- [constructor](CubeTextureLoader.md)

### Properties

- [schema](CubeTextureLoader.md)

### Accessors

- [scene](CubeTextureLoader.md)

### Methods

- [cancel](CubeTextureLoader.md)
- [getBuiltin](CubeTextureLoader.md)
- [load](CubeTextureLoader.md)
- [release](CubeTextureLoader.md)

## Constructors

### constructor

• **new CubeTextureLoader**(`_scene`, `type`)

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

详见[ICubeTextureLoaderOptions](../interfaces/ICubeTextureLoaderOptions.md)。

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
| `params` | `IAssetLoadData`<[`ICubeTextureLoaderOptions`](../interfaces/ICubeTextureLoaderOptions.md)> |

#### Returns

`void`

#### Inherited from

[AssetLoader](AssetLoader.md).[cancel](AssetLoader.md)


### getBuiltin

▸ **getBuiltin**(): { `assetId`: `string` ; `options`: [`ICubeTextureLoaderOptions`](../interfaces/ICubeTextureLoaderOptions.md) ; `src`: `string` }[]

返回默认资源列表。
所有默认资源都是惰性加载的。

#### Returns

{ `assetId`: `string` ; `options`: [`ICubeTextureLoaderOptions`](../interfaces/ICubeTextureLoaderOptions.md) ; `src`: `string` }[]

#### Inherited from

[AssetLoader](AssetLoader.md).[getBuiltin](AssetLoader.md)


### load

▸ **load**(`params`, `callbacks`): `void`

加载一个资源，并根据情况执行`callbacks`中的回调。
**理论上必须要实现！**

#### Parameters

| Name | Type |
| --- | --- |
| `params` | `ICubeTextureLoadData` |
| `callbacks` | `Object` |
| `callbacks.onError` | (`error`: `Error`) => `void` |
| `callbacks.onLoaded` | (`value`: `default`) => `void` |
| `callbacks.onLoading` | (`progress`: `number`) => `void` |

#### Returns

`void`

#### Overrides

[AssetLoader](AssetLoader.md).[load](AssetLoader.md)


### release

▸ **release**(`params`, `value`): `void`

释放资源时将会调用，用于自定义释放逻辑。

#### Parameters

| Name | Type |
| --- | --- |
| `params` | `ICubeTextureLoadData` |
| `value` | `default` |

#### Returns

`void`

#### Overrides

[AssetLoader](AssetLoader.md).[release](AssetLoader.md)
