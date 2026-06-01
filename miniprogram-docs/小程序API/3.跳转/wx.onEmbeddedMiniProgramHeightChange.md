# wx.onEmbeddedMiniProgramHeightChange(function listener)

> 官方文档：[wx.onEmbeddedMiniProgramHeightChange(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.onEmbeddedMiniProgramHeightChange.html)
> 所属分类：[跳转](跳转目录.md)
> 导航路径：跳转 / wx.onEmbeddedMiniProgramHeightChange
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.33.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

监听半屏小程序可视高度变化事件

## 参数

### function listener

半屏小程序可视高度变化事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| height | number | 可视高度 |
| initialHeight | number | 半屏小程序初始高度 |

## 示例代码

```js
const func = function (res) {
  console.log(res.height)
  console.log(res.initialHeight)
}
wx.onEmbeddedMiniProgramHeightChange(func)
// 取消监听
wx.offEmbeddedMiniProgramHeightChange(func)
```
