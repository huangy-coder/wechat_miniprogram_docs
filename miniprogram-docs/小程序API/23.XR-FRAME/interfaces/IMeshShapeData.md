# Interface: IMeshShapeData

> 官方文档：[Interface: IMeshShapeData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IMeshShapeData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IMeshShapeData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IMeshShapeData

**`see`** [MeshShape](../classes/MeshShape.md)

## Hierarchy

- [`IShapeData`](IShapeData.md) ↳ **`IMeshShapeData`**

## Table of contents

### Properties

- [autoFit](IMeshShapeData.md)
- [center](IMeshShapeData.md)
- [convex](IMeshShapeData.md)
- [disabled](IMeshShapeData.md)

## Properties

### autoFit

• `Optional` **autoFit**: `boolean`

轮廓是否自动贴合[Mesh组件](../classes/Mesh.md)或[GLTF组件](../classes/GLTF.md)的大小。
如果当前元素下不存在Mesh组件和GLTF组件则不生效。

> [MeshShape](../classes/MeshShape.md)永远会开启这项。

**`default`** false

#### Inherited from

[IShapeData](IShapeData.md).[autoFit](IShapeData.md)


### center

• `Optional` **center**: [`number`, `number`, `number`]

轮廓中心相对元素[Transform](../classes/Transform.md)中心的偏移量。

**`default`** [0, 0, 0]

#### Inherited from

[IShapeData](IShapeData.md).[center](IShapeData.md)


### convex

• `Optional` **convex**: `boolean`

是否使用凸多边形来包围Mesh。
*如果元素有`shape-interact`属性，则会强制开启。*

**`default`** false


### disabled

• `Optional` **disabled**: `boolean`

是否禁用shape。

**`default`** false

#### Inherited from

[IShapeData](IShapeData.md).[disabled](IShapeData.md)
