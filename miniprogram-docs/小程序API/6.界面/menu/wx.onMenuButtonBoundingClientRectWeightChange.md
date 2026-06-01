# wx.onMenuButtonBoundingClientRectWeightChange(function listener)

> 官方文档：[wx.onMenuButtonBoundingClientRectWeightChange(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.onMenuButtonBoundingClientRectWeightChange.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 菜单 / wx.onMenuButtonBoundingClientRectWeightChange
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.4.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

监听菜单按钮（右上角胶囊按钮）的布局位置信息变化事件

## 参数

### function listener

菜单按钮（右上角胶囊按钮）的布局位置信息变化事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| width | number | 宽度，单位：px |
| height | number | 高度，单位：px |
| top | number | 上边界坐标，单位：px |
| right | number | 右边界坐标，单位：px |
| bottom | number | 下边界坐标，单位：px |
| left | number | 左边界坐标，单位：px |

## 示例代码

```js
const callback = res => console.log('menuButtonBoundingClientRectWeightChange', res)

wx.onMenuButtonBoundingClientRectWeightChange(callback)
// 取消监听
wx.offMenuButtonBoundingClientRectWeightChange(callback)
```
