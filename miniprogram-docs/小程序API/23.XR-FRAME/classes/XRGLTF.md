# Class: XRGLTF

> 官方文档：[Class: XRGLTF](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/XRGLTF.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / XRGLTF
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / XRGLTF

标签为`xr-gltf`。
不能在这个标签内放置子标签。

默认组件见[GLTFDefaultComponents](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#GLTFDefaultComponents)，属性映射见[GLTFDataMapping](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#GLTFDataMapping)。

## Hierarchy

- [`XRShadow`](XRShadow.md) ↳ **`XRGLTF`**

## Table of contents

### Constructors

- [constructor](XRGLTF.md)

### Properties

- [dataMapping](XRGLTF.md)
- [defaultComponents](XRGLTF.md)
- [TYPE](XRGLTF.md)

### Accessors

- [event](XRGLTF.md)
- [id](XRGLTF.md)
- [inXML](XRGLTF.md)
- [name](XRGLTF.md)
- [parent](XRGLTF.md)
- [scene](XRGLTF.md)

### Methods

- [addChild](XRGLTF.md)
- [addComponent](XRGLTF.md)
- [dfs](XRGLTF.md)
- [getChildAtIndex](XRGLTF.md)
- [getChildByClass](XRGLTF.md)
- [getChildByFilter](XRGLTF.md)
- [getChildByName](XRGLTF.md)
- [getChildrenByFilter](XRGLTF.md)
- [getChildrenByName](XRGLTF.md)
- [getComponent](XRGLTF.md)
- [release](XRGLTF.md)
- [removeChild](XRGLTF.md)
- [removeComponent](XRGLTF.md)
- [setAttribute](XRGLTF.md)
- [setId](XRGLTF.md)

## Constructors

### constructor

• **new XRGLTF**(`_type`, `triggerEvent`)

#### Parameters

| Name | Type |
| --- | --- |
| `_type` | `string` |
| `triggerEvent` | `TFrameworkEventTrigger` |

#### Inherited from

[XRShadow](XRShadow.md).[constructor](XRShadow.md)

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

#### Overrides

[XRShadow](XRShadow.md).[dataMapping](XRShadow.md)


### defaultComponents

• `Readonly` **defaultComponents**: [`IEntityComponents`](../interfaces/IEntityComponents.md)

`Element`的默认组件集合，详见[IEntityComponents](../interfaces/IEntityComponents.md)。

#### Overrides

[XRShadow](XRShadow.md).[defaultComponents](XRShadow.md)


### TYPE

▪ `Static` **TYPE**: `string` = `'element'`

#### Inherited from

[XRShadow](XRShadow.md).[TYPE](XRShadow.md)

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

#### Inherited from

[XRShadow](XRShadow.md).[addChild](XRShadow.md)


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

[XRShadow](XRShadow.md).[addComponent](XRShadow.md)


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

[XRShadow](XRShadow.md).[dfs](XRShadow.md)


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

[XRShadow](XRShadow.md).[getChildAtIndex](XRShadow.md)


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

[XRShadow](XRShadow.md).[getChildByClass](XRShadow.md)


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

[XRShadow](XRShadow.md).[getChildByFilter](XRShadow.md)


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

[XRShadow](XRShadow.md).[getChildByName](XRShadow.md)


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

[XRShadow](XRShadow.md).[getChildrenByFilter](XRShadow.md)


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

[XRShadow](XRShadow.md).[getChildrenByName](XRShadow.md)


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

[XRShadow](XRShadow.md).[getComponent](XRShadow.md)

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

[XRShadow](XRShadow.md).[getComponent](XRShadow.md)


### release

▸ **release**(): `void`

仅限自己创建的节点使用，否则后果自负。

#### Returns

`void`

#### Inherited from

[XRShadow](XRShadow.md).[release](XRShadow.md)


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

[XRShadow](XRShadow.md).[removeChild](XRShadow.md)


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

[XRShadow](XRShadow.md).[removeComponent](XRShadow.md)


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

[XRShadow](XRShadow.md).[setAttribute](XRShadow.md)


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

[XRShadow](XRShadow.md).[setId](XRShadow.md)
