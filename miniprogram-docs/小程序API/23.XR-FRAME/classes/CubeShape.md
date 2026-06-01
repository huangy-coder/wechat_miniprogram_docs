# Class: CubeShape

> 官方文档：[Class: CubeShape](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/CubeShape.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / CubeShape
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / CubeShape

为当前元素创建一个可交互的长方体轮廓。
可通过在标签上添加`cube-shape`属性来为元素添加该组件。

**`see`** [ICubeShapeData](../interfaces/ICubeShapeData.md)

## Hierarchy

- [`Shape`](Shape.md)<[`ICubeShapeData`](../interfaces/ICubeShapeData.md)> ↳ **`CubeShape`**

## Table of contents

### Constructors

- [constructor](CubeShape.md)

### Events

- [onAdd](CubeShape.md)
- [onRelease](CubeShape.md)
- [onRemove](CubeShape.md)
- [onTick](CubeShape.md)
- [onUpdate](CubeShape.md)

### Properties

- [implType](CubeShape.md)
- [priority](CubeShape.md)
- [schema](CubeShape.md)
- [shadowRoot](CubeShape.md)
- [EVENTS](CubeShape.md)

### Accessors

- [el](CubeShape.md)
- [scene](CubeShape.md)
- [type](CubeShape.md)
- [version](CubeShape.md)

### Methods

- [getBasicImpl](CubeShape.md)
- [getData](CubeShape.md)
- [getGLTFRootShape](CubeShape.md)
- [getShadowShapes](CubeShape.md)
- [initDelegates](CubeShape.md)
- [resetListeners](CubeShape.md)
- [setAsShadow](CubeShape.md)
- [setData](CubeShape.md)
- [setDataOne](CubeShape.md)

## Constructors

### constructor

• **new CubeShape**()

#### Inherited from

[Shape](Shape.md).[constructor](Shape.md)

## Events

### onAdd

▸ **onAdd**(`parent`, `data`): `void`

所挂载的`element`被挂载到场景时触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `parent` | [`Element`](Element.md) |
| `data` | [`ICubeShapeData`](../interfaces/ICubeShapeData.md) |

#### Returns

`void`

#### Inherited from

[Shape](Shape.md).[onAdd](Shape.md)


### onRelease

▸ **onRelease**(`data`): `void`

从被挂载的`element`上被移除，或是`element`被销毁时，触发的回调。
一般用于释放持有的资源。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | [`IShapeData`](../interfaces/IShapeData.md) |

#### Returns

`void`

#### Inherited from

[Shape](Shape.md).[onRelease](Shape.md)


### onRemove

▸ **onRemove**(`parent`, `data`): `void`

所挂载的`element`从父节点`parent`被移除时，或者自己从`element`上被移除时，触发的回调。
一般用于消除功能的运作。
**如果一个组件的元素直接被销毁了，那这个组件就不会经历onRemove而是直接进入onRelease。**

#### Parameters

| Name | Type |
| --- | --- |
| `parent` | [`Element`](Element.md) |
| `data` | [`IShapeData`](../interfaces/IShapeData.md) |

#### Returns

`void`

#### Inherited from

[Shape](Shape.md).[onRemove](Shape.md)


### onTick

▸ **onTick**(`dateTime`, `data`): `void`

渲染每帧触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `dateTime` | `number` |
| `data` | [`ICubeShapeData`](../interfaces/ICubeShapeData.md) |

#### Returns

`void`

#### Inherited from

[Shape](Shape.md).[onTick](Shape.md)


### onUpdate

▸ **onUpdate**(`data`, `preData`): `void`

数据更新时触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | [`ICubeShapeData`](../interfaces/ICubeShapeData.md) |
| `preData` | [`ICubeShapeData`](../interfaces/ICubeShapeData.md) |

#### Returns

`void`

#### Inherited from

[Shape](Shape.md).[onUpdate](Shape.md)

## Properties

### implType

• **implType**: `ShapeImplType`

#### Inherited from

[Shape](Shape.md).[implType](Shape.md)


### priority

• `Readonly` **priority**: `number` = `400`

自定义组件的更新优先级。

#### Inherited from

[Shape](Shape.md).[priority](Shape.md)


### schema

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md)

