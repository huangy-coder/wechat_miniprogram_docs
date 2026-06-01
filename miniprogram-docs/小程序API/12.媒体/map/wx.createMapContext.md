# MapContext wx.createMapContext(string mapId, Object this)

> 官方文档：[MapContext wx.createMapContext(string mapId, Object this)](https://developers.weixin.qq.com/miniprogram/dev/api/media/map/wx.createMapContext.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 地图 / wx.createMapContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [map](https://developers.weixin.qq.com/miniprogram/dev/component/map.html)

## 功能描述

创建 [map](https://developers.weixin.qq.com/miniprogram/dev/component/map.html) 上下文 [MapContext](MapContext.md) 对象。建议使用 [wx.createSelectorQuery](../../19.WXML/wx.createSelectorQuery.md) 获取 context 对象。

## 参数

### string mapId

[map](https://developers.weixin.qq.com/miniprogram/dev/component/map.html) 组件的 id

### Object this

在自定义组件下，当前组件实例的this，以操作组件内 [map](https://developers.weixin.qq.com/miniprogram/dev/component/map.html) 组件

## 返回值

### MapContext
