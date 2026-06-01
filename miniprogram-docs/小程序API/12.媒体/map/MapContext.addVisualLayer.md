# MapContext.addVisualLayer(Object object)

> 官方文档：[MapContext.addVisualLayer(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.addVisualLayer.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 地图 / MapContext / MapContext.addVisualLayer
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [map](https://developers.weixin.qq.com/miniprogram/dev/component/map.html)

## 功能描述

添加可视化图层。需要刷新时，interval 可设置的最小值为 15 s。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| layerId | String |   | 是 | 可视化图层id（[创建图层指引](https://lbs.qq.com/dev/console/layers/layerEdit)) |
| interval | Number | 0 | 否 | 刷新周期，单位秒 |
| zIndex | Number | 1 | 否 | 图层绘制顺序 |
| opacity | Number | 1 | 否 | 图层透明度 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |
