# Interface: ICameraData

> 官方文档：[Interface: ICameraData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ICameraData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / ICameraData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / ICameraData

[Camera](../classes/Camera.md)组件数据接口。

## Table of contents

### Properties

- [allowFeatures](ICameraData.md)
- [background](ICameraData.md)
- [clearColor](ICameraData.md)
- [clearDepth](ICameraData.md)
- [clearStencil](ICameraData.md)
- [cullMask](ICameraData.md)
- [depth](ICameraData.md)
- [far](ICameraData.md)
- [fov](ICameraData.md)
- [isARCamera](ICameraData.md)
- [isClearColor](ICameraData.md)
- [isClearDepth](ICameraData.md)
- [isClearStencil](ICameraData.md)
- [isPerspective](ICameraData.md)
- [near](ICameraData.md)
- [orthSize](ICameraData.md)
- [postProcess](ICameraData.md)
- [renderTarget](ICameraData.md)
- [target](ICameraData.md)

## Properties

### allowFeatures

• **allowFeatures**: `string`[]

允许的渲染标记，配合[RenderSystem](../classes/RenderSystem.md)的`changeFeatures`一起使用。
`xml`中的数据类型为`array`，默认为空。


### background

• **background**: [`TCameraBackground`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TCameraBackground)

背景清屏模式。
`xml`中的数据类型为`string`，默认为`default`。


### clearColor

• **clearColor**: `number`[]

清屏颜色。
`xml`中的数据类型为`color`，默认为`0 0 0 1`。


### clearDepth

• **clearDepth**: `number`

清屏深度。
`xml`中的数据类型为`number`，默认为`1`。


### clearStencil

• **clearStencil**: `number`

清屏模板值。
`xml`中的数据类型为`number`，默认为`0`。


### cullMask

• **cullMask**: `number`

掩码，一般和[Transform.layer](../classes/Transform.md)一起使用，决定那些节点要被渲染。
`xml`中的数据类型为`number`。


### depth

• **depth**: `number`

深度，决定在多相机时的渲染顺序。
`xml`中的数据类型为`number`。


### far

• **far**: `number`

远平面。
`xml`中的数据类型为`number`，默认为`100`。


### fov

• **fov**: `number`

视场角。
`xml`中的数据类型为`number`，默认为`60`。


### isARCamera

• **isARCamera**: `boolean`

是否为AR相机，配合[ARSystem](../classes/ARSystem.md)使用。
`xml`中的数据类型为`boolean`，默认为`false`。
**非常需要注意当设置为`true`时不能同时设置`target`数据！**


### isClearColor

• **isClearColor**: `boolean`

清屏是否要清颜色。
`xml`中的数据类型为`boolean`，默认为`true`。


### isClearDepth

• **isClearDepth**: `boolean`

清屏是否要清深度。
`xml`中的数据类型为`boolean`，默认为`true`。


### isClearStencil

• **isClearStencil**: `boolean`

清屏是否要清模板值。
`xml`中的数据类型为`boolean`，默认为`true`。


### isPerspective

• **isPerspective**: `boolean`

是否为透视相机。
`xml`中的数据类型为`boolean`，默认为`true`。


### near

• **near**: `number`

近平面。
`xml`中的数据类型为`number`，默认为`0.1`。


### orthSize

• **orthSize**: `number`

非透视模式，即正交模式时，可视范围大小。
`xml`中的数据类型为`number`，默认为`4`。


### postProcess

• **postProcess**: `string`[]

后处理，一个后处理资源id的数组。
`xml`中的数据类型为`array`，默认为空。


### renderTarget

• `Optional` **renderTarget**: [`RenderTexture`](../classes/RenderTexture.md)

相机的渲染目标，如果不设置则渲染到屏幕。
`xml`中的数据类型为`render-texture`资源。


### target

• `Optional` **target**: [`Transform`](../classes/Transform.md)

相机对准的目标节点，如果不设置则为自由模式。
`xml`中的数据类型为节点对应的`nodeId`。
