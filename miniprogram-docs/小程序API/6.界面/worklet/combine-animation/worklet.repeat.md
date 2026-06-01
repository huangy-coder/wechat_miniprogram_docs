# AnimationObject worklet.repeat(AnimationObject animation, number numberOfReps, boolean reverse, function callback)

> 官方文档：[AnimationObject worklet.repeat(AnimationObject animation, number numberOfReps, boolean reverse, function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/combine-animation/worklet.repeat.html)
> 所属分类：[界面](../../界面目录.md)
> 导航路径：界面 / worklet 动画 / 组合动画 / worklet.repeat
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

> 相关文档: [worklet 动画](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/worklet.html)

## 功能描述

重复执行动画。

## 参数

### AnimationObject animation

动画对象

### number numberOfReps

重复次数。为负值时一直循环，直到被取消动画。

### boolean reverse

反向运行动画，每周期结束动画由尾到头运行。该字段仅对 timing 和 spring 返回的动画对象生效。

### function callback

动画完成回调。动画被取消时，返回 fasle，正常完成时返回 true。

## 返回值

### AnimationObject

返回 `AnimationObject` 类型值，可直接赋值给 `SharedValue`。

## 示例代码

```javascript
const { shared, repeat, timing } = wx.worklet
const offset = shared(0)
offset.value = repeat(timing(70), 2, true);
```
