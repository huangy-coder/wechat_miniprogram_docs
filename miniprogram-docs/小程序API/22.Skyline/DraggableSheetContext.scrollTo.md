# DraggableSheetContext.scrollTo(Object object)

> 官方文档：[DraggableSheetContext.scrollTo(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/skyline/DraggableSheetContext.scrollTo.html)
> 所属分类：[Skyline](Skyline目录.md)
> 导航路径：Skyline / DraggableSheetContext / DraggableSheetContext.scrollTo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.2.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持

> 相关文档: [draggable-sheet](https://developers.weixin.qq.com/miniprogram/dev/component/draggable-sheet.html)

## 功能描述

滚动到指定位置。`size` 取值 `[0, 1]`，`size = 1` 时表示撑满 `draggable-sheet` 组件。`size` 和 `pixels` 同时传入时，仅 size 生效。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| size | number |   | 否 | 相对目标位置 |
| pixels | number |   | 否 | 绝对目标位置 |
| animated | boolean | true | 否 | 是否启用滚动动画 |
| duration | number | 300 | 否 | 滚动动画时长（ms) |
| easingFunction | string | ease | 否 | 缓动函数 |

## 示例代码

```javascript
Page({
  onReady() {
    this.createSelectorQuery()
      .select(".sheet")
      .node()
      .exec(res => {
        const sheetContext = res[0].node
        sheetContext.scrollTo({
          size: 0.7,
          animated: true,
          duration: 300,
          easingFunction: 'ease'
        })
  },
})
```
