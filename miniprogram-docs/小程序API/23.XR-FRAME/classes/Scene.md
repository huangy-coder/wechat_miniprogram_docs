# Class: Scene

> 官方文档：[Class: Scene](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Scene.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Scene
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Scene

场景，系统核心之一。

`Scene`是元素的一种，对应于`xr-scene`标签。
作为整个`xr-frame`组件的根节点，它提供了整个组件运作的一些基本能力，挂在了各大系统，驱动生命周期循环。

## Hierarchy

- [`Element`](Element.md) ↳ **`Scene`**

## Table of contents

### Constructors

- [constructor](Scene.md)

### Properties

- [dataMapping](Scene.md)
- [defaultComponents](Scene.md)
- [isScene](Scene.md)
- [TYPE](Scene.md)

### Accessors

- [animation](Scene.md)
- [ar](Scene.md)
- [assets](Scene.md)
- [event](Scene.md)
- [frameHeight](Scene.md)
- [frameWidth](Scene.md)
- [gizmo](Scene.md)
- [height](Scene.md)
- [id](Scene.md)
- [inXML](Scene.md)
- [name](Scene.md)
- [parent](Scene.md)
- [physics](Scene.md)
- [ready](Scene.md)
- [render](Scene.md)
- [rootShadow](Scene.md)
- [scene](Scene.md)
- [share](Scene.md)
- [timestamp](Scene.md)
- [video](Scene.md)
- [width](Scene.md)

### Methods

- [addChild](Scene.md)
- [addComponent](Scene.md)
- [createEffect](Scene.md)
- [createElement](Scene.md)
- [createGeometry](Scene.md)
- [createImage](Scene.md)
- [createMaterial](Scene.md)
- [createPostProcess](Scene.md)
- [createRenderTexture](Scene.md)
- [createTexture](Scene.md)
- [createUniformBlock](Scene.md)
- [createUniformBlockDesc](Scene.md)
- [createVertexLayout](Scene.md)
- [createVideoTexture](Scene.md)
- [dfs](Scene.md)
- [getChildAtIndex](Scene.md)
- [getChildByClass](Scene.md)
- [getChildByFilter](Scene.md)
- [getChildByName](Scene.md)
- [getChildrenByFilter](Scene.md)
- [getChildrenByName](Scene.md)
- [getComponent](Scene.md)
- [getElementById](Scene.md)
- [getNodeById](Scene.md)
- [release](Scene.md)
- [removeChild](Scene.md)
- [removeComponent](Scene.md)
- [setAttribute](Scene.md)
- [setId](Scene.md)

## Constructors

### constructor

• **new Scene**(`_type`, `triggerEvent`)

#### Parameters

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

#### Inherited from

[Element](Element.md).[constructor](Element.md)

## Properties

### dataMapping

• `Readonly` **dataMapping**: `Object`

`Element`的数据映射。它是为了给组件的属性提供一个方便的用法，比如：

```ts
{
  position: [transform, position]
}
```

就是将`xml`中写在这个`Element`的`position`直接映射到了`transform`组件的`position`属性上。

**通常来讲，所有的驼峰如`nodeId`都会被映射为小写加中划线`node-id`**。

#### Index signature

▪ [key: `string`]: `string`[]

#### Inherited from

[Element](Element.md).[dataMapping](Element.md)


### defaultComponents

• `Readonly` **defaultComponents**: [`IEntityComponents`](../interfaces/IEntityComponents.md)

`Element`的默认组件集合，详见[IEntityComponents](../interfaces/IEntityComponents.md)。

#### Overrides

[Element](Element.md).[defaultComponents](Element.md)


### isScene

• `Readonly` **isScene**: `boolean` = `true`


### TYPE

▪ `Static` **TYPE**: `string` = `'element'`

#### Inherited from

[Element](Element.md).[TYPE](Element.md)

## Accessors

### animation

• `get` **animation**(): [`AnimationSystem`](AnimationSystem.md)

动画系统。

#### Returns

[`AnimationSystem`](AnimationSystem.md)


### ar

• `get` **ar**(): [`ARSystem`](ARSystem.md)

AR系统。

#### Returns

[`ARSystem`](ARSystem.md)


### assets

• `get` **assets**(): [`AssetsSystem`](AssetsSystem.md)

资源系统。

#### Returns

[`AssetsSystem`](AssetsSystem.md)


### event

• `get` **event**(): [`EventManager`](EventManager.md)

事件管理器。

#### Returns

[`EventManager`](EventManager.md)


### frameHeight

• `get` **frameHeight**(): `number`

显示分辨率高。

#### Returns

`number`


### frameWidth

• `get` **frameWidth**(): `number`

显示分辨率宽。

#### Returns

`number`


### gizmo

• `get` **gizmo**(): [`GizmoSystem`](GizmoSystem.md)

Gizmo系统。

#### Returns

[`GizmoSystem`](GizmoSystem.md)


### height

• `get` **height**(): `number`

渲染分辨率高，一般物理点击事件之类的都是参考这个。

#### Returns

`number`


### id

• `get` **id**(): `string`

写在`xml`上的那个`id`，要求唯一。

#### Returns

`string`


### inXML

• `get` **inXML**(): `boolean`

元素是否在`xml`中，若是`xr-shadow`下的节点，则为`false`。

#### Returns

`boolean`


### name

• `get` **name**(): `string`

名字，写在`xml`上的那个`name`，不唯一。

#### Returns

`string`

• `set` **name**(`value`): `void`

名字，写在`xml`上的那个`name`，不唯一。

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `string` |

#### Returns

`void`


### parent

• `get` **parent**(): [`Element`](Element.md)

父元素。

#### Returns

[`Element`](Element.md)


### physics

• `get` **physics**(): [`PhysicsSystem`](PhysicsSystem.md)

物理系统。

#### Returns

[`PhysicsSystem`](PhysicsSystem.md)


### ready

• `get` **ready**(): `boolean`

场景是否已经就绪。

#### Returns

`boolean`


### render

• `get` **render**(): [`RenderSystem`](RenderSystem.md)

渲染系统。

#### Returns

[`RenderSystem`](RenderSystem.md)


### rootShadow

• `get` **rootShadow**(): [`XRShadow`](XRShadow.md)

一个可以用于快速挂载自己创建的`Element`的`shadow`节点。

#### Returns

[`XRShadow`](XRShadow.md)


### scene

• `get` **scene**(): `this`

自身。

#### Returns

`this`


### share

• `get` **share**(): [`ShareSystem`](ShareSystem.md)

分享系统。

#### Returns

[`ShareSystem`](ShareSystem.md)


### timestamp

• `get` **timestamp**(): `number`

当前时间戳(ms)。

#### Returns

`number`


### video

• `get` **video**(): [`VideoSystem`](VideoSystem.md)

视频系统。

#### Returns

[`VideoSystem`](VideoSystem.md)


### width

• `get` **width**(): `number`

渲染分辨率宽，一般物理点击事件之类的都是参考这个。

#### Returns

`number`

## Methods

### addChild

▸ **addChild**(`child`): `void`

手动添加一个子节点，**注意需要保证当前节点是`xr-shadow`或其子节点**。

#### Parameters

| Name | Type |
| --- | --- |
| `child` | [`Element`](Element.md) |

#### Returns

`void`

#### Inherited from

[Element](Element.md).[addChild](Element.md)


### addComponent

▸ **addComponent**<`T`>(`clz`, `options?`): `T`

手动添加一个`Component`。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](Component.md)<`any`, `T`> |

