# Interface: IImage

> 官方文档：[Interface: IImage](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IImage.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IImage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IImage

引擎原生图片接口。

## Table of contents

### Properties

- [autoRelease](IImage.md)
- [data](IImage.md)
- [height](IImage.md)
- [localPath](IImage.md)
- [onerror](IImage.md)
- [onload](IImage.md)
- [premultiplyAlpha](IImage.md)
- [src](IImage.md)
- [type](IImage.md)
- [width](IImage.md)

## Properties

### autoRelease

• `Optional` **autoRelease**: `boolean`

对于`ArrayBuffer`创建的图片，第一次使用后是否要自动释放内存，在`xr-frame`中，默认自动释放。


### data

• `Optional` `Readonly` **data**: `ArrayBuffer` | `HTMLImageElement`

解码数据，视不同Backend而定。


### height

• **height**: `number`

图片高度。


### localPath

• `Optional` **localPath**: `string`

图片本地缓存地址，仅在微信内有用。


### onerror

• **onerror**: (`error`: `Error`) => `void`

#### Type declaration

▸ (`error`): `void`

出错的回调。

##### Parameters

| Name | Type |
| --- | --- |
| `error` | `Error` |

##### Returns

`void`


### onload

• **onload**: () => `void`

#### Type declaration

▸ (): `void`

加载完成的回调。

##### Returns

`void`


### premultiplyAlpha

• **premultiplyAlpha**: `boolean`

是否要预乘Alpha。


### src

• **src**: `string` | `ArrayBufferView` | `ArrayBuffer`

图片地址或者待解码的ArrayBuffer。


### type

• `Optional` **type**: `string`

图片源于ArrayBuffer时，传入的mimetype。


### width

• **width**: `number`

图片宽度。
