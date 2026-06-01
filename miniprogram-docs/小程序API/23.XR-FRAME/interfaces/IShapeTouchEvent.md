# Interface: IShapeTouchEvent

> 官方文档：[Interface: IShapeTouchEvent](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IShapeTouchEvent.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IShapeTouchEvent
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IShapeTouchEvent

`touch-shape`和`untouch-shape`事件的回调参数。

## Hierarchy

- **`IShapeTouchEvent`** ↳ [`IShapeDragEvent`](IShapeDragEvent.md)

## Table of contents

### Properties

- [camera](IShapeTouchEvent.md)
- [dir](IShapeTouchEvent.md)
- [force](IShapeTouchEvent.md)
- [origin](IShapeTouchEvent.md)
- [shape](IShapeTouchEvent.md)
- [target](IShapeTouchEvent.md)
- [x](IShapeTouchEvent.md)
- [y](IShapeTouchEvent.md)

## Properties

### camera

• **camera**: [`Camera`](../classes/Camera.md)

渲染*被选中的[轮廓](../classes/Shape.md)*的相机。


### dir

• **dir**: [`number`, `number`, `number`]

从[camera](IShapeTouchEvent.md)投射出的射线的单位向量。


### force

• **force**: `number`

**`unimplemented`**


### origin

• **origin**: [`number`, `number`, `number`]

[camera](IShapeTouchEvent.md)在三维场景中的位置。


### shape

• **shape**: [`Shape`](../classes/Shape.md)<`any`>

被选中的[轮廓](../classes/Shape.md)。


### target

• **target**: [`Element`](../classes/Element.md)

*被选中的[轮廓](../classes/Shape.md)*所在的元素。


### x

• **x**: `number`

点击位置在二维canvas中的x坐标。


### y

• **y**: `number`

点击位置在二维canvas中的y坐标。
