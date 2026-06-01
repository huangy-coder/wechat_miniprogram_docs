# Interface: ITextureLoaderOptions

> 官方文档：[Interface: ITextureLoaderOptions](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ITextureLoaderOptions.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / ITextureLoaderOptions
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / ITextureLoaderOptions

[TextureLoader](../classes/TextureLoader.md)可接受的自定义参数`schema`。

## Table of contents

### Properties

- [anisoLevel](ITextureLoaderOptions.md)
- [generateMipmaps](ITextureLoaderOptions.md)
- [magFilter](ITextureLoaderOptions.md)
- [minFilter](ITextureLoaderOptions.md)
- [wrapU](ITextureLoaderOptions.md)
- [wrapV](ITextureLoaderOptions.md)

## Properties

### anisoLevel

• `Optional` **anisoLevel**: `number`

各向异性系数。

**`default`** 1


### generateMipmaps

• `Optional` **generateMipmaps**: `boolean`

是否要生成mipmaps。

**`default`** false


### magFilter

• `Optional` **magFilter**: `number`

magFilter，值为数字，见[EFilterMode](../enums/EFilterMode.md)。
默认值依据纹理是否POT而定。


### minFilter

• `Optional` **minFilter**: `number`

minFilter，值为数字，见[EFilterMode](../enums/EFilterMode.md)。
默认值依据纹理是否POT而定。


### wrapU

• `Optional` **wrapU**: `number`

wrapU，值为数字，见[EWrapMode](../enums/EWrapMode.md)。

**`default`** 2


### wrapV

• `Optional` **wrapV**: `number`

wrapV，值为数字，见[EWrapMode](../enums/EWrapMode.md)。

**`default`** 2
