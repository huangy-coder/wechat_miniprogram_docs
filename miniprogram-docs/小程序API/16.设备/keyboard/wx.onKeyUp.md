# wx.onKeyUp(function listener)

> 官方文档：[wx.onKeyUp(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.onKeyUp.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 键盘 / wx.onKeyUp
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.6.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

监听小程序全局键盘按键弹起事件。仅适用于 PC 平台

## 参数

### function listener

小程序全局键盘按键弹起事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| key | string | 按键名称，同 Web 规范 KeyEvent key 属性 |
| code | string | 按键 code，同 Web 规范 KeyEvent code 属性 |
| altKey | string | 当前是否同时按下了 altKey，同 Web 规范 KeyEvent altKey 属性 |
| shiftKey | string | 当前是否同时按下了 shiftKey，同 Web 规范 KeyEvent shiftKey 属性 |
| timeStamp | number | 事件触发时的时间戳 |

## 注意事项

1. 必须在小程序窗口处于前台且曾有过用户操作（例如点击等）后才会触发。
2. 如某个快捷键组合已经被系统定义（例如 alt+F4、全屏时按 esc 退出等），则会优先响应系统操作，是否发送此事件取决于系统规则。
3. 如当前焦点正聚焦在 `input`、`textarea`、`editor` 组件，则不会发送此事件。
4. 如当前焦点在 webview 组件中，则不会发送此事件。
