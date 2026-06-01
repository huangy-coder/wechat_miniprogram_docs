# Class: Element

> 官方文档：[Class: Element](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Element.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Element
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Element

元素，系统核心之一。

本质上就是对应于`xml`中标签，所有的标签的实现都是继承自`Element`的，其一般不包含逻辑，仅仅是通过`defaultComponents`和`dataMapping`定义组件的集合与映射。
自定义元素最后使用{#@link registerElement}。

## Hierarchy

- **`Element`** ↳ [`Scene`](Scene.md) ↳ [`XRNode`](XRNode.md) ↳ [`XRShadow`](XRShadow.md) ↳ [`XRCamera`](XRCamera.md) ↳ [`XRMesh`](XRMesh.md) ↳ [`XRLight`](XRLight.md) ↳ [`XRMaterial`](XRMaterial.md) ↳ [`XRAssetRenderTexture`](XRAssetRenderTexture.md) ↳ [`XRAssetLoad`](XRAssetLoad.md) ↳ [`XRAssets`](XRAssets.md) ↳ [`XREnv`](XREnv.md) ↳ [`XRARTracker`](XRARTracker.md) ↳ [`XRText`](XRText.md) ↳ [`XRParticle`](XRParticle.md) ↳ [`XRAssetPostProcess`](XRAssetPostProcess.md)

## Table of contents

### Constructors

- [constructor](Element.md)

### Properties

- [dataMapping](Element.md)
- [defaultComponents](Element.md)
- [TYPE](Element.md)

### Accessors

- [event](Element.md)
- [id](Element.md)
- [inXML](Element.md)
- [name](Element.md)
- [parent](Element.md)
- [scene](Element.md)

### Methods

- [addChild](Element.md)
- [addComponent](Element.md)
- [dfs](Element.md)
- [getChildAtIndex](Element.md)
- [getChildByClass](Element.md)
- [getChildByFilter](Element.md)
- [getChildByName](Element.md)
- [getChildrenByFilter](Element.md)
- [getChildrenByName](Element.md)
- [getComponent](Element.md)
- [release](Element.md)
- [removeChild](Element.md)
- [removeComponent](Element.md)
- [setAttribute](Element.md)
- [setId](Element.md)

## Constructors

### constructor

• **new Element**(`_type`, `triggerEvent`)

#### Parameters

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

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


### defaultComponents

• `Readonly` **defaultComponents**: [`IEntityComponents`](../interfaces/IEntityComponents.md)

`Element`的默认组件集合，详见[IEntityComponents](../interfaces/IEntityComponents.md)。


### TYPE

▪ `Static` **TYPE**: `string` = `'element'`

## Accessors

### event

• `get` **event**(): [`EventManager`](EventManager.md)

事件管理器。

#### Returns

[`EventManager`](EventManager.md)


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


### scene

• `get` **scene**(): [`Scene`](Scene.md)

场景实例。

#### Returns

[`Scene`](Scene.md)

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


### getChildrenByFilter

▸ **getChildrenByFilter**(`filter`): [`Element`](Element.md)[]

通过`filter`获取子元素列表。

#### Parameters

| Name | Type |
| --- | --- |
| `filter` | (`child`: [`Element`](Element.md)) => `boolean` |

#### Returns

[`Element`](Element.md)[]


### getChildrenByName

▸ **getChildrenByName**(`name`): [`Element`](Element.md)[]

通过元素的名字`name`获取子元素们。

#### Parameters

| Name | Type |
| --- | --- |
| `name` | `string` |

#### Returns

[`Element`](Element.md)[]


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


### release

▸ **release**(): `void`

仅限自己创建的节点使用，否则后果自负。

#### Returns

`void`


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


### removeComponent

▸ **removeComponent**(`clz`): `void`

手动移除一个`Component`，注意保证其不在`xml`上。

#### Parameters

| Name | Type |
| --- | --- |
| `clz` | () => [`Component`](Component.md)<`any`> |

#### Returns

`void`


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


### setId

▸ **setId**(`id`): `void`

仅限自己创建的节点使用，否则后果自负。

#### Parameters

| Name | Type |
| --- | --- |
| `id` | `string` |

#### Returns

`void`
