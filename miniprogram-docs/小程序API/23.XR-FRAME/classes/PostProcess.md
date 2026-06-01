# Class: PostProcess

> 官方文档：[Class: PostProcess](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/PostProcess.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / PostProcess
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / PostProcess

后处理资源。

一般由[AssetPostProcess](AssetPostProcess.md)加载。

## Table of contents

### Constructors

- [constructor](PostProcess.md)

### Accessors

- [data](PostProcess.md)
- [isHDR](PostProcess.md)
- [type](PostProcess.md)

## Constructors

### constructor

• **new PostProcess**(`_scene`, `options`)

#### Parameters

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](Scene.md) |
| `options` | [`IPostProcessOptions`](../interfaces/IPostProcessOptions.md) |

## Accessors

### data

• `get` **data**(): `Object`

数据，可以修改。

#### Returns

`Object`


### isHDR

• `get` **isHDR**(): `boolean`

是否开启了HDR。

#### Returns

`boolean`


### type

• `get` **type**(): `string`

类型。

#### Returns

`string`
