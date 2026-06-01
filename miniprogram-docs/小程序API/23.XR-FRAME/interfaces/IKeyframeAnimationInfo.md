# Interface: IKeyframeAnimationInfo

> 官方文档：[Interface: IKeyframeAnimationInfo](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IKeyframeAnimationInfo.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IKeyframeAnimationInfo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IKeyframeAnimationInfo

`Keyframe`动画数据的动画部分。

## Table of contents

### Properties

- [delay](IKeyframeAnimationInfo.md)
- [direction](IKeyframeAnimationInfo.md)
- [duration](IKeyframeAnimationInfo.md)
- [ease](IKeyframeAnimationInfo.md)
- [easeParams](IKeyframeAnimationInfo.md)
- [keyframe](IKeyframeAnimationInfo.md)
- [loop](IKeyframeAnimationInfo.md)

## Properties

### delay

• `Optional` **delay**: `number`

播放延迟。


### direction

• `Optional` **direction**: [`TDirection`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TDirection)

播放方向。


### duration

• **duration**: `number`

动画长度(s)。


### ease

• **ease**: `string`

动画插值方式，详见[noneParamsEaseFuncs](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#noneParamsEaseFuncs)和[useParamsEaseFuncs](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#useParamsEaseFuncs)。


### easeParams

• `Optional` **easeParams**: `number`[]

如果是可以接受参数的插值方式，指定参数。


### keyframe

• **keyframe**: `string`

指定动画使用的Keyframe。


### loop

• `Optional` **loop**: `number`

循环次数，`0`为不循环，`-1`为永远循环。
