# Object wx.getWindowInfo()

> 官方文档：[Object wx.getWindowInfo()](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getWindowInfo.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 系统 / wx.getWindowInfo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.21.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

获取窗口信息

## 返回值

### Object

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| pixelRatio | number | 设备像素比 |
| screenWidth | number | 屏幕宽度，单位px |
| screenHeight | number | 屏幕高度，单位px |
| windowWidth | number | 可使用窗口宽度，单位px |
| windowHeight | number | 可使用窗口高度，单位px |
| statusBarHeight | number | 状态栏的高度，单位px |
| safeArea | Object | 在竖屏正方向下的安全区域。部分机型没有安全区域概念，也不会返回 safeArea 字段，开发者需自行兼容。 |
| screenTop | number | 窗口上边缘的y值 |

补充表：
| 结构属性 | 类型 | 说明 |
| --- | --- | --- |
| left | number | 安全区域左上角横坐标 |
| right | number | 安全区域右下角横坐标 |
| top | number | 安全区域左上角纵坐标 |
| bottom | number | 安全区域右下角纵坐标 |
| width | number | 安全区域的宽度，单位逻辑像素 |
| height | number | 安全区域的高度，单位逻辑像素 |

## 示例代码

```js
const windowInfo = wx.getWindowInfo()

console.log(windowInfo.pixelRatio)
console.log(windowInfo.screenWidth)
console.log(windowInfo.screenHeight)
console.log(windowInfo.windowWidth)
console.log(windowInfo.windowHeight)
console.log(windowInfo.statusBarHeight)
console.log(windowInfo.safeArea)
console.log(windowInfo.screenTop)
```