#### Parameters

| Name | Type |
| --- | --- |
| `clz` | () => `T` |
| `options?` | `T`[`"__DATA_TYPE"`] |

#### Returns

`T`

#### Inherited from

[Element](Element.md).[addComponent](Element.md)


### createEffect

▸ **createEffect**(`description`): [`Effect`](Effect.md)

手动创建一个`Effect`资源。

#### Parameters

| Name | Type |
| --- | --- |
| `description` | [`IEffectAsset`](../interfaces/IEffectAsset.md) |

#### Returns

[`Effect`](Effect.md)


### createElement

▸ **createElement**<`T`>(`clz`, `attributes?`): `T`

创建一个`Element`，但注意**其只能作为`xr-shadow`的子孙节点**，否则可能会出错！

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](Element.md)<`T`> |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `clz` | (...`args`: `any`) => `T` | - |
| `attributes?` | `Object` | 初始化的属性，同于`xml`中对应的标签属性。 |

#### Returns

`T`


### createGeometry

▸ **createGeometry**(`vertexLayout`, `vBuffer`, `iBuffer`, `indexType?`): [`Geometry`](Geometry.md)

手动创建一个`Geometry`资源。

#### Parameters

| Name | Type |
| --- | --- |
| `vertexLayout` | `default` |
| `vBuffer` | `ArrayBufferView` |
| `iBuffer` | `ArrayBufferView` |
| `indexType?` | [`EIndexType`](../enums/EIndexType.md) |

