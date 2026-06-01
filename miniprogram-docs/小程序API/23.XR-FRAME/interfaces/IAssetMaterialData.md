# Interface: IAssetMaterialData

> 官方文档：[Interface: IAssetMaterialData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAssetMaterialData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IAssetMaterialData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IAssetMaterialData

`AssetMaterial`数据接口。

## Table of contents

### Properties

- [assetId](IAssetMaterialData.md)
- [effect](IAssetMaterialData.md)
- [envData](IAssetMaterialData.md)
- [renderQueue](IAssetMaterialData.md)
- [states](IAssetMaterialData.md)
- [uniforms](IAssetMaterialData.md)

## Properties

### assetId

• **assetId**: `string`

被引用时的资源Id。
`xml`中的数据类型为`string`。


### effect

• **effect**: [`Effect`](../classes/Effect.md)

基于的效果。
`xml`中的数据类型为`effect`资源，默认为`simple`。


### envData

• `Optional` **envData**: [`EnvData`](../classes/EnvData.md)

用于覆盖全局的、材质维度的环境数据。


### renderQueue

• **renderQueue**: `number`

要覆盖的渲染顺序。
`xml`中的数据类型为`number`，无默认值。
大于等于`2500`视为透明物体。


### states

• **states**: [`string`, `string`][]

初始要写入的渲染状态`states`。
`xml`中的数据类型为`map`。
目前支持`renderQueue`、`cullOn`、`depthTestOn`、`depthTestWrite`、`alphaMode`、`alphaCutOff`。
`alphaMode`和`alphaCutOff`遵循glTF标准。


### uniforms

• **uniforms**: [`string`, `string`][]

初始要写入的`uniforms`，类型根据`effect`中的定义决定。
`xml`中的数据类型为`map`。
