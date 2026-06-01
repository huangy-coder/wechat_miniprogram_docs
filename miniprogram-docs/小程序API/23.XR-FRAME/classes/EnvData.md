# Class: EnvData

> 官方文档：[Class: EnvData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/EnvData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / EnvData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / EnvData

环境数据资源，一般用[xr-frame-cli](https://github.com/wechat-miniprogram/xr-frame-cli)生成。

## Table of contents

### Constructors

- [constructor](EnvData.md)

### Accessors

- [diffuseSH](EnvData.md)
- [hasDiffuse](EnvData.md)
- [hasSpecular](EnvData.md)
- [skyboxMap](EnvData.md)
- [specularMap](EnvData.md)
- [specularMipmapCount](EnvData.md)
- [specularMipmaps](EnvData.md)
- [specularRGBD](EnvData.md)
- [useHalfSkyMap](EnvData.md)

### Methods

- [destroy](EnvData.md)

## Constructors

### constructor

• **new EnvData**(`options`)

#### Parameters

| Name | Type |
| --- | --- |
| `options` | [`IEnvDataOptions`](../interfaces/IEnvDataOptions.md) |

## Accessors

### diffuseSH

• `get` **diffuseSH**(): `Float32Array`

#### Returns

`Float32Array`


### hasDiffuse

• `get` **hasDiffuse**(): `boolean`

#### Returns

`boolean`


### hasSpecular

• `get` **hasSpecular**(): `boolean`

#### Returns

`boolean`


### skyboxMap

• `get` **skyboxMap**(): `default`

#### Returns

`default`


### specularMap

• `get` **specularMap**(): `default`

#### Returns

`default`


### specularMipmapCount

• `get` **specularMipmapCount**(): `number`

#### Returns

`number`


### specularMipmaps

• `get` **specularMipmaps**(): `boolean`

#### Returns

`boolean`


### specularRGBD

• `get` **specularRGBD**(): `boolean`

#### Returns

`boolean`


### useHalfSkyMap

• `get` **useHalfSkyMap**(): `boolean`

#### Returns

`boolean`

## Methods

### destroy

▸ **destroy**(): `void`

#### Returns

`void`
