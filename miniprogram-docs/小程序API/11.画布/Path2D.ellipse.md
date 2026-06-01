# Path2D.ellipse(number x, number y, number radiusX, number radiusY, number rotation, number startAngle, number endAngle, boolean counterclockwise)

> 官方文档：[Path2D.ellipse(number x, number y, number radiusX, number radiusY, number rotation, number startAngle, number endAngle, boolean counterclockwise)](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Path2D.ellipse.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / Path2D / Path2D.ellipse
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

> 相关文档: [画布指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

## 功能描述

添加椭圆弧路径

## 参数

### number x

椭圆圆心横坐标。

### number y

椭圆圆心纵坐标。

### number radiusX

椭圆长轴半径，必须为非负数。

### number radiusY

椭圆短轴半径，必须为非负数。

### number rotation

椭圆旋转角度。

### number startAngle

圆弧开始角度。

### number endAngle

圆弧结束角度。

### boolean counterclockwise

是否逆时针绘制。如果传 true, 则会从 endAngle 开始绘制到 startAngle。
