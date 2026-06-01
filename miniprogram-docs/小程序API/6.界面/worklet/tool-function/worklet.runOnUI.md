# function worklet.runOnUI(function fn)

> 官方文档：[function worklet.runOnUI(function fn)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/tool-function/worklet.runOnUI.html)
> 所属分类：[界面](../../界面目录.md)
> 导航路径：界面 / worklet 动画 / 工具函数 / worklet.runOnUI
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

> 相关文档: [worklet 动画](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/worklet.html)

## 功能描述

在 UI 线程执行 worklet 函数。

## 参数

### function fn

worklet 类型函数。

## 返回值

### function

`runOnUI` 为高阶函数，返回一个函数，执行时运行在 `UI` 线程。

## 示例代码

```javascript
function someWorklet(greeting) {
  'worklet';
  console.log('hello', greeting); // print: [ui] hello Skyline
}

wx.worklet.runOnUI(someWorklet)('Skyline')
```
