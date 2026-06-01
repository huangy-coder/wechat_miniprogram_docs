# Class: MeshShape

> 官方文档：[Class: MeshShape](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/MeshShape.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / MeshShape
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / MeshShape

利用当前元素下的[Mesh组件](Mesh.md)或[GLTF组件](GLTF.md)，创建一个完全贴合的轮廓。如果当前元素下不存在Mesh组件或GLTF组件，则不生效。
可通过在标签上添加`mesh-shape`属性来为元素添加该组件。

> ⚠️ 如果Mesh或GLTF内部结构非常复杂，创建和维持该组件可能会占用较多的资源。如果发现该组件会导致小程序性能下降，可以考虑改用其他轮廓类型，并开启[autoFit](../interfaces/IShapeData.md)属性。

> ⚠️ MeshShape使用的Mesh的顶点数量不能超过65535个。如果超过了，推荐使用CubeShape+autoFit来代替。

**`see`** [IMeshShapeData](../interfaces/IMeshShapeData.md)

## Hierarchy

- [`Shape`](Shape.md)<[`IMeshShapeData`](../interfaces/IMeshShapeData.md)> ↳ **`MeshShape`**

## Table of contents

### Constructors

- [constructor](MeshShape.md)

### Events

- [onAdd](MeshShape.md)
- [onRelease](MeshShape.md)
- [onRemove](MeshShape.md)
- [onTick](MeshShape.md)
- [onUpdate](MeshShape.md)

### Properties

- [implType](MeshShape.md)
- [priority](MeshShape.md)
- [schema](MeshShape.md)
- [shadowRoot](MeshShape.md)
- [EVENTS](MeshShape.md)

### Accessors

- [el](MeshShape.md)
- [scene](MeshShape.md)
- [type](MeshShape.md)
- [version](MeshShape.md)

### Methods

- [getBasicImpl](MeshShape.md)
- [getData](MeshShape.md)
- [getGLTFRootShape](MeshShape.md)
- [getShadowShapes](MeshShape.md)
- [initDelegates](MeshShape.md)
- [resetListeners](MeshShape.md)
- [setAsShadow](MeshShape.md)
- [setData](MeshShape.md)
- [setDataOne](MeshShape.md)

## Constructors

### constructor

• **new MeshShape**()

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
| `data` | [`IMeshShapeData`](../interfaces/IMeshShapeData.md) |

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
| `data` | [`IMeshShapeData`](../interfaces/IMeshShapeData.md) |

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
| `data` | [`IMeshShapeData`](../interfaces/IMeshShapeData.md) |
| `preData` | [`IMeshShapeData`](../interfaces/IMeshShapeData.md) |

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

• `Optional` **shadowRoot**: `GLTFAbstractShape`<[`IMeshShapeData`](../interfaces/IMeshShapeData.md)>

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

▸ **getBasicImpl**(): `BasicShape`<[`IMeshShapeData`](../interfaces/IMeshShapeData.md)>

#### Returns

`BasicShape`<[`IMeshShapeData`](../interfaces/IMeshShapeData.md)>

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

▸ **getGLTFRootShape**(): [`Shape`](Shape.md)<[`IMeshShapeData`](../interfaces/IMeshShapeData.md)>

#### Returns

[`Shape`](Shape.md)<[`IMeshShapeData`](../interfaces/IMeshShapeData.md)>

#### Inherited from

[Shape](Shape.md).[getGLTFRootShape](Shape.md)


### getShadowShapes

▸ **getShadowShapes**(): [`Shape`](Shape.md)<[`IMeshShapeData`](../interfaces/IMeshShapeData.md)>[]

#### Returns

[`Shape`](Shape.md)<[`IMeshShapeData`](../interfaces/IMeshShapeData.md)>[]

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
| `root` | `GLTFAbstractShape`<[`IMeshShapeData`](../interfaces/IMeshShapeData.md)> |
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
