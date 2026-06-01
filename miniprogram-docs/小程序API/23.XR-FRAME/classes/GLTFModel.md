# Class: GLTFModel

> 官方文档：[Class: GLTFModel](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/GLTFModel.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / GLTFModel
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / GLTFModel

加载完毕的GLTF模型，可以在节点下创建[GLTF组件](GLTF.md)来将其实例化。

## Table of contents

### Constructors

- [constructor](GLTFModel.md)

### Properties

- [jsonRaw](GLTFModel.md)

### Methods

- [createFromBuffer](GLTFModel.md)

## Constructors

### constructor

• **new GLTFModel**(`_scene`, `model`)

#### Parameters

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](Scene.md) |
| `model` | `GLTFRootLoaded` |

## Properties

### jsonRaw

• `Readonly` **jsonRaw**: `object`

如果IGLTFLoaderOptions里开启了preserveRaw，则会将原始json保存下来。

## Methods

### createFromBuffer

▸ `Static` **createFromBuffer**(`scene`, `buffer`, `options`): `Promise`<[`GLTFModel`](GLTFModel.md)>

使用GLB文件加载而成的buffer，来生成GLTF模型。

#### Parameters

| Name | Type |
| --- | --- |
| `scene` | [`Scene`](Scene.md) |
| `buffer` | `ArrayBuffer` |
| `options` | [`IGLTFLoaderOptions`](../interfaces/IGLTFLoaderOptions.md) |

#### Returns

`Promise`<[`GLTFModel`](GLTFModel.md)>
