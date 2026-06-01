# MapContext.includePoints(Object object)

> 官方文档：[MapContext.includePoints(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.includePoints.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 地图 / MapContext / MapContext.includePoints
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.2.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [map](https://developers.weixin.qq.com/miniprogram/dev/component/map.html)

## 功能描述

缩放视野展示所有经纬度

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| points | Array.<Object> |   | 是 | 要显示在可视区域内的坐标点列表 |
| padding | Array.<number> |   | 否 | 坐标点形成的矩形边缘到地图边缘的距离，单位像素。格式为[上,右,下,左]。开发者工具暂不支持padding参数。 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

补充表：
| 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| longitude | number |   | 是 | 经度 |
| latitude | number |   | 是 | 纬度 |
