# Class: Geometry

> 官方文档：[Class: Geometry](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Geometry.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Geometry
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Geometry

几何资源，用于定义渲染中的图元数据。

## Table of contents

### Constructors

- [constructor](Geometry.md)

### Accessors

- [boundBall](Geometry.md)
- [boundBox](Geometry.md)
- [indexBuffer](Geometry.md)
- [indexData](Geometry.md)
- [vertexBuffer](Geometry.md)
- [vertexData](Geometry.md)
- [vertexLayout](Geometry.md)

### Methods

- [addSubMesh](Geometry.md)
- [getIndiceLength](Geometry.md)
- [getIndiceStart](Geometry.md)
- [getMaterialIndex](Geometry.md)
- [getSubMeshCount](Geometry.md)
- [getVertexLayout](Geometry.md)
- [modifySubMesh](Geometry.md)
- [setBoundBall](Geometry.md)
- [setBoundBox](Geometry.md)
- [uploadIndexBuffer](Geometry.md)
- [uploadVertexBuffer](Geometry.md)

## Constructors

### constructor

• **new Geometry**(`_scene`, `vertexLayout`, `vBuffer`, `iBuffer`, `indexType?`)

构造一个`Geometry`。

#### Parameters

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](Scene.md) |
| `vertexLayout` | `default` |
| `vBuffer` | `ArrayBufferView` |
| `iBuffer` | `ArrayBufferView` |
| `indexType` | [`EIndexType`](../enums/EIndexType.md) |

## Accessors

### boundBall

• `get` **boundBall**(): [`BoundBall`](BoundBall.md)

包围球，只读。

#### Returns

[`BoundBall`](BoundBall.md)


### boundBox

• `get` **boundBox**(): [`BoundBox`](BoundBox.md)

包围盒，只读。

#### Returns

[`BoundBox`](BoundBox.md)


### indexBuffer

• `get` **indexBuffer**(): `default`

获取IndexBuffer。

#### Returns

`default`


### indexData

• `get` **indexData**(): `default`

获取IndexData。
这种类型的索引数据用于合批，只对于开启了`dynamicBatch`的Renderer有效。
注意如果已经获取过`indexBuffer`，将无效。

#### Returns

`default`


### vertexBuffer

• `get` **vertexBuffer**(): `default`

获取VertexBuffer。

#### Returns

`default`


### vertexData

• `get` **vertexData**(): `default`

获取VertexData。
这种类型的顶点数据用于合批，只对于开启了`dynamicBatch`的Renderer有效。
注意如果已经获取过`vertexBuffer`，将无效。

#### Returns

`default`


### vertexLayout

• `get` **vertexLayout**(): `default`

获取VertexLayout。

#### Returns

`default`

## Methods

### addSubMesh

▸ **addSubMesh**(`length`, `offset`, `materialIndex?`): `void`

增加subMesh。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `length` | `number` | 索引长度 |
| `offset` | `number` | 索引起始偏移 |
| `materialIndex?` | `number` | - |

#### Returns

`void`


### getIndiceLength

▸ **getIndiceLength**(`subMeshIndex`): `number`

获取指定序号的subMesh的索引长度

#### Parameters

| Name | Type |
| --- | --- |
| `subMeshIndex` | `number` |

#### Returns

`number`

索引长度，返回-1代表SubMesh不存在


### getIndiceStart

▸ **getIndiceStart**(`subMeshIndex`): `number`

获取指定序号的subMesh的索引起始点

#### Parameters

| Name | Type |
| --- | --- |
| `subMeshIndex` | `number` |

#### Returns

`number`

索引起始点,返回-1代表SubMesh不存在


### getMaterialIndex

▸ **getMaterialIndex**(`subMeshIndex`): `number`

获取指定序号的subMesh的材质序号

#### Parameters

| Name | Type |
| --- | --- |
| `subMeshIndex` | `number` |

#### Returns

`number`

材质序号，返回-1代表subMesh不存在


### getSubMeshCount

▸ **getSubMeshCount**(): `number`

获取当前mesh有多少subMesh

#### Returns

`number`


### getVertexLayout

▸ **getVertexLayout**(): `default`

获取VertexLayout。

#### Returns

`default`


### modifySubMesh

▸ **modifySubMesh**(`subMeshIndex`, `length`, `offset`): `boolean`

修改subMesh。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `subMeshIndex` | `number` | - |
| `length` | `number` | 索引长度 |
| `offset` | `number` | 索引起始偏移 |

#### Returns

`boolean`


### setBoundBall

▸ **setBoundBall**(`center`, `radius`): `void`

动态更新包围球。

#### Parameters

| Name | Type |
| --- | --- |
| `center` | [`Vector3`](Vector3.md) |
| `radius` | `number` |

#### Returns

`void`


### setBoundBox

▸ **setBoundBox**(`center`, `size`, `autoUpdateBall?`): `void`

动态更新包围盒，默认会自动计算包围球。

#### Parameters

| Name | Type | Default value |
| --- | --- | --- |
| `center` | [`Vector3`](Vector3.md) | `undefined` |
| `size` | [`Vector3`](Vector3.md) | `undefined` |
| `autoUpdateBall` | `boolean` | `true` |

#### Returns

`void`


### uploadIndexBuffer

▸ **uploadIndexBuffer**(`offset`, `buffer`): `void`

更新IndexBuffer。
仅在获取了`indexBuffer`后有效。

#### Parameters

| Name | Type |
| --- | --- |
| `offset` | `number` |
| `buffer` | `Uint16Array` \| `Uint32Array` |

#### Returns

`void`


### uploadVertexBuffer

▸ **uploadVertexBuffer**(`offset`, `buffer`): `void`

更新VertexBuffer。
仅在获取了`vertexBuffer`后有效。

#### Parameters

| Name | Type |
| --- | --- |
| `offset` | `number` |
| `buffer` | `ArrayBufferView` |

#### Returns

`void`
