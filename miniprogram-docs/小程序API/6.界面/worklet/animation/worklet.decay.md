# AnimationObject worklet.decay(Object options, function callback)

> 官方文档：[AnimationObject worklet.decay(Object options, function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/animation/worklet.decay.html)
> 所属分类：[界面](../../界面目录.md)
> 导航路径：界面 / worklet 动画 / 动画 / worklet.decay
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

> 相关文档: [worklet 动画](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/worklet.html)

## 功能描述

基于滚动衰减的动画。

## 参数

### Object options

动画配置

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| velocity | number | 0 | 否 | 初速度 |
| deceleration | number | 0.998 | 否 | 衰减速率 |
| clamp | Array.<number> | [] | 否 | 边界值，长度为 2 的数组 |

### function callback

动画完成回调。动画被取消时，返回 fasle，正常完成时返回 true。

## 返回值

### AnimationObject

返回 AnimationObject 类型值，可直接赋值给 SharedValue。

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/zaI8sgmw7lGW)

```html
<pan-gesture-handler onGestureEvent="handlepan">
  <view class="circle"></view>
</pan-gesture-handler>
```

```js
const { shared, decay } = wx.worklet
Page({
  onLoad() {
    this._offset = shared(0);
    this.applyAnimatedStyle('.circle', () => {
      'worklet';
      return {
        transform: `translateX(${this._offset.value}px)`
      };
    });
  },
  handlepan(evt) {
    'worklet';
    if (evt.state === GestureState.ACTIVE) {
      this._offset.value += evt.deltaX;
    } else if (evt.state === GestureState.END) {
      this._offset.value = decay({
         velocity: evt.velocityX,
         clamp: [-200, 200],
        },
        () => {
           'worklet'
           console.info('@@@ decay finish')
        }
      );
    }
  }
});
```
