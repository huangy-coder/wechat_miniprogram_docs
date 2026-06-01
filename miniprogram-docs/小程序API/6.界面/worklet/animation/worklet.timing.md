# AnimationObject worklet.timing(number toValue, Object options, function callback)

> 官方文档：[AnimationObject worklet.timing(number toValue, Object options, function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/animation/worklet.timing.html)
> 所属分类：[界面](../../界面目录.md)
> 导航路径：界面 / worklet 动画 / 动画 / worklet.timing
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

> 相关文档: [worklet 动画](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/worklet.html)

## 功能描述

基于时间的动画。

## 参数

### number toValue

目标值

### Object options

动画配置

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 300 | 否 | 动画时长 |
| easing | function | Easing.inOut(Easing.quad) | 否 | 动画曲线，参考 [Easing](worklet.Easing.md) 模块。 |

### function callback

动画完成回调。动画被取消时，返回 fasle，正常完成时返回 true。

## 返回值

### AnimationObject

返回 `AnimationObject` 类型值，可直接赋值给 `SharedValue`。

## 示例代码

```javascript
<view id="moved-box"></view>
<view id="btn" bind:tap="tap">点击驱动小球移动</view>
</code>

<code>
const { shared, timing, Easing } = wx.worklet
Page({
  onLoad() {
    const offset = shared(0)
    this.applyAnimatedStyle('#moved-box', () => {
      'worklet';
      return {
        transform: `translateX(${offset.value}px)`
      }
    })
    this._offset = offset
  }
  tap() {
    const random = Math.random()
    this._offset.value = timing(random, {
        duration: 500,
        easing: Easing.bezier(0.25, 0.1, 0.25, 1),
      }),
    };
})
```
