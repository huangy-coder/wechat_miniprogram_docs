# DraggableSheetContext

> 官方文档：[DraggableSheetContext](https://developers.weixin.qq.com/miniprogram/dev/api/skyline/DraggableSheetContext.html)
> 所属分类：[Skyline](Skyline目录.md)
> 导航路径：Skyline / DraggableSheetContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.2.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [draggable-sheet](https://developers.weixin.qq.com/miniprogram/dev/component/draggable-sheet.html)

DraggableSheet 实例，可通过 [wx.createSelectorQuery](../19.WXML/wx.createSelectorQuery.md) 的 [NodesRef.node](../19.WXML/NodesRef.node.md) 方法获取。

## 方法

### DraggableSheetContext.scrollTo(Object object)

滚动到指定位置。`size` 取值 `[0, 1]`，`size = 1` 时表示撑满 `draggable-sheet` 组件。`size` 和 `pixels` 同时传入时，仅 size 生效。