自定义组件的`schema`。

#### Overrides

[Shape](Shape.md).[schema](Shape.md)


### shadowRoot

• `Optional` **shadowRoot**: `GLTFAbstractShape`<[`ICubeShapeData`](../interfaces/ICubeShapeData.md)>

#### Inherited from

[Shape](Shape.md).[shadowRoot](Shape.md)


### EVENTS

▪ `Static` **EVENTS**: `string`[]

#### Overrides

[Shape](Shape.md).[EVENTS](Shape.md)

## Accessors

### el

• `get` **el**(): [`Element`](Element.md)

挂载的元素。

#### Returns

[`Element`](Element.md)


### scene

• `get` **scene**(): [`Scene`](Scene.md)

当前场景。

#### Returns

[`Scene`](Scene.md)


### type

• `get` **type**(): [`EShapeType`](../enums/EShapeType.md)

#### Returns

[`EShapeType`](../enums/EShapeType.md)


### version

• `get` **version**(): `number`

当前版本，每次有数据更新都会增加，可以用作和其他组件合作的依据。

#### Returns

`number`

## Methods

### getBasicImpl

▸ **getBasicImpl**(): `BasicShape`<[`ICubeShapeData`](../interfaces/ICubeShapeData.md)>

#### Returns

`BasicShape`<[`ICubeShapeData`](../interfaces/ICubeShapeData.md)>

#### Inherited from

[Shape](Shape.md).[getBasicImpl](Shape.md)


### getData

▸ **getData**<`T`>(`key`): [`IShapeData`](../interfaces/IShapeData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeData`](../interfaces/IShapeData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`IShapeData`](../interfaces/IShapeData.md)[`T`]

#### Inherited from

[Shape](Shape.md).[getData](Shape.md)


### getGLTFRootShape

▸ **getGLTFRootShape**(): [`Shape`](Shape.md)<[`ICubeShapeData`](../interfaces/ICubeShapeData.md)>

#### Returns

[`Shape`](Shape.md)<[`ICubeShapeData`](../interfaces/ICubeShapeData.md)>

#### Inherited from

[Shape](Shape.md).[getGLTFRootShape](Shape.md)


### getShadowShapes

▸ **getShadowShapes**(): [`Shape`](Shape.md)<[`ICubeShapeData`](../interfaces/ICubeShapeData.md)>[]

#### Returns

[`Shape`](Shape.md)<[`ICubeShapeData`](../interfaces/ICubeShapeData.md)>[]

#### Inherited from

[Shape](Shape.md).[getShadowShapes](Shape.md)


### initDelegates

▸ **initDelegates**(`el`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `el` | [`Element`](Element.md) |

#### Returns

`void`

#### Inherited from

[Shape](Shape.md).[initDelegates](Shape.md)


### resetListeners

▸ **resetListeners**(): `void`

#### Returns

`void`

#### Inherited from

[Shape](Shape.md).[resetListeners](Shape.md)


### setAsShadow

▸ **setAsShadow**(`root`, `transform`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `root` | `GLTFAbstractShape`<[`ICubeShapeData`](../interfaces/ICubeShapeData.md)> |
| `transform` | `TQS` |

#### Returns

`void`

#### Inherited from

[Shape](Shape.md).[setAsShadow](Shape.md)


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IShapeData`](../interfaces/IShapeData.md)> |

#### Returns

`void`

#### Inherited from

[Shape](Shape.md).[setData](Shape.md)


### setDataOne

▸ **setDataOne**<`T`>(`key`, `value`): `void`

设置一个数据。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IShapeData`](../interfaces/IShapeData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IShapeData`](../interfaces/IShapeData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Shape](Shape.md).[setDataOne](Shape.md)
