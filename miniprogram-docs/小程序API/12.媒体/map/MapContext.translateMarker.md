# MapContext.translateMarker(Object object)

> 官方文档：[MapContext.translateMarker(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.translateMarker.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 地图 / MapContext / MapContext.translateMarker
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

从基础库 [3.11.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 建议使用 [MapContext.moveAlong](MapContext.md) 代替

> 基础库 1.2.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：支持

> 相关文档: [map](https://developers.weixin.qq.com/miniprogram/dev/component/map.html)

## 功能描述

平移marker，带动画。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| markerId | number |   | 是 | 指定 marker |   |
| destination | Object |   | 是 | 指定 marker 移动到的目标点 |   |
| autoRotate | boolean |   | 是 | 移动过程中是否自动旋转 marker |   |
| rotate | number |   | 是 | marker 的旋转角度 |   |
| moveWithRotate | boolean | false | 否 | 平移和旋转同时进行 | [2.13.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| duration | number | 1000 | 否 | 动画持续时长，平移与旋转分别计算 |   |
| animationEnd | function |   | 否 | 动画结束回调函数 |   |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

补充表：
| 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| longitude | number |   | 是 | 经度 |
| latitude | number |   | 是 | 纬度 |
