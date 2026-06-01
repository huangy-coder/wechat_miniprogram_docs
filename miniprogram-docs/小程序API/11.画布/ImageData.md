# ImageData

> 官方文档：[ImageData](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/ImageData.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / ImageData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.9.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [画布指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

ImageData 对象

## 属性

### number width

使用像素描述 ImageData 的实际宽度

### number height

使用像素描述 ImageData 的实际高度

### Uint8ClampedArray data

一维数组，包含以 RGBA 顺序的数据，数据使用 0 至 255（包含）的整数表示
