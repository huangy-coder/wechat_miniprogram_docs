# CanvasContext

> 官方文档：[CanvasContext](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / CanvasContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [旧版画布迁移指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas-legacy-migration.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

canvas 组件的绘图上下文。CanvasContext 是旧版的接口， 新版 Canvas 2D 接口与 Web 一致。

## 属性

### string| CanvasGradient fillStyle

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

填充颜色。用法同 [CanvasContext.setFillStyle()](CanvasContext.setFillStyle.md)。

### string| CanvasGradient strokeStyle

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

边框颜色。用法同 [CanvasContext.setStrokeStyle()](CanvasContext.setStrokeStyle.md)。

### number shadowOffsetX

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

阴影相对于形状在水平方向的偏移

### number shadowOffsetY

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

阴影相对于形状在竖直方向的偏移

### number shadowColor

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

阴影的颜色

### number shadowBlur

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

阴影的模糊级别

### number lineWidth

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

线条的宽度。用法同 [CanvasContext.setLineWidth()](CanvasContext.setLineWidth.md)。

### string lineCap

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

线条的端点样式。用法同 [CanvasContext.setLineCap()](CanvasContext.setLineCap.md)。

### string lineJoin

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

线条的交点样式。用法同 [CanvasContext.setLineJoin()](CanvasContext.setLineJoin.md)。

**lineJoin 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| bevel | 斜角 |   |
| round | 圆角 |   |
| miter | 尖角 |   |

### number miterLimit

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

最大斜接长度。用法同 [CanvasContext.setMiterLimit()](CanvasContext.setMiterLimit.md)。

### number lineDashOffset

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

虚线偏移量，初始值为0

### string font

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

当前字体样式的属性。符合 [CSS font 语法](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font) 的 DOMString 字符串，至少需要提供字体大小和字体族名。默认值为 10px sans-serif。

### number globalAlpha

全局画笔透明度。范围 0-1，0 表示完全透明，1 表示完全不透明。

### string globalCompositeOperation

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

在绘制新形状时应用的合成操作的类型。目前安卓版本只适用于 `fill` 填充块的合成，用于 `stroke` 线段的合成效果都是 `source-over`。

目前支持的操作有

- 安卓：xor, source-over, source-atop, destination-out, lighter, overlay, darken, lighten, hard-light
- iOS：xor, source-over, source-atop, destination-over, destination-out, lighter, multiply, overlay, darken, lighten, color-dodge, color-burn, hard-light, soft-light, difference, exclusion, saturation, luminosity

## 方法

### CanvasContext.draw(boolean reserve, function callback)

将之前在绘图上下文中的描述（路径、变形、样式）画到 canvas 中。

### CanvasGradient CanvasContext.createLinearGradient(number x0, number y0, number x1, number y1)

创建一个线性的渐变颜色。返回的`CanvasGradient`对象需要使用 [CanvasGradient.addColorStop()](CanvasGradient.addColorStop.md) 来指定渐变点，至少要两个。

### CanvasGradient CanvasContext.createCircularGradient(number x, number y, number r)

创建一个圆形的渐变颜色。起点在圆心，终点在圆环。返回的`CanvasGradient`对象需要使用 [CanvasGradient.addColorStop()](CanvasGradient.addColorStop.md) 来指定渐变点，至少要两个。

### CanvasContext.createPattern(string image, string repetition)

对指定的图像创建模式的方法，可在指定的方向上重复元图像

### Object CanvasContext.measureText(string text)

测量文本尺寸信息。目前仅返回文本宽度。同步接口。

### CanvasContext.save()

保存绘图上下文。

### CanvasContext.restore()

恢复之前保存的绘图上下文。

### CanvasContext.beginPath()

开始创建一个路径。需要调用 `fill` 或者 `stroke` 才会使用路径进行填充或描边

- 在最开始的时候相当于调用了一次 `beginPath`。
- 同一个路径内的多次 `setFillStyle`、`setStrokeStyle`、`setLineWidth`等设置，以最后一次设置为准。

### CanvasContext.moveTo(number x, number y)

把路径移动到画布中的指定点，不创建线条。用 `stroke` 方法来画线条

### CanvasContext.lineTo(number x, number y)

增加一个新点，然后创建一条从上次指定点到目标点的线。用 `stroke` 方法来画线条

### CanvasContext.quadraticCurveTo(number cpx, number cpy, number x, number y)

创建二次贝塞尔曲线路径。曲线的起始点为路径中前一个点。

### CanvasContext.bezierCurveTo(number cp1x, number cp1y, number cp2x, number cp2y, number x, number y)

创建三次方贝塞尔曲线路径。曲线的起始点为路径中前一个点。

### CanvasContext.arc(number x, number y, number r, number sAngle, number eAngle, boolean counterclockwise)

创建一条弧线。

- 创建一个圆可以指定起始弧度为 0，终止弧度为 2 * Math.PI。
- 用 `stroke` 或者 `fill` 方法来在 `canvas` 中画弧线。

### CanvasContext.rect(number x, number y, number width, number height)

创建一个矩形路径。需要用 [`fill`](CanvasContext.fill.md) 或者 [`stroke`](CanvasContext.stroke.md) 方法将矩形真正的画到 `canvas` 中

### CanvasContext.arcTo(number x1, number y1, number x2, number y2, number radius)

根据控制点和半径绘制圆弧路径。

### CanvasContext.clip()

从原始画布中剪切任意形状和尺寸。一旦剪切了某个区域，则所有之后的绘图都会被限制在被剪切的区域内（不能访问画布上的其他区域）。可以在使用 `clip` 方法前通过使用 `save` 方法对当前画布区域进行保存，并在以后的任意时间通过`restore`方法对其进行恢复。

### CanvasContext.fillRect(number x, number y, number width, number height)

填充一个矩形。用 [`setFillStyle`](CanvasContext.setFillStyle.md) 设置矩形的填充色，如果没设置默认是黑色。

### CanvasContext.strokeRect(number x, number y, number width, number height)

画一个矩形(非填充)。 用 [`setStrokeStyle`](CanvasContext.setStrokeStyle.md) 设置矩形线条的颜色，如果没设置默认是黑色。

### CanvasContext.clearRect(number x, number y, number width, number height)

清除画布上在该矩形区域内的内容

### CanvasContext.fill()

对当前路径中的内容进行填充。默认的填充色为黑色。

### CanvasContext.stroke()

画出当前路径的边框。默认颜色色为黑色。

### CanvasContext.closePath()

关闭一个路径。会连接起点和终点。如果关闭路径后没有调用 `fill` 或者 `stroke` 并开启了新的路径，那之前的路径将不会被渲染。

### CanvasContext.scale(number scaleWidth, number scaleHeight)

在调用后，之后创建的路径其横纵坐标会被缩放。多次调用倍数会相乘。

### CanvasContext.rotate(number rotate)

以原点为中心顺时针旋转当前坐标轴。多次调用旋转的角度会叠加。原点可以用 `translate` 方法修改。

### CanvasContext.translate(number x, number y)

对当前坐标系的原点 (0, 0) 进行变换。默认的坐标系原点为页面左上角。

### CanvasContext.drawImage(string imageResource, number sx, number sy, number sWidth, number sHeight, number dx, number dy, number dWidth, number dHeight)

绘制图像到画布

### CanvasContext.strokeText(string text, number x, number y, number maxWidth)

给定的 (x, y) 位置绘制文本描边的方法

### CanvasContext.transform(number scaleX, number skewX, number skewY, number scaleY, number translateX, number translateY)

使用矩阵多次叠加当前变换的方法

### CanvasContext.setTransform(number scaleX, number skewX, number skewY, number scaleY, number translateX, number translateY)

使用矩阵重新设置（覆盖）当前变换的方法

### CanvasContext.setFillStyle(string|CanvasGradient color)

设置填充色。

### CanvasContext.setStrokeStyle(string|CanvasGradient color)

设置描边颜色。

### CanvasContext.setShadow(number offsetX, number offsetY, number blur, string color)

设定阴影样式。

### CanvasContext.setGlobalAlpha(number alpha)

设置全局画笔透明度。

### CanvasContext.setLineWidth(number lineWidth)

设置线条的宽度

### CanvasContext.setLineJoin(string lineJoin)

设置线条的交点样式

### CanvasContext.setLineCap(string lineCap)

设置线条的端点样式

### CanvasContext.setLineDash(Array.<number> pattern, number offset)

设置虚线样式。

### CanvasContext.setMiterLimit(number miterLimit)

设置最大斜接长度。斜接长度指的是在两条线交汇处内角和外角之间的距离。当 [CanvasContext.setLineJoin()](CanvasContext.setLineJoin.md) 为 miter 时才有效。超过最大倾斜长度的，连接处将以 lineJoin 为 bevel 来显示。

### CanvasContext.fillText(string text, number x, number y, number maxWidth)

在画布上绘制被填充的文本

### CanvasContext.setFontSize(number fontSize)

设置字体的字号

### CanvasContext.setTextAlign(string align)

设置文字的对齐

### CanvasContext.setTextBaseline(string textBaseline)

设置文字的竖直对齐
