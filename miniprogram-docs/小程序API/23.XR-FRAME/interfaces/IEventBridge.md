# Interface: IEventBridge

> 官方文档：[Interface: IEventBridge](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IEventBridge.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IEventBridge
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IEventBridge

## Table of contents

### Methods

- [bindEntitiesToBones](IEventBridge.md)
- [bindEntityToBone](IEventBridge.md)
- [entityAddChild](IEventBridge.md)
- [entityAddChildAtIndex](IEventBridge.md)
- [entityClear](IEventBridge.md)
- [entityRemoveFromParent](IEventBridge.md)
- [entitySetActive](IEventBridge.md)
- [entitySetLocalMatrixDirty](IEventBridge.md)
- [refreshWorldTransform](IEventBridge.md)
- [setRootEntity](IEventBridge.md)
- [unbindEntitiesFromBones](IEventBridge.md)
- [unbindEntityFromBone](IEventBridge.md)

## Methods

### bindEntitiesToBones

▸ **bindEntitiesToBones**(`entities`, `boneEntities`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `entities` | { `id`: `number` }[] |
| `boneEntities` | { `id`: `number` }[] |

#### Returns

`void`


### bindEntityToBone

▸ **bindEntityToBone**(`entity`, `boneEntity`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `entity` | `Object` |
| `entity.id` | `number` |
| `boneEntity` | `Object` |
| `boneEntity.id` | `number` |

#### Returns

`void`


### entityAddChild

▸ **entityAddChild**(`entity`, `child`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `entity` | `number` |
| `child` | `number` |

#### Returns

`void`


### entityAddChildAtIndex

▸ **entityAddChildAtIndex**(`entity`, `child`, `index`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `entity` | `number` |
| `child` | `number` |
| `index` | `number` |

#### Returns

`void`


### entityClear

▸ **entityClear**(`entity`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `entity` | `number` |

#### Returns

`void`


### entityRemoveFromParent

▸ **entityRemoveFromParent**(`entity`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `entity` | `number` |

#### Returns

`void`


### entitySetActive

▸ **entitySetActive**(`entity`, `active`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `entity` | `number` |
| `active` | `boolean` |

#### Returns

`void`


### entitySetLocalMatrixDirty

▸ **entitySetLocalMatrixDirty**(`entity`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `entity` | `number` |

#### Returns

`void`


### refreshWorldTransform

▸ **refreshWorldTransform**(): `void`

#### Returns

`void`


### setRootEntity

▸ **setRootEntity**(`entity`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `entity` | `number` |

#### Returns

`void`


### unbindEntitiesFromBones

▸ **unbindEntitiesFromBones**(`entities`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `entities` | { `id`: `number` }[] |

#### Returns

`void`


### unbindEntityFromBone

▸ **unbindEntityFromBone**(`entity`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `entity` | `Object` |
| `entity.id` | `number` |

#### Returns

`void`
