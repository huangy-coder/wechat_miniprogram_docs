# Class: Atlas

> 官方文档：[Class: Atlas](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Atlas.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Atlas
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Atlas

图集资源。

**`version`** 2.27.1

一般通过[AtlasLoader](AtlasLoader.md)加载自动生成。
推荐使用[Shoebox](https://www.renderhjs.net/shoebox/)等工具生成。

## Table of contents

### Constructors

- [constructor](Atlas.md)

### Properties

- [isAtlas](Atlas.md)

### Accessors

- [frames](Atlas.md)
- [meta](Atlas.md)
- [texture](Atlas.md)

### Methods

- [getFrame](Atlas.md)
- [getUVMatrix](Atlas.md)
- [getUVST](Atlas.md)
- [updateFrame](Atlas.md)
- [CREATE_FROM_GRIDS](Atlas.md)
- [CREATE_FROM_TEXTURE](Atlas.md)

## Constructors

### constructor

• **new Atlas**(`_scene`, `options`)

构建一个图集。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `_scene` | [`Scene`](Scene.md) | - |
| `options` | [`IAtlasOptions`](../interfaces/IAtlasOptions.md) | 初始化参数。 |

## Properties

### isAtlas

• **isAtlas**: `boolean` = `true`

## Accessors

### frames

• `get` **frames**(): `Object`

获取帧集合。

#### Returns

`Object`


### meta

• `get` **meta**(): `Object`

获取元信息。

#### Returns

`Object`

| Name | Type |
| --- | --- |
| `size` | { `h`: `number` ; `w`: `number` } |
| `size.h` | `number` |
| `size.w` | `number` |


### texture

• `get` **texture**(): `default`

获取整体的纹理。

#### Returns

`default`

## Methods

### getFrame

▸ **getFrame**(`frameName`): `Object`

获取某一帧的数据。

#### Parameters

| Name | Type |
| --- | --- |
| `frameName` | `string` |

#### Returns

`Object`

| Name | Type |
| --- | --- |
| `h` | `number` |
| `w` | `number` |
| `x` | `number` |
| `y` | `number` |


### getUVMatrix

▸ **getUVMatrix**(`frameName`): [`Matrix3`](Matrix3.md)

获取某一帧的uv变换矩阵。

#### Parameters

| Name | Type |
| --- | --- |
| `frameName` | `string` |

#### Returns

[`Matrix3`](Matrix3.md)


### getUVST

▸ **getUVST**(`frameName`): [`Vector4`](Vector4.md)

获取某一帧的uvST。
[sx, sy, tx, ty]。

#### Parameters

| Name | Type |
| --- | --- |
| `frameName` | `string` |

#### Returns

[`Vector4`](Vector4.md)


### updateFrame

▸ **updateFrame**(`frameName`, `onUpdate`): `void`

更新某一frame，通过`onUpdate`方法参数中的`texture`和`region`来更新上此帧所占据区域内的图像。

#### Parameters

| Name | Type |
| --- | --- |
| `frameName` | `string` |
| `onUpdate` | (`texture`: `default`, `region`: { `h`: `number` ; `w`: `number` ; `x`: `number` ; `y`: `number` }, `frameName`: `string`) => `void` |

#### Returns

`void`


### CREATE_FROM_GRIDS

▸ `Static` **CREATE_FROM_GRIDS**(`scene`, `options`, `onUpdate?`): [`Atlas`](Atlas.md)

根据宽高和行数、列数来创建一个空的图集。
这个图集将被行列分成若干个格子帧，开发者可以根据实际状况去使用`updateFrame`更新这些格子。
自动生成的帧的名字为`${row}${col}`，比如第一行第一列为`'11'`。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `scene` | [`Scene`](Scene.md) | - |
| `options` | `Object` | - |
| `options.cols` | `number` | - |
| `options.height` | `number` | - |
| `options.rows` | `number` | - |
| `options.space?` | `number` | - |
| `options.width` | `number` | - |
| `onUpdate?` | (`texture`: `default`, `region`: { `col`: `number` ; `h`: `number` ; `row`: `number` ; `w`: `number` ; `x`: `number` ; `y`: `number` }, `frameName`: `string`) => `void` | 初始化时的回调，可以用于一开始绘制图像 |

#### Returns

[`Atlas`](Atlas.md)


### CREATE_FROM_TEXTURE

▸ `Static` **CREATE_FROM_TEXTURE**(`scene`, `texture`, `options`): [`Atlas`](Atlas.md)

根据纹理和配置，来通过纹理创建一个不可修改的图集。通常用于精灵动画。
这个图集将被行列分成若干个格子帧，每一帧的名字为`0`、`1`、`2`......

#### Parameters

| Name | Type |
| --- | --- |
| `scene` | [`Scene`](Scene.md) |
| `texture` | `default` |
| `options` | [`IAtlasCreationOptions`](../interfaces/IAtlasCreationOptions.md) |

#### Returns

[`Atlas`](Atlas.md)