#### Returns

[`Geometry`](Geometry.md)


### createImage

▸ **createImage**(`autoRelease?`): [`IImage`](../interfaces/IImage.md)

手动创建一个`Image`资源。

#### Parameters

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `autoRelease` | `boolean` | `true` | 此图片在第一次时候后是否释放原始数据，默认释放。 |

#### Returns

[`IImage`](../interfaces/IImage.md)


### createMaterial

▸ **createMaterial**(`effect`, `defaultUniforms?`): [`Material`](Material.md)

手动创建一个`Material`资源。

#### Parameters

| Name | Type |
| --- | --- |
| `effect` | [`Effect`](Effect.md) |
| `defaultUniforms?` | `Object` |

#### Returns

[`Material`](Material.md)


### createPostProcess

▸ **createPostProcess**(`options`): [`PostProcess`](PostProcess.md)

手动创建一个`PostProcess`资源。

#### Parameters

| Name | Type |
| --- | --- |
| `options` | [`IPostProcessOptions`](../interfaces/IPostProcessOptions.md) |

#### Returns

[`PostProcess`](PostProcess.md)


### createRenderTexture

▸ **createRenderTexture**(`options?`): [`RenderTexture`](RenderTexture.md)

手动创建一个`RenderTexture`资源。

#### Parameters

| Name | Type |
| --- | --- |
| `options?` | [`IRenderTextureOptions`](../interfaces/IRenderTextureOptions.md) |

#### Returns

[`RenderTexture`](RenderTexture.md)


### createTexture

▸ **createTexture**(`options`): `default`

手动创建一个`Texture`资源。

#### Parameters

| Name | Type |
| --- | --- |
| `options` | [`ITextureOptions`](../interfaces/ITextureOptions.md) |

#### Returns

`default`


### createUniformBlock

▸ **createUniformBlock**(`descriptor`): `default`

手动创建一个`UniformBlock`资源。

#### Parameters

| Name | Type |
| --- | --- |
| `descriptor` | `default` |

#### Returns

`default`


### createUniformBlockDesc

▸ **createUniformBlockDesc**(`options`): `default`

手动创建一个`UniformBlockDescriptor`资源。

#### Parameters

| Name | Type |
| --- | --- |
| `options` | [`IUniformDescriptorOptions`](../interfaces/IUniformDescriptorOptions.md) |

#### Returns

`default`


### createVertexLayout

▸ **createVertexLayout**(`options`): `default`

手动创建一个`VertexLayout`资源。

#### Parameters

| Name | Type |
| --- | --- |
| `options` | [`IVertexLayoutOptions`](../interfaces/IVertexLayoutOptions.md) |

#### Returns

`default`


### createVideoTexture

▸ **createVideoTexture**(`options?`): `Promise`<[`VideoTexture`](VideoTexture.md)>

手动创建一个`VideoTexture`资源。

#### Parameters

| Name | Type |
| --- | --- |
| `options?` | [`IVideoTextureOptions`](../interfaces/IVideoTextureOptions.md) |

#### Returns

`Promise`<[`VideoTexture`](VideoTexture.md)>


### dfs

▸ **dfs**<`T`>(`callback`, `defaultParams?`, `excludeRoot?`, `stop?`): `void`

递归遍历元素的所有子孙节点。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends `unknown` |

#### Parameters

| Name | Type |
| --- | --- |
| `callback` | (`element`: [`Element`](Element.md), `params?`: `T`) => `T` |
| `defaultParams?` | `T` |
| `excludeRoot?` | `boolean` |
| `stop` | (`element`: [`Element`](Element.md), `params?`: `T`) => `boolean` |

#### Returns

`void`

#### Inherited from

[Element](Element.md).[dfs](Element.md)


### getChildAtIndex

▸ **getChildAtIndex**<`T`>(`index`): `T`

获取第`index`个子元素。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](Element.md)<`T`> = [`Element`](Element.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `index` | `number` |

#### Returns

`T`

#### Inherited from

[Element](Element.md).[getChildAtIndex](Element.md)


### getChildByClass

▸ **getChildByClass**<`T`>(`clz`): `T`

通过元素的类获取子元素。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](Element.md)<`T`> = [`Element`](Element.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `clz` | (...`args`: `any`[]) => `T` |

#### Returns

`T`

#### Inherited from

[Element](Element.md).[getChildByClass](Element.md)


### getChildByFilter

▸ **getChildByFilter**<`T`>(`filter`): `T`

通过`filter`获取子元素。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](Element.md)<`T`> = [`Element`](Element.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](Element.md)) => `boolean` |

