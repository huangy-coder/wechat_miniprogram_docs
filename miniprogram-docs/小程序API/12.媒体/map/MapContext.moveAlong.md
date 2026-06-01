# MapContext.moveAlong(Object object)

> 官方文档：[MapContext.moveAlong(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.moveAlong.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 地图 / MapContext / MapContext.moveAlong
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.13.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：支持

> 相关文档: [map](https://developers.weixin.qq.com/miniprogram/dev/component/map.html)

## 功能描述

沿指定路径移动 `marker`，用于轨迹回放等场景。动画完成时触发回调事件，若动画进行中，对同一 `marker` 再次调用 `moveAlong` 方法，前一次的动画将被打断。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| markerId | number |   | 是 | 指定 marker |
| path | Array |   | 是 | 移动路径的坐标串，坐标点格式 `{longitude, latitude}` |
| autoRotate | boolean | true | 否 | 根据路径方向自动改变 marker 的旋转角度 |
| duration | number |   | 是 | 平滑移动的时间 |
| precision | Object |   | 是 | 平滑移动触发 map 组件 interpolatepoint 事件的插值精度，单位为 m。默认不触发。 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |
