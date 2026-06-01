# VKPlaneAnchor

> 官方文档：[VKPlaneAnchor](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKPlaneAnchor.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKPlaneAnchor
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.22.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

平面 anchor，只有 v2 版本支持

## 属性

### number id

唯一标识

### number type

类型

**type 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 平面 |   |

### Float32Array transform

包含位置、旋转、放缩信息的矩阵，以列为主序

### Object size

尺寸

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 宽度 |
| height | number | 高度 |

### number alignment

方向

## 示例代码

v1 版本：[水平面AR能力使用参考](https://github.com/wechat-miniprogram/miniprogram-demo/tree/master/miniprogram/packageAPI/pages/ar/plane-ar)
v2 版本：[水平面AR能力v2使用参考](https://github.com/wechat-miniprogram/miniprogram-demo/tree/master/miniprogram/packageAPI/pages/ar/plane-ar-v2)
