# Interface: IGLTFData

> 官方文档：[Interface: IGLTFData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IGLTFData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IGLTFData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IGLTFData

**`see`** [GLTF](../classes/GLTF.md)

## Table of contents

### Properties

- [castShadow](IGLTFData.md)
- [model](IGLTFData.md)
- [neverCull](IGLTFData.md)
- [receiveShadow](IGLTFData.md)
- [states](IGLTFData.md)

## Properties

### castShadow

• `Optional` **castShadow**: `boolean`

是否投射阴影，默认false。


### model

• **model**: [`GLTFModel`](../classes/GLTFModel.md)

已加载完毕的GLTF模型。


### neverCull

• `Optional` **neverCull**: `boolean`

是否不参与剔除，默认false(即参与剔除)。


### receiveShadow

• `Optional` **receiveShadow**: `boolean`

是否接受阴影，默认false。


### states

• `Optional` **states**: [`string`, `string`][]

修改GLTF的默认renderStates。
