# Interface: ITextureOptions

> 官方文档：[Interface: ITextureOptions](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ITextureOptions.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / ITextureOptions
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / ITextureOptions

纹理资源[Texture](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#Texture)的创建参数。

## Table of contents

### Properties

- [anisoLevel](ITextureOptions.md)
- [generateMipmaps](ITextureOptions.md)
- [height](ITextureOptions.md)
- [magFilter](ITextureOptions.md)
- [minFilter](ITextureOptions.md)
- [mips](ITextureOptions.md)
- [offsets](ITextureOptions.md)
- [pixelFormat](ITextureOptions.md)
- [slices](ITextureOptions.md)
- [source](ITextureOptions.md)
- [type](ITextureOptions.md)
- [width](ITextureOptions.md)
- [wrapU](ITextureOptions.md)
- [wrapV](ITextureOptions.md)
- [wrapW](ITextureOptions.md)

## Properties

### anisoLevel

• `Optional` **anisoLevel**: `number`

各向异性等级。


### generateMipmaps

• `Optional` **generateMipmaps**: `boolean`

是否要自动生成`mipmaps`，仅对非压缩纹理有效。


### height

• `Optional` **height**: `number`

纹理高，如果`source`是`IImage`可以不传。


### magFilter

• `Optional` **magFilter**: [`EFilterMode`](../enums/EFilterMode.md)


### minFilter

• `Optional` **minFilter**: [`EFilterMode`](../enums/EFilterMode.md)


### mips

• `Optional` **mips**: `number`

纹理有多少级`mipmap`。


### offsets

• `Optional` **offsets**: `Uint32Array`

当`source`为`Buffer`纹理并且拥有`mipmaps`之类的时，标记如何切割数据。
规则是: off1, size1, off2, size2......


### pixelFormat

• `Optional` **pixelFormat**: [`ETextureFormat`](../enums/ETextureFormat.md)

纹理的像素格式。


### slices

• `Optional` **slices**: `number`

纹理有多少切片，比如立方体纹理就为`6`。


### source

• `Optional` **source**: `TTextureSource`[]

纹理数据源，如果是2D纹理，一般只能有一个元素。如果是`Buffer`类型数据，比如压缩纹理，则需要和`offsets`配合使用，一般用于`mipmaps`的场合。
如果是立方体纹理，则有六个元素。


### type

• `Optional` **type**: [`ETextureType`](../enums/ETextureType.md)

纹理类型。


### width

• `Optional` **width**: `number`

纹理宽，如果`source`是`IImage`可以不传。


### wrapU

• `Optional` **wrapU**: [`EWrapMode`](../enums/EWrapMode.md)


### wrapV

• `Optional` **wrapV**: [`EWrapMode`](../enums/EWrapMode.md)


### wrapW

• `Optional` **wrapW**: [`EWrapMode`](../enums/EWrapMode.md)
