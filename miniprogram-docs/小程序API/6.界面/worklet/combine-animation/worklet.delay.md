# AnimationObject worklet.delay(number delayMS, AnimationObject delayedAnimation)

> 官方文档：[AnimationObject worklet.delay(number delayMS, AnimationObject delayedAnimation)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/combine-animation/worklet.delay.html)
> 所属分类：[界面](../../界面目录.md)
> 导航路径：界面 / worklet 动画 / 组合动画 / worklet.delay
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

> 相关文档: [worklet 动画](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/worklet.html)

## 功能描述

延迟执行动画。

## 参数

### number delayMS

动画开始前等待的时间，单位：毫秒。

### AnimationObject delayedAnimation

动画对象。

## 返回值

### AnimationObject

返回 `AnimationObject` 类型值，可直接赋值给 `SharedValue`。

## 示例代码

```javascript
const { shared, repeat, timing } = wx.worklet
const offset = shared(0)
offset.value = delay(1000, timing(70));
```
