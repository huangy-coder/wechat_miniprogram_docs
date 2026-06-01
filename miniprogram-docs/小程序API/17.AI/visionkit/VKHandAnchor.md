# VKHandAnchor

> 官方文档：[VKHandAnchor](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKHandAnchor.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKHandAnchor
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.28.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

手势 anchor

## 属性

### number id

唯一标识

### number type

类型

**type 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 7 | 手势 |   |

### number detectId

识别序号

### Object size

相对视窗的尺寸，取值范围为 [0, 1]，0 为左/上边缘，1 为右/下边缘

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 宽度 |
| height | number | 高度 |

### Object origin

相对视窗的位置信息，取值范围为 [0, 1]，0 为左/上边缘，1 为右/下边缘

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | 横坐标 |
| y | number | 纵坐标 |

### Array.<number> confidence

关键点的置信度

### Array.<Object> points

关键点

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| x | number | 横坐标 |
| y | number | 纵坐标 |

### number score

总体置信值

### number gesture

手势分类, 返回整数-1到18, -1表示无效手势

**gesture 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 单手比心 |   |
| 1 | 布（数字5） |   |
| 2 | 剪刀（数字2） |   |
| 3 | 握拳 |   |
| 4 | 数字1 |   |
| 5 | 热爱 |   |
| 6 | 点赞 |   |
| 7 | 数字3 |   |
| 8 | 摇滚 |   |
| 9 | 数字6 |   |
| 10 | 数字8 |   |
| 11 | 双手抱拳（恭喜发财） |   |
| 12 | 数字4 |   |
| 13 | 比ok |   |
| 14 | 不喜欢（踩） |   |
| 15 | 双手比心 |   |
| 16 | 祈祷（双手合十） |   |
| 17 | 双手抱拳 |   |
| 18 | 无手势动作 |   |
| -1 | 无效手势 |   |

## 示例代码

[静态图像hand检测能力使用参考](https://github.com/wechat-miniprogram/miniprogram-demo/tree/master/miniprogram/packageAPI/pages/ar/photo-hand-detect)

[实时摄像头hand检测能力使用参考](https://github.com/wechat-miniprogram/miniprogram-demo/tree/master/miniprogram/packageAPI/pages/ar/hand-detect)
