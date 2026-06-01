# Animation

> 官方文档：[Animation](https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 动画 / Animation
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [动画](https://developers.weixin.qq.com/miniprogram/dev/framework/view/animation.html)

动画对象

## 方法

### Object Animation.export()

导出动画队列。**export 方法每次调用后会清掉之前的动画操作。**

### Animation Animation.step(Object object)

表示一组动画完成。可以在一组动画中调用任意多个动画方法，一组动画中的所有动画会同时开始，一组动画完成后才会进行下一组动画。

### Animation Animation.matrix()

同 [transform-function matrix](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/matrix)

### Animation Animation.matrix3d()

同 [transform-function matrix3d](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/matrix3d)

### Animation Animation.rotate(number angle)

从原点顺时针旋转一个角度

### Animation Animation.rotate3d(number x, number y, number z, number angle)

从 固定 轴顺时针旋转一个角度

### Animation Animation.rotateX(number angle)

从 X 轴顺时针旋转一个角度

### Animation Animation.rotateY(number angle)

从 Y 轴顺时针旋转一个角度

### Animation Animation.rotateZ(number angle)

从 Z 轴顺时针旋转一个角度

### Animation Animation.scale(number sx, number sy)

缩放

### Animation Animation.scale3d(number sx, number sy, number sz)

缩放

### Animation Animation.scaleX(number scale)

缩放 X 轴

### Animation Animation.scaleY(number scale)

缩放 Y 轴

### Animation Animation.scaleZ(number scale)

缩放 Z 轴

### Animation Animation.skew(number ax, number ay)

对 X、Y 轴坐标进行倾斜

### Animation Animation.skewX(number angle)

对 X 轴坐标进行倾斜

### Animation Animation.skewY(number angle)

对 Y 轴坐标进行倾斜

### Animation Animation.translate(number tx, number ty)

平移变换

### Animation Animation.translate3d(number tx, number ty, number tz)

对 xyz 坐标进行平移变换

### Animation Animation.translateX(number translation)

对 X 轴平移

### Animation Animation.translateY(number translation)

对 Y 轴平移

### Animation Animation.translateZ(number translation)

对 Z 轴平移

### Animation Animation.opacity(number value)

设置透明度

### Animation Animation.backgroundColor(string value)

设置背景色

### Animation Animation.width(number|string value)

设置宽度

### Animation Animation.height(number|string value)

设置高度

### Animation Animation.left(number|string value)

设置 left 值

### Animation Animation.right(number|string value)

设置 right 值

### Animation Animation.top(number|string value)

设置 top 值

### Animation Animation.bottom(number|string value)

设置 bottom 值

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/Swab8kmW7v2V)

```html
<view animation="{{animationData}}" style="background:red;height:100rpx;width:100rpx"></view>
```

```js
Page({
  data: {
    animationData: {}
  },
  onShow: function(){
    var animation = wx.createAnimation({
      duration: 1000,
      timingFunction: 'ease',
    })

    this.animation = animation

    animation.scale(2,2).rotate(45).step()

    this.setData({
      animationData:animation.export()
    })

    setTimeout(function() {
      animation.translate(30).step()
      this.setData({
        animationData:animation.export()
      })
    }.bind(this), 1000)
  },
  rotateAndScale: function () {
    // 旋转同时放大
    this.animation.rotate(45).scale(2, 2).step()
    this.setData({
      animationData: this.animation.export()
    })
  },
  rotateThenScale: function () {
    // 先旋转后放大
    this.animation.rotate(45).step()
    this.animation.scale(2, 2).step()
    this.setData({
      animationData: this.animation.export()
    })
  },
  rotateAndScaleThenTranslate: function () {
    // 先旋转同时放大，然后平移
    this.animation.rotate(45).scale(2, 2).step()
    this.animation.translate(100, 100).step({ duration: 1000 })
    this.setData({
      animationData: this.animation.export()
    })
  }
})
```
