# Interface: IARTrackerData

> 官方文档：[Interface: IARTrackerData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IARTrackerData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IARTrackerData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IARTrackerData

[ARTracker](../classes/ARTracker.md)组件数据接口。

## Table of contents

### Properties

- [autoSync](IARTrackerData.md)
- [image](IARTrackerData.md)
- [mode](IARTrackerData.md)
- [src](IARTrackerData.md)

## Properties

### autoSync

• `Optional` **autoSync**: `number`[]

在`Face`模式下，给定一个**特征点索引**列表，详见官网对应文档。
系统会自动同步位置和缩放到`ARTracker`下对应的顺序的子节点。
`-1`代表不同步位置，只同步缩放。


### image

• `Optional` **image**: [`IImage`](IImage.md)

要追踪的图片资源，优先使用。
`xml`中数据为`image`类型。


### mode

• **mode**: [`TTrackMode`](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#TTrackMode)

跟踪模式，必须在[ARSystem](../classes/ARSystem.md)已开启的模式列表中。
`xml`中数据为`string`类型。


### src

• `Optional` **src**: `string`

要追踪的图片地址，如果`image`没有定义，则使用这个。
`xml`中数据为`string`类型。
