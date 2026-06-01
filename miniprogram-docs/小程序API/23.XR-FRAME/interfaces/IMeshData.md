# Interface: IMeshData

> 官方文档：[Interface: IMeshData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IMeshData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IMeshData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IMeshData

`Mesh`数据接口。

## Table of contents

### Properties

- [castShadow](IMeshData.md)
- [envData](IMeshData.md)
- [geometry](IMeshData.md)
- [material](IMeshData.md)
- [neverCull](IMeshData.md)
- [receiveShadow](IMeshData.md)
- [states](IMeshData.md)
- [uniforms](IMeshData.md)

## Properties

### castShadow

• `Optional` **castShadow**: `boolean`

在主光源产生阴影开启阴影时，是否要产生阴影。
`xml`中的数据类型为`boolean`，默认为`false`。


### envData

• `Optional` **envData**: [`EnvData`](../classes/EnvData.md)

用于覆盖`material`中的，全局的、材质维度的环境数据。

- `xml`中同[IAssetMaterialData.envData](IAssetMaterialData.md)。


### geometry

• **geometry**: [`Geometry`](../classes/Geometry.md)

渲染使用的几何数据。
`xml`中的数据类型为`geometry`资源。


### material

• `Optional` **material**: [`Material`](../classes/Material.md)

渲染使用的材质数据。
`xml`中的数据类型为`material`资源。


### neverCull

• `Optional` **neverCull**: `boolean`

是否强制不被剔除。
`xml`中的数据类型为`boolean`，默认为`false`。


### receiveShadow

• `Optional` **receiveShadow**: `boolean`

在主光源产生阴影开启阴影时，是否要接受阴影。
`xml`中的数据类型为`boolean`，默认为`false`。


### states

• `Optional` **states**: [`string`, `string`][]

覆盖`material`中的默认`states`，如果覆盖了，则会先创建一个材质副本。
`xml`中同[IAssetMaterialData.states](IAssetMaterialData.md)。


### uniforms

• `Optional` **uniforms**: [`string`, `string`][]

覆盖`material`中的默认`uniforms`，如果覆盖了，则会先创建一个材质副本。
`xml`中同[IAssetMaterialData.uniforms](IAssetMaterialData.md)。
