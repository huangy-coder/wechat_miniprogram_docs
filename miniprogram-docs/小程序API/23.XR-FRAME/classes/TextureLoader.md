# Class: TextureLoader

> 官方文档：[Class: TextureLoader](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/TextureLoader.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / TextureLoader
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / TextureLoader

纹理资源[Texture](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#Texture)的加载器。

内置资源可以通过[registerTexture](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#registerTexture)注册，拥有内置资源`brdf-lut`、`white`、`transparent`、`black`、`red`、`green`、`blue`、`yellow`、`babyblue`、`babygreen`、`babyred`。

## Hierarchy

- [`AssetLoader`](AssetLoader.md)<`Kanata.Texture`, [`ITextureLoaderOptions`](../interfaces/ITextureLoaderOptions.md)> ↳ **`TextureLoader`**

## Table of contents

### Constructors

- [constructor](TextureLoader.md)

### Properties

- [schema](TextureLoader.md)

### Accessors

- [scene](TextureLoader.md)

### Methods

- [cancel](TextureLoader.md)
- [getBuiltin](TextureLoader.md)
- [load](TextureLoader.md)
- [release](TextureLoader.md)

## Constructors

### constructor

• **new TextureLoader**(`_scene`, `type`)

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
| `params` | `IAssetLoadData`<[`ITextureLoaderOptions`](../interfaces/ITextureLoaderOptions.md)> |

#### Returns

`void`

#### Inherited from

[AssetLoader](AssetLoader.md).[cancel](AssetLoader.md)


### getBuiltin

▸ **getBuiltin**(): { `assetId`: `string` = 'brdf-lut'; `options`: {} = {}; `src`: `string` = 'https://mmbizwxaminiprogram-1258344707.cos.ap-guangzhou.myqcloud.com/xr-frame/brdflut.png' }[]

返回默认资源列表。
所有默认资源都是惰性加载的。

#### Returns

{ `assetId`: `string` = 'brdf-lut'; `options`: {} = {}; `src`: `string` = 'https://mmbizwxaminiprogram-1258344707.cos.ap-guangzhou.myqcloud.com/xr-frame/brdflut.png' }[]

#### Overrides

[AssetLoader](AssetLoader.md).[getBuiltin](AssetLoader.md)


### load

▸ **load**(`params`, `callbacks`): `void`

加载一个资源，并根据情况执行`callbacks`中的回调。
**理论上必须要实现！**

#### Parameters

| Name | Type |
| --- | --- |
| `params` | `ITextureLoadData` |
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
| `params` | `ITextureLoadData` |
| `value` | `default` |

#### Returns

`void`

#### Overrides

[AssetLoader](AssetLoader.md).[release](AssetLoader.md)
