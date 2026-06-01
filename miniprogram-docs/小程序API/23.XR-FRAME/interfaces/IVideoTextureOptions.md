# Interface: IVideoTextureOptions

> 官方文档：[Interface: IVideoTextureOptions](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IVideoTextureOptions.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IVideoTextureOptions
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IVideoTextureOptions

视频纹理[VideoTexture](../classes/VideoTexture.md)的创建参数。

## Table of contents

### Properties

- [abortAudio](IVideoTextureOptions.md)
- [autoPause](IVideoTextureOptions.md)
- [autoPlay](IVideoTextureOptions.md)
- [loop](IVideoTextureOptions.md)
- [placeHolder](IVideoTextureOptions.md)
- [src](IVideoTextureOptions.md)

## Properties

### abortAudio

• `Optional` **abortAudio**: `boolean`

是否禁止音频，默认禁止。


### autoPause

• `Optional` **autoPause**: `boolean`

是否在小程序压后台时自动暂停，默认暂停。


### autoPlay

• `Optional` **autoPlay**: `boolean`

是否要在加载完毕后自动播放。


### loop

• `Optional` **loop**: `boolean`

是否要循环播放。


### placeHolder

• `Optional` **placeHolder**: [`IImage`](IImage.md)

视频未加载成功时，可选的首帧图片地址。


### src

• **src**: `string`

视频地址。
