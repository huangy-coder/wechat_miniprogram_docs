# Interface: IAtlasOptions

> 官方文档：[Interface: IAtlasOptions](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAtlasOptions.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IAtlasOptions
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IAtlasOptions

`Atlas`的初始化参数类型。

## Table of contents

### Properties

- [frames](IAtlasOptions.md)
- [image](IAtlasOptions.md)
- [meta](IAtlasOptions.md)
- [texture](IAtlasOptions.md)

## Properties

### frames

• **frames**: `Object`

帧定义，若不指定`uv`则会自动按比例计算。

#### Index signature

▪ [key: `string`]: { `frame`: { `h`: `number` ; `w`: `number` ; `x`: `number` ; `y`: `number` } }


### image

• `Optional` **image**: [`IImage`](IImage.md)

图片。


### meta

• **meta**: `Object`

原信息，主要定义图片尺寸。

#### Type declaration

| Name | Type |
| --- | --- |
| `size` | { `h`: `number` ; `w`: `number` } |
| `size.h` | `number` |
| `size.w` | `number` |


### texture

• `Optional` **texture**: `default`

也可以直接传入一张纹理。
