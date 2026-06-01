# Interface: ICubeTextureLoaderOptions

> 官方文档：[Interface: ICubeTextureLoaderOptions](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ICubeTextureLoaderOptions.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / ICubeTextureLoaderOptions
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / ICubeTextureLoaderOptions

[CubeTextureLoader](../classes/CubeTextureLoader.md)可接受的自定义参数`schema`。

## Table of contents

### Properties

- [anisoLevel](ICubeTextureLoaderOptions.md)
- [faces](ICubeTextureLoaderOptions.md)
- [generateMipmaps](ICubeTextureLoaderOptions.md)
- [magFilter](ICubeTextureLoaderOptions.md)
- [minFilter](ICubeTextureLoaderOptions.md)
- [wrapU](ICubeTextureLoaderOptions.md)
- [wrapV](ICubeTextureLoaderOptions.md)
- [wrapW](ICubeTextureLoaderOptions.md)

## Properties

### anisoLevel

• **anisoLevel**: `number`

各向异性系数。

**`default`** 1


### faces

• **faces**: `string`[]

顺序为 left right top bottom front back。


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


### wrapW

• `Optional` **wrapW**: `number`

wrapW，值为数字，见[EWrapMode](../enums/EWrapMode.md)。

**`default`** 2
