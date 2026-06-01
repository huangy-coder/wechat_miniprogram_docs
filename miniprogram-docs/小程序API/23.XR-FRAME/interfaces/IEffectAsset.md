# Interface: IEffectAsset

> 官方文档：[Interface: IEffectAsset](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IEffectAsset.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IEffectAsset
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IEffectAsset

`Effect`资源的参数接口。

## Table of contents

### Properties

- [defaultRenderQueue](IEffectAsset.md)
- [images](IEffectAsset.md)
- [name](IEffectAsset.md)
- [passes](IEffectAsset.md)
- [properties](IEffectAsset.md)
- [shaders](IEffectAsset.md)

## Properties

### defaultRenderQueue

• **defaultRenderQueue**: `number`

使用该`Effect`的`Material`的默认渲染队列。
透明物体需要大于`2500`！


### images

• `Optional` **images**: { `default`: `string` ; `key`: `string` ; `macro?`: `string` }[]

纹理资源，传给UniformBlock的另一部分。


### name

• **name**: `string`

名字，应当和`registerEffect`时的名字一致。


### passes

• **passes**: { `lightMode`: `string` ; `renderStates?`: [`IRenderStates`](IRenderStates.md) ; `shaders`: [`number`, `number`] ; `useMaterialRenderStates`: `boolean` }[]

渲染时的`passes`，渲染时指定的`lightMode`的每个`pass`都会被按顺序绘制。


### properties

• `Optional` **properties**: { `default`: `number`[] ; `key`: `string` ; `macro?`: `string` ; `num?`: `number` ; `type`: [`EUniformType`](../enums/EUniformType.md) }[]

属性，传给UniformBlock的一部分。


### shaders

• **shaders**: `string`[]

所有的`shader`列表。
