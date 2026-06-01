# Interface: IRenderStates

> 官方文档：[Interface: IRenderStates](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IRenderStates.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IRenderStates
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IRenderStates

支持定制的渲染状态。

大部分状态会定制的开发者应该看名字就懂，就不详细说明了。

## Table of contents

### Properties

- [blendDst](IRenderStates.md)
- [blendDstAlpha](IRenderStates.md)
- [blendDstRGB](IRenderStates.md)
- [blendFunc](IRenderStates.md)
- [blendOn](IRenderStates.md)
- [blendSrc](IRenderStates.md)
- [blendSrcAlpha](IRenderStates.md)
- [blendSrcRGB](IRenderStates.md)
- [colorWrite](IRenderStates.md)
- [cullFace](IRenderStates.md)
- [cullOn](IRenderStates.md)
- [depthTestComp](IRenderStates.md)
- [depthTestOn](IRenderStates.md)
- [depthWrite](IRenderStates.md)
- [primitiveType](IRenderStates.md)
- [renderQueue](IRenderStates.md)
- [stencilComp](IRenderStates.md)
- [stencilFail](IRenderStates.md)
- [stencilPass](IRenderStates.md)
- [stencilReadMask](IRenderStates.md)
- [stencilRef](IRenderStates.md)
- [stencilTestOn](IRenderStates.md)
- [stencilWriteMask](IRenderStates.md)
- [stencilZFail](IRenderStates.md)

## Properties

### blendDst

• `Optional` **blendDst**: [`EBlendFactor`](../enums/EBlendFactor.md)

不要使用，使用`blendDstRGB`。


### blendDstAlpha

• `Optional` **blendDstAlpha**: [`EBlendFactor`](../enums/EBlendFactor.md)


### blendDstRGB

• `Optional` **blendDstRGB**: [`EBlendFactor`](../enums/EBlendFactor.md)


### blendFunc

• `Optional` **blendFunc**: [`EBlendEquation`](../enums/EBlendEquation.md)


### blendOn

• `Optional` **blendOn**: `boolean`


### blendSrc

• `Optional` **blendSrc**: [`EBlendFactor`](../enums/EBlendFactor.md)

不要使用，使用`blendSrcRGB`。


### blendSrcAlpha

• `Optional` **blendSrcAlpha**: [`EBlendFactor`](../enums/EBlendFactor.md)


### blendSrcRGB

• `Optional` **blendSrcRGB**: [`EBlendFactor`](../enums/EBlendFactor.md)


### colorWrite

• `Optional` **colorWrite**: `number`

在基础库版本`v2.31.1`以上支持。


### cullFace

• `Optional` **cullFace**: [`ECullMode`](../enums/ECullMode.md)


### cullOn

• `Optional` **cullOn**: `boolean`


### depthTestComp

• `Optional` **depthTestComp**: [`ECompareFunc`](../enums/ECompareFunc.md)


### depthTestOn

• `Optional` **depthTestOn**: `boolean`


### depthWrite

• `Optional` **depthWrite**: `boolean`


### primitiveType

• `Optional` **primitiveType**: [`EPrimitiveType`](../enums/EPrimitiveType.md)


### renderQueue

• `Optional` **renderQueue**: `number`

渲染队列，大于等于`2500`为透明物体，否则为非透明物体。


### stencilComp

• `Optional` **stencilComp**: [`ECompareFunc`](../enums/ECompareFunc.md)


### stencilFail

• `Optional` **stencilFail**: [`EStencilOp`](../enums/EStencilOp.md)


### stencilPass

• `Optional` **stencilPass**: [`EStencilOp`](../enums/EStencilOp.md)


### stencilReadMask

• `Optional` **stencilReadMask**: `number`


### stencilRef

• `Optional` **stencilRef**: `number`


### stencilTestOn

• `Optional` **stencilTestOn**: `boolean`


### stencilWriteMask

• `Optional` **stencilWriteMask**: `number`


### stencilZFail

• `Optional` **stencilZFail**: [`EStencilOp`](../enums/EStencilOp.md)
