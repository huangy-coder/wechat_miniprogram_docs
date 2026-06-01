# Interface: IKeyframeAnimationData

> 官方文档：[Interface: IKeyframeAnimationData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IKeyframeAnimationData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IKeyframeAnimationData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IKeyframeAnimationData

`Keyframe`动画数据的动画部分。

## Table of contents

### Properties

- [animation](IKeyframeAnimationData.md)
- [keyframe](IKeyframeAnimationData.md)

## Properties

### animation

• **animation**: `Object`

动画部分。

#### Index signature

▪ [name: `string`]: [`IKeyframeAnimationInfo`](IKeyframeAnimationInfo.md)


### keyframe

• **keyframe**: `Object`

关键帧定义部分，可以参考[basic-animation](https://mmbizwxaminiprogram-1258344707.cos.ap-guangzhou.myqcloud.com/xr-frame/doc/basic-animation.json)。

`name`为关键帧名字。
`key`为`0~100`的进度。
`prop`为属性序列，其规则为`[componentName].[prop1].[prop2].[prop3]...`，但是有一些特殊的缩写：
`position`、`scale`、`rotation`是`transform`组件下对应的属性，`material.u_xxx`则是设置材质的uniform。
`prop`的值，可以是数字或者数字数组。

#### Index signature

▪ [name: `string`]: { `[key: string]`: { `[prop: string]`: `number` | `number`[]; }; }
