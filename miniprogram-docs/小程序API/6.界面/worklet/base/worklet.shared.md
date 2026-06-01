# SharedValue worklet.shared(any initialValue)

> 官方文档：[SharedValue worklet.shared(any initialValue)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/base/worklet.shared.html)
> 所属分类：[界面](../../界面目录.md)
> 导航路径：界面 / worklet 动画 / 基础 / worklet.shared
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

> 相关文档: [worklet 动画](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/worklet.html)

## 功能描述

创建共享变量 `SharedValue`，用于跨线程共享数据和驱动动画。

## 参数

### any initialValue

初始值，可通过 `.value` 属性进行读取和修改。类型可以是 `number | string | bool | null | undefined | Object | Array | Function`。

## 返回值

### SharedValue

返回 SharedValue 类型值，可被 worklet 函数捕获。

## 示例代码

```javascript
const offset = wx.worklet.shared(0)
const someWorkletFn = () => {
 'worklet'
 console.log('offset: ', offset.value)
}
```
