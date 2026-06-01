# Interface: IViewAction

> 官方文档：[Interface: IViewAction](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IViewAction.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IViewAction
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IViewAction

对一个View进行清屏的操作。

## Table of contents

### Properties

- [clearColor](IViewAction.md)
- [clearDepth](IViewAction.md)
- [clearStencil](IViewAction.md)
- [colorAction](IViewAction.md)
- [depthAction](IViewAction.md)
- [stencilAction](IViewAction.md)

## Properties

### clearColor

• `Optional` **clearColor**: [`number`, `number`, `number`, `number`]

用于清屏的颜色值。

**`default`** [0,0,0,0]


### clearDepth

• `Optional` **clearDepth**: `number`

用于清屏的深度值。

**`default`** 1


### clearStencil

• `Optional` **clearStencil**: `number`

用于清屏的模板值。

**`default`** 0


### colorAction

• `Optional` **colorAction**: [`ELoadAction`](../enums/ELoadAction.md)

颜色操作。


### depthAction

• `Optional` **depthAction**: [`ELoadAction`](../enums/ELoadAction.md)

深度操作。


### stencilAction

• `Optional` **stencilAction**: [`ELoadAction`](../enums/ELoadAction.md)

模板操作。
