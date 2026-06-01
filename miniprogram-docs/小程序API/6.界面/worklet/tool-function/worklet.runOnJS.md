# function worklet.runOnJS(function fn)

> 官方文档：[function worklet.runOnJS(function fn)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/tool-function/worklet.runOnJS.html)
> 所属分类：[界面](../../界面目录.md)
> 导航路径：界面 / worklet 动画 / 工具函数 / worklet.runOnJS
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

> 相关文档: [worklet 动画](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/worklet.html)

## 功能描述

`worklet` 函数运行在 `UI` 线程时，捕获的外部函数可能为 `worklet` 类型或普通函数，为了更明显的对其区分，要求必须使用 `runOnJS` 调回 `JS` 线程的普通函数。
有这样的要求是因为，调用其它 `worklet` 函数时是同步调用，但在 `UI` 线程执行 `JS` 线程的函数只能是异步，开发者容易混淆，试图同步获取 `JS` 线程的返回值。

## 参数

### function fn

未声明为 worklet 类型的普通函数。

## 返回值

### function

`runOnJS` 为高阶函数，返回一个函数，执行时运行在 `JS` 线程。

## 示例代码

```javascript
 function someFunc(greeting) {
   console.log('hello', greeting);
 }

 function someWorklet() {
   'worklet'
   runOnJS(someFunc)('Skyline')
 }

 wx.worklet.runOnUI(someWorklet)()
```
