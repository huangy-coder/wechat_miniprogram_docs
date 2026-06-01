# IntersectionObserver wx.createIntersectionObserver(Object component, Object options)

> 官方文档：[IntersectionObserver wx.createIntersectionObserver(Object component, Object options)](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/wx.createIntersectionObserver.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / wx.createIntersectionObserver
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.9.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [获取界面上的节点信息](https://developers.weixin.qq.com/miniprogram/dev/framework/view/selector.html)

## 功能描述

创建并返回一个 IntersectionObserver 对象实例。在自定义组件或包含自定义组件的页面中，应使用 `this.createIntersectionObserver([options])` 来代替。

## 参数

### Object component

自定义组件实例

### Object options

选项

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| thresholds | Array.<number> | [0] | 否 | 一个数值数组，包含所有阈值。 |   |
| initialRatio | number | 0 | 否 | 初始的相交比例，如果调用时检测到的相交比例与这个值不相等且达到阈值，则会触发一次监听器的回调函数。 |   |
| observeAll | boolean | false | 否 | 是否同时观测多个目标节点（而非一个），如果设为 true ，observe 的 targetSelector 将选中多个节点（注意：同时选中过多节点将影响渲染性能） | [2.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| nativeMode | boolean | false | 否 | 是否使用原生观察器模式。 | [3.5.7](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 返回值

### IntersectionObserver

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/ETQafJmu7BTm)

## 原生模式

小程序的观察器默认使用非原生模式。非原生模式下，部分表现会与原生模式有差异，具体差异为：

1. 非原生观察器调用 `relativeTo` 设置的参照区域可以为任意节点；而原生模式只能相对祖先节点。
2. 非原生观察器调用 `relativeTo` 或 `relativeToViewport` 可以设置多个参照区域，参照区域之间会取交集；而原生模式只允许设置一个参照区域。
3. 非原生观察器计算区域相交时，直接计算节点区域和参照区域的交集；而原生模式会对节点的祖先节点进行遍历，计算节点的祖先节点到参照节点的路径中，所有节点区域的交集。
4. 原生观察器性能比非原生模式更高。

原生观察器相关信息可参考 [IntersectionObserver 文档](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)。

## Tips

1. 若 `relativeTo` 设置的参照区域不是祖先节点，则无法开启原生模式。
2. 若调用多次 `relativeTo` 和 `relativeToViewport`，观察器性能会下降。
