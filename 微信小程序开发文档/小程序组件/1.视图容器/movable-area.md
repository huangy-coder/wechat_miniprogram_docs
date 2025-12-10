视图容器 /movable-area /

> 基础库 1.2.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Windows 版**：支持
>
> **微信 Mac 版**：支持
>
> **微信 鸿蒙 OS 版**：支持

渲染框架支持情况：WebView

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/movable-area.html#%E5%8A%9F%E8%83%BD%E6%8F%8F%E8%BF%B0) 功能描述

[movable-view](https://developers.weixin.qq.com/miniprogram/dev/component/movable-view.html)的可移动区域。

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/movable-area.html#%E5%B1%9E%E6%80%A7%E8%AF%B4%E6%98%8E) 属性说明

| 属性       | 类型    | 默认值 | 必填 | 说明                                                         | 最低版本                                                     |
| ---------- | ------- | ------ | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| scale-area | Boolean | false  | 否   | 当里面的movable-view设置为支持双指缩放时，设置此值可将缩放手势生效区域修改为整个movable-area | [1.9.90](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/movable-area.html#Bug-Tip) Bug & Tip

1.  `tip`: movable-area 必须设置width和height属性，不设置默认为10px\*\*
2.  `tip`: 当movable-view小于movable-area时，movable-view的移动范围是在movable-area内；
3.  `tip`: 当movable-view大于movable-area时，movable-view的移动范围必须包含movable-area（x轴方向和y轴方向分开考虑）
4.  `tip`: 若当前组件所在的页面或全局开启了 `enablePassiveEvent` 配置项，该内置组件可能会出现非预期表现（详情参考 [enablePassiveEvent 文档](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/app)）

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/movable-area.html#%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81) 示例代码

```xml
<view class="container">

  <view class="page-body">
    <view class="page-section">
      <view class="page-section-title first">movable-view区域小于movable-area</view>
      <movable-area>
        <movable-view x="{{x}}" y="{{y}}" direction="all">text</movable-view>
      </movable-area>
    </view>
    <view class="btn-area">
      <button bindtap="tap" class="page-body-button" type="primary">点击移动到 (30px, 30px)</button>
    </view>

    <view class="page-section">
      <view class="page-section-title">movable-view区域大于movable-area</view>
      <movable-area>
        <movable-view class="max" direction="all">text</movable-view>
      </movable-area>
    </view>

    <view class="page-section">
      <view class="page-section-title">只可以横向移动</view>
      <movable-area>
        <movable-view direction="horizontal">text</movable-view>
      </movable-area>
    </view>

    <view class="page-section">
      <view class="page-section-title">只可以纵向移动</view>
      <movable-area>
        <movable-view direction="vertical">text</movable-view>
      </movable-area>
    </view>

    <view class="page-section">
      <view class="page-section-title">可超出边界</view>
      <movable-area>
        <movable-view direction="all" out-of-bounds>text</movable-view>
      </movable-area>
    </view>

    <view class="page-section">
      <view class="page-section-title">带有惯性</view>
      <movable-area>
        <movable-view direction="all" inertia>text</movable-view>
      </movable-area>
    </view>

    <view class="page-section">
      <view class="page-section-title">可放缩</view>
      <movable-area scale-area>
        <movable-view direction="all" bindchange="onChange" bindscale="onScale" scale scale-min="0.5" scale-max="4" scale-value="{{scale}}">text</movable-view>
      </movable-area>
    </view>

    <view class="btn-area">
      <button bindtap="tap2" class="page-body-button" type="primary">点击放大3倍</button>
    </view>
  </view>

</view>
```

```js
Page({
  onShareAppMessage() {
    return {
      title: 'movable-view',
      path: 'page/component/pages/movable-view/movable-view'
    }
  },

  data: {
    x: 0,
    y: 0,
    scale: 2,
  },

  tap() {
    this.setData({
      x: 30,
      y: 30
    })
  },

  tap2() {
    this.setData({
      scale: 3
    })
  },

  onChange(e) {
    console.log(e.detail)
  },

  onScale(e) {
    console.log(e.detail)
  }
})
```