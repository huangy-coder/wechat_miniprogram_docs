# VKMarkerAnchor

> 官方文档：[VKMarkerAnchor](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKMarkerAnchor.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKMarkerAnchor
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.24.5 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

marker anchor

## 属性

### number id

唯一标识

### number type

类型

**type 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 1 | marker |   |

### Float32Array transform

包含位置、旋转、放缩信息的矩阵，以列为主序

### number markerId

marker id

### string path

图片路径

## 示例代码

[2D Marker能力使用参考](https://github.com/wechat-miniprogram/miniprogram-demo/tree/master/miniprogram/packageAPI/pages/ar/2dmarker-ar)
