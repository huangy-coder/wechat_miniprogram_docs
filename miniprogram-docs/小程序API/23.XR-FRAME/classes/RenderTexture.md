# Class: RenderTexture

> 官方文档：[Class: RenderTexture](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/RenderTexture.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / RenderTexture
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / RenderTexture

渲染纹理组件，可作为{@link Camera.renderTarget}。

## Table of contents

### Constructors

- [constructor](RenderTexture.md)

### Properties

- [isRenderTexture](RenderTexture.md)

### Accessors

- [height](RenderTexture.md)
- [id](RenderTexture.md)
- [width](RenderTexture.md)

### Methods

- [IS](RenderTexture.md)

## Constructors

### constructor

• **new RenderTexture**(`_scene`, `options`)

#### Parameters

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](Scene.md) |
| `options` | [`IRenderTextureOptions`](../interfaces/IRenderTextureOptions.md) |

## Properties

### isRenderTexture

• `Readonly` **isRenderTexture**: `boolean` = `true`

## Accessors

### height

• `get` **height**(): `number`

贴图高。

#### Returns

`number`


### id

• `get` **id**(): `number`

#### Returns

`number`


### width

• `get` **width**(): `number`

贴图宽。

#### Returns

`number`

## Methods

### IS

▸ `Static` **IS**(`obj`): obj is RenderTexture

#### Parameters

| Name | Type |
| --- | --- |
| `obj` | `any` |

#### Returns

obj is RenderTexture
