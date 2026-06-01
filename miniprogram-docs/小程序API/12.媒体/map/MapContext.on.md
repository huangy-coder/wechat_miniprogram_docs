# MapContext.on(string event, function callback)

> 官方文档：[MapContext.on(string event, function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.on.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 地图 / MapContext / MapContext.on
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.13.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [map](https://developers.weixin.qq.com/miniprogram/dev/component/map.html)

## 功能描述

监听地图事件。

### visualLayerEvent

可视化图层 visualLayer 统一回调出口，['2.26.0'](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 起支持。

#### 返回参数

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| layerId | String | 图层 id |
| eventType | String | 事件类型 |
| eventInfo | String | 事件信息 |

### markerClusterCreate

缩放或拖动导致新的聚合簇产生时触发，仅返回新创建的聚合簇信息。

#### 返回参数

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| clusters | `Array&lt;ClusterInfo&gt;` | 聚合簇数据 |

### markerClusterClick

聚合簇的点击事件。

#### 返回参数

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| cluster | ClusterInfo | 聚合簇 |

#### ClusterInfo 结构

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| clusterId | Number | 聚合簇的 id |
| center | LatLng | 聚合簇的坐标 |
| markerIds | `Array&lt;Number&gt;` | 该聚合簇内的点标记数据数组 |

### markerCollisionStatusChange

marker 参与碰撞后隐藏时的回调，['3.4.3'](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 起支持。

#### 返回参数

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| show | `Array&lt;Number&gt;` | 碰撞时隐藏后又显示的 `markerIds` |
| hide | `Array&lt;Number&gt;` | 碰撞时被隐藏的 `markerIds` |

## 参数

### string event

事件名

**event 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| markerClusterCreate |   |   |
| markerClusterClick |   |   |
| visualLayerEvent |   |   |
| markerCollisionStatusChange |   |   |

### function callback

事件的回调函数

## 示例代码

```js
  MapContext.on('visualLayerEvent', (res) => {})
  MapContext.on('markerClusterCreate', (res) => {})
  MapContext.on('markerClusterClick', (res) => {})
  MapContext.on('markerCollisionStatusChange', (res) => {})
```
