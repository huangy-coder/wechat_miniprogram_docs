# Class: Material

> 官方文档：[Class: Material](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Material.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Material
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Material

材质资源，一般被代理到[XRMaterial](XRMaterial.md)元素。

## Table of contents

### Constructors

- [constructor](Material.md)

### Accessors

- [alphaCutOff](Material.md)
- [alphaMode](Material.md)
- [renderQueue](Material.md)

### Methods

- [clearRenderState](Material.md)
- [clearRenderStates](Material.md)
- [clone](Material.md)
- [getFloat](Material.md)
- [getMacro](Material.md)
- [getMatrix](Material.md)
- [getRenderState](Material.md)
- [getTexture](Material.md)
- [getVector](Material.md)
- [initByEffect](Material.md)
- [resetTexture](Material.md)
- [setFloat](Material.md)
- [setMacro](Material.md)
- [setMacros](Material.md)
- [setMatrix](Material.md)
- [setRenderState](Material.md)
- [setRenderStates](Material.md)
- [setTexture](Material.md)
- [setTextureAsset](Material.md)
- [setVector](Material.md)

## Constructors

### constructor

• **new Material**(`_scene`)

#### Parameters

| Name | Type |
| --- | --- |
| `_scene` | [`Scene`](Scene.md) |

## Accessors

### alphaCutOff

• `set` **alphaCutOff**(`value`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `number` |

#### Returns

`void`


### alphaMode

• `set` **alphaMode**(`value`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `"OPAQUE"` \| `"BLEND"` \| `"MASK"` |

#### Returns

`void`


### renderQueue

• `get` **renderQueue**(): `number`

透明物体需要大于`2500`！

#### Returns

`number`

• `set` **renderQueue**(`value`): `void`

透明物体需要大于`2500`！

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `number` |

#### Returns

`void`

## Methods

### clearRenderState

▸ **clearRenderState**<`TKey`>(`key`): `boolean`

清除渲染状态。
清除材质的渲染状态，转而从effect中使用默认值。

#### Type parameters

| Name | Type |
| --- | --- |
| `TKey` | extends keyof [`IRenderStates`](../interfaces/IRenderStates.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `TKey` |

#### Returns

`boolean`


### clearRenderStates

▸ **clearRenderStates**(`states`): `boolean`

批量清除渲染状态。
清除材质的渲染状态，转而从effect中使用默认值。

#### Parameters

| Name | Type |
| --- | --- |
| `states` | `Object` |

#### Returns

`boolean`


### clone

▸ **clone**(): [`Material`](Material.md)

拷贝自身，生成一份新的材质数据。

#### Returns

[`Material`](Material.md)


### getFloat

▸ **getFloat**(`key`): `number`

获取一个Float

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |

#### Returns

`number`


### getMacro

▸ **getMacro**(`key`): `boolean`

获取宏。

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |

#### Returns

`boolean`


### getMatrix

▸ **getMatrix**(`key`): [`Matrix3`](Matrix3.md) | [`Matrix4`](Matrix4.md)

获取一个Vector值的拷贝。

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |

#### Returns

[`Matrix3`](Matrix3.md) | [`Matrix4`](Matrix4.md)


### getRenderState

▸ **getRenderState**(`key`): `number` | `boolean`

获取渲染状态。

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |

#### Returns

`number` | `boolean`


### getTexture

▸ **getTexture**(`key`): `default`

获取材质中已设置的贴图。

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |

#### Returns

`default`


### getVector

▸ **getVector**(`key`): [`Vector3`](Vector3.md) | [`Vector2`](Vector2.md) | [`Vector4`](Vector4.md)

获取一个Vector值的拷贝。

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |

#### Returns

[`Vector3`](Vector3.md) | [`Vector2`](Vector2.md) | [`Vector4`](Vector4.md)


### initByEffect

▸ **initByEffect**(`effect`, `defaultUniforms?`): `void`

通过效果初始化材质。

#### Parameters

| Name | Type |
| --- | --- |
| `effect` | [`Effect`](Effect.md) |
| `defaultUniforms?` | `Object` |

#### Returns

`void`


### resetTexture

▸ **resetTexture**(`key`): `default`

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |

#### Returns

`default`


### setFloat

▸ **setFloat**(`key`, `value`): `boolean`

设置一个Float

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |
| `value` | `number` |

#### Returns

`boolean`

是否设置成功


### setMacro

▸ **setMacro**(`key`, `value`): `void`

设置宏。

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |
| `value` | `number` \| `boolean` |

#### Returns

`void`


### setMacros

▸ **setMacros**(`marcos`): `void`

批量设置宏。

#### Parameters

| Name | Type |
| --- | --- |
| `marcos` | `Object` |

#### Returns

`void`


### setMatrix

▸ **setMatrix**(`key`, `value`): `boolean`

设置一个Matrix

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |
| `value` | [`Matrix3`](Matrix3.md) \| [`Matrix4`](Matrix4.md) |

#### Returns

`boolean`

是否设置成功


### setRenderState

▸ **setRenderState**<`TKey`>(`key`, `value`): `boolean`

设置渲染状态。
只有标记了`useMaterialRenderStates`的Pass会受到影响

#### Type parameters

| Name | Type |
| --- | --- |
| `TKey` | extends keyof [`IRenderStates`](../interfaces/IRenderStates.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `TKey` |
| `value` | [`IRenderStates`](../interfaces/IRenderStates.md)[`TKey`] |

#### Returns

`boolean`


### setRenderStates

▸ **setRenderStates**(`states`): `boolean`

批量设置渲染状态。
只有标记了`useMaterialRenderStates`的Pass会受到影响。

#### Parameters

| Name | Type |
| --- | --- |
| `states` | [`IRenderStates`](../interfaces/IRenderStates.md) |

#### Returns

`boolean`


### setTexture

▸ **setTexture**(`key`, `value`): `boolean`

设置一张贴图。

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |
| `value` | `default` |

#### Returns

`boolean`

是否设置成功。


### setTextureAsset

▸ **setTextureAsset**(`key`, `assetId`): `boolean`

设置一张贴图。

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |
| `assetId` | `string` |

#### Returns

`boolean`

是否设置成功。


### setVector

▸ **setVector**(`key`, `value`): `boolean`

设置一个Vector。

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `string` |
| `value` | [`Vector3`](Vector3.md) \| [`Vector2`](Vector2.md) \| [`Vector4`](Vector4.md) |

#### Returns

`boolean`

是否设置成功。