#### Returns

`T`

#### Inherited from

[Element](Element.md).[getChildByFilter](Element.md)


### getChildByName

▸ **getChildByName**<`T`>(`name`): `T`

通过元素的名字`name`获取子元素。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends [`Element`](Element.md)<`T`> = [`Element`](Element.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `name` | `string` |

#### Returns

`T`

#### Inherited from

[Element](Element.md).[getChildByName](Element.md)


### getChildrenByFilter

▸ **getChildrenByFilter**(`filter`): [`Element`](Element.md)[]

通过`filter`获取子元素列表。

#### Parameters

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](Element.md)) => `boolean` |

#### Returns

[`Element`](Element.md)[]

#### Inherited from

[Element](Element.md).[getChildrenByFilter](Element.md)


### getChildrenByName

▸ **getChildrenByName**(`name`): [`Element`](Element.md)[]

通过元素的名字`name`获取子元素们。

#### Parameters

| Name | Type |
| --- | --- |
| `name` | `string` |

#### Returns

[`Element`](Element.md)[]

#### Inherited from

[Element](Element.md).[getChildrenByName](Element.md)


### getComponent

▸ **getComponent**<`T`>(`clzName`): `T`

获取一个`Component`，可以使用类或者名字获取。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](Component.md)<`any`, `T`> |

#### Parameters

| Name | Type |
| --- | --- |
| `clzName` | `string` |

#### Returns

`T`

#### Inherited from

[Element](Element.md).[getComponent](Element.md)

▸ **getComponent**<`T`>(`clz`): `T`

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends [`Component`](Component.md)<`any`, `T`> |

#### Parameters

| Name | Type |
| --- | --- |
| `clz` | () => `T` |

#### Returns

`T`

#### Inherited from

[Element](Element.md).[getComponent](Element.md)


### getElementById

▸ **getElementById**(`id`): [`Element`](Element.md)

通过在`wxml`的元素上设置的`id`索引一个元素，`id`是唯一的。

#### Parameters

| Name | Type |
| --- | --- |
| `id` | `string` |

#### Returns

[`Element`](Element.md)


### getNodeById

▸ **getNodeById**(`nodeId`): [`Transform`](Transform.md)

通过在`wxml`的元素上设置的`node-id`索引一个`Transform`组件，`node-id`是唯一的。

#### Parameters

| Name | Type |
| --- | --- |
| `nodeId` | `string` |

#### Returns

[`Transform`](Transform.md)


### release

▸ **release**(): `void`

仅限自己创建的节点使用，否则后果自负。

#### Returns

`void`

#### Inherited from

[Element](Element.md).[release](Element.md)


### removeChild

▸ **removeChild**(`child`): `void`

手动移除一个子节点，**注意需要保证当前节点是`xr-shadow`或其子节点**。
**只调用removeChild没有办法走进子节点的onRelease里**，需要手动调用子节点的release才行。

#### Parameters

| Name | Type |
| --- | --- |
| `child` | [`Element`](Element.md) |

#### Returns

`void`

#### Inherited from

[Element](Element.md).[removeChild](Element.md)


### removeComponent

▸ **removeComponent**(`clz`): `void`

手动移除一个`Component`，注意保证其不在`xml`上。

#### Parameters

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](Component.md)<`any`> |

#### Returns

`void`

#### Inherited from

[Element](Element.md).[removeComponent](Element.md)


### setAttribute

▸ **setAttribute**(`name`, `value`): `void`

设置一个属性，对应于`xml`标签中的那些属性，值为字符串。
**一般建议使用`component`的`setData`方法**！！！

#### Parameters

| Name | Type |
| --- | --- |
| `name` | `string` |
| `value` | `string` |

#### Returns

`void`

#### Inherited from

[Element](Element.md).[setAttribute](Element.md)


### setId

▸ **setId**(`id`): `void`

仅限自己创建的节点使用，否则后果自负。

#### Parameters

| Name | Type |
| --- | --- |
| `id` | `string` |

#### Returns

`void`

#### Inherited from

[Element](Element.md).[setId](Element.md)
