# Interface: IAnimatorData

> 官方文档：[Interface: IAnimatorData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IAnimatorData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IAnimatorData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IAnimatorData

[Animator](../classes/Animator.md)组件数据接口。

## Table of contents

### Properties

- [autoPlay](IAnimatorData.md)
- [clipMap](IAnimatorData.md)
- [keyframe](IAnimatorData.md)

## Properties

### autoPlay

• `Optional` **autoPlay**: [`IAnimatorAutoPlay`](IAnimatorAutoPlay.md)

默认自动播放的参数，详见[IAnimatorAutoPlay](IAnimatorAutoPlay.md)。
`xml`中为`dict`数据。


### clipMap

• `Optional` **clipMap**: `Object`

默认的片段名字映射，由于一个动画可以有多个片段，所以能通过映射由`Animator`中播放的名字 -> 动画资源中片段的名字。
`xml`中为`dict`数据。

#### Index signature

▪ [key: `string`]: `string`


### keyframe

• **keyframe**: [`Animation`](../classes/Animation.md)<`any`, `any`>

默认的`Keyframe`动画资源。
`xml`中为资源id。
