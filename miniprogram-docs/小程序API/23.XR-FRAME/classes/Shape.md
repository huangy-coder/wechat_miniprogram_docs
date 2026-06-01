# Class: Shape<T>

> 官方文档：[Class: Shape<T>](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Shape.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Shape
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Shape

轮廓组件的基类。
为元素添加*该组件的子类*可以创建一个可用于交互的轮廓。

> 💡 只要创建了轮廓，在点击该物体时就可以触发事件：
> - touch-shape: 点击物体事件，回调参数为[IShapeTouchEvent](../interfaces/IShapeTouchEvent.md)；
> - drag-shape: 拖拽物体事件，回调参数为[IShapeDragEvent](../interfaces/IShapeDragEvent.md)；
> - untouch-shape: 松开物体事件，回调参数为[IShapeTouchEvent](../interfaces/IShapeTouchEvent.md)；
> 绑定事件的方法可参考以下代码：
> `<xr-node sphere-shape bind:touch-shape="handleTouchShape"></xr-node>`

> 💡 如果想要将轮廓可视化来确认轮廓大小，可以在同一个元素下添加[ShapeGizmos](ShapeGizmos.md)组件，或在标签上添加`shape-gizmo`属性（对MeshShape不起作用）。

**`abstract`**

## Type parameters

| Name | Type |
| --- | --- |
| `T` | extends [`IShapeData`](../interfaces/IShapeData.md) = `any` |

## Hierarchy

- [`Component`](Component.md)<[`IShapeData`](../interfaces/IShapeData.md)> ↳ **`Shape`** ↳↳ [`SphereShape`](SphereShape.md) ↳↳ [`MeshShape`](MeshShape.md) ↳↳ [`CapsuleShape`](CapsuleShape.md) ↳↳ [`CubeShape`](CubeShape.md)

## Table of contents

### Constructors

- [constructor](Shape.md)

### Events

- [onAdd](Shape.md)
- [onRelease](Shape.md)
- [onRemove](Shape.md)
- [onTick](Shape.md)
- [onUpdate](Shape.md)

### Properties

- [implType](Shape.md)
- [priority](Shape.md)
- [schema](Shape.md)
- [shadowRoot](Shape.md)
- [EVENTS](Shape.md)

### Accessors

- [el](Shape.md)
- [scene](Shape.md)
- [type](Shape.md)
- [version](Shape.md)

### Methods

- [getBasicImpl](Shape.md)
- [getData](Shape.md)
- [getGLTFRootShape](Shape.md)
- [getShadowShapes](Shape.md)
- [initDelegates](Shape.md)
- [resetListeners](Shape.md)
- [setAsShadow](Shape.md)
- [setData](Shape.md)
- [setDataOne](Shape.md)

## Constructors

### constructor

• **new Shape**<`T`>()

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends [`IShapeData`](../interfaces/IShapeData.md) = `any` |

#### Inherited from

[Component](Component.md).[constructor](Component.md)

## Events

### onAdd

▸ **onAdd**(`parent`, `data`): `void`

所挂载的`element`被挂载到场景时触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `parent` | [`Element`](Element.md) |
| `data` | `T` |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onAdd](Component.md)


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

[Component](Component.md).[onRelease](Component.md)


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

[Component](Component.md).[onRemove](Component.md)


### onTick

▸ **onTick**(`dateTime`, `data`): `void`

渲染每帧触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `dateTime` | `number` |
| `data` | `T` |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onTick](Component.md)


### onUpdate

▸ **onUpdate**(`data`, `preData`): `void`

数据更新时触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `T` |
| `preData` | `T` |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onUpdate](Component.md)

## Properties

### implType

• **implType**: `ShapeImplType`


### priority

• `Readonly` **priority**: `number` = `400`

自定义组件的更新优先级。

#### Overrides

[Component](Component.md).[priority](Component.md)


### schema

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md) = `{}`

自定义组件的`schema`。

#### Inherited from

[Component](Component.md).[schema](Component.md)


### shadowRoot

• `Optional` **shadowRoot**: `GLTFAbstractShape`<`T`>


### EVENTS

▪ `Static` **EVENTS**: `string`[]

#### Overrides

[Component](Component.md).[EVENTS](Component.md)

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

▸ **getBasicImpl**(): `BasicShape`<`T`>

#### Returns

`BasicShape`<`T`>


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

[Component](Component.md).[getData](Component.md)


### getGLTFRootShape

▸ **getGLTFRootShape**(): [`Shape`](Shape.md)<`T`>

#### Returns

[`Shape`](Shape.md)<`T`>


### getShadowShapes

▸ **getShadowShapes**(): [`Shape`](Shape.md)<`T`>[]

#### Returns

[`Shape`](Shape.md)<`T`>[]


### initDelegates

▸ **initDelegates**(`el`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `el` | [`Element`](Element.md) |

#### Returns

`void`


### resetListeners

▸ **resetListeners**(): `void`

#### Returns

`void`


### setAsShadow

▸ **setAsShadow**(`root`, `transform`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `root` | `GLTFAbstractShape`<`T`> |
| `transform` | `TQS` |

#### Returns

`void`


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

[Component](Component.md).[setData](Component.md)


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

[Component](Component.md).[setDataOne](Component.md)
