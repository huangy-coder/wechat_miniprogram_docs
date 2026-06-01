# Interface: IShapeDragEvent

> 官方文档：[Interface: IShapeDragEvent](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IShapeDragEvent.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IShapeDragEvent
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IShapeDragEvent

`drag-shape`事件的回调参数。

## Hierarchy

- [`IShapeTouchEvent`](IShapeTouchEvent.md) ↳ **`IShapeDragEvent`**

## Table of contents

### Properties

- [camera](IShapeDragEvent.md)
- [deltaX](IShapeDragEvent.md)
- [deltaY](IShapeDragEvent.md)
- [dir](IShapeDragEvent.md)
- [force](IShapeDragEvent.md)
- [origin](IShapeDragEvent.md)
- [shape](IShapeDragEvent.md)
- [target](IShapeDragEvent.md)
- [x](IShapeDragEvent.md)
- [y](IShapeDragEvent.md)

## Properties

### camera

• **camera**: [`Camera`](../classes/Camera.md)

渲染*被选中的[轮廓](../classes/Shape.md)*的相机。

#### Inherited from

[IShapeTouchEvent](IShapeTouchEvent.md).[camera](IShapeTouchEvent.md)


### deltaX

• **deltaX**: `number`

点击位置在二维canvas中的x坐标的变化量。


### deltaY

• **deltaY**: `number`

点击位置在二维canvas中的y坐标的变化量。


### dir

• **dir**: [`number`, `number`, `number`]

从[camera](IShapeDragEvent.md)投射出的射线的单位向量。

#### Inherited from

[IShapeTouchEvent](IShapeTouchEvent.md).[dir](IShapeTouchEvent.md)


### force

• **force**: `number`

**`unimplemented`**

#### Inherited from

[IShapeTouchEvent](IShapeTouchEvent.md).[force](IShapeTouchEvent.md)


### origin

• **origin**: [`number`, `number`, `number`]

[camera](IShapeDragEvent.md)在三维场景中的位置。

#### Inherited from

[IShapeTouchEvent](IShapeTouchEvent.md).[origin](IShapeTouchEvent.md)


### shape

• **shape**: [`Shape`](../classes/Shape.md)<`any`>

被选中的[轮廓](../classes/Shape.md)。

#### Inherited from

[IShapeTouchEvent](IShapeTouchEvent.md).[shape](IShapeTouchEvent.md)


### target

• **target**: [`Element`](../classes/Element.md)

*被选中的[轮廓](../classes/Shape.md)*所在的元素。

#### Inherited from

[IShapeTouchEvent](IShapeTouchEvent.md).[target](IShapeTouchEvent.md)


### x

• **x**: `number`

点击位置在二维canvas中的x坐标。

#### Inherited from

[IShapeTouchEvent](IShapeTouchEvent.md).[x](IShapeTouchEvent.md)


### y

• **y**: `number`

点击位置在二维canvas中的y坐标。

#### Inherited from

[IShapeTouchEvent](IShapeTouchEvent.md).[y](IShapeTouchEvent.md)
