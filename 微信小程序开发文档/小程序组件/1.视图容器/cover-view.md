视图容器 /cover-view /

目前[原生组件](https://developers.weixin.qq.com/miniprogram/dev/component/native-component.html)均已支持同层渲染，建议使用 [view](https://developers.weixin.qq.com/miniprogram/dev/component/view.html) 替代

> 基础库 1.4.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Windows 版**：支持
>
> **微信 Mac 版**：支持
>
> **微信 鸿蒙 OS 版**：支持

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）、WebView

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/cover-view.html#%E5%8A%9F%E8%83%BD%E6%8F%8F%E8%BF%B0) 功能描述

覆盖在原生组件之上的文本视图。

可覆盖的原生组件包括 [map](https://developers.weixin.qq.com/miniprogram/dev/component/map.html)、[video](https://developers.weixin.qq.com/miniprogram/dev/component/video.html)、[canvas](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)、[camera](https://developers.weixin.qq.com/miniprogram/dev/component/camera.html)、[live-player](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html)、[live-pusher](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)

只支持嵌套 [cover-view](https://developers.weixin.qq.com/miniprogram/dev/component/cover-view.html)、[cover-image](https://developers.weixin.qq.com/miniprogram/dev/component/cover-image.html)，可在 [cover-view](https://developers.weixin.qq.com/miniprogram/dev/component/cover-view.html) 中使用 [button](https://developers.weixin.qq.com/miniprogram/dev/component/button.html)。组件属性的长度单位默认为px，[2.4.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)起支持传入单位(rpx/px)。

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/cover-view.html#%E5%B1%9E%E6%80%A7%E8%AF%B4%E6%98%8E) 属性说明

| 属性       | 类型          | 默认值 | 必填                                                         | 说明                                                         | 最低版本 |
| ---------- | ------------- | ------ | ------------------------------------------------------------ | ------------------------------------------------------------ | -------- |
| scroll-top | number/string | 否     | 设置顶部滚动偏移量，仅在设置了 overflow-y: scroll 成为滚动元素后生效 | [2.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |          |

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/cover-view.html#Bug-Tip) Bug & Tip

1.  `tip`: [cover-view](https://developers.weixin.qq.com/miniprogram/dev/component/cover-view.html)和[cover-image](https://developers.weixin.qq.com/miniprogram/dev/component/cover-image.html)的`aria-role`仅可设置为`button`，读屏模式下才可以点击，并朗读出“按钮”；为空时可以聚焦，但不可点击
2.  `tip`: 基础库 2.2.4 起支持 touch 相关事件，也可使用 hover-class 设置点击态
3.  `tip`: 基础库 2.1.0 起支持设置 `scale` `rotate` 的 css 样式，包括 transition 动画
4.  `tip`: 基础库 1.9.90 起 `cover-view` 支持 `overflow: scroll`，但不支持动态更新 `overflow`
5.  `tip`: 基础库 1.9.90 起最外层 `cover-view` 支持 `position: fixed`
6.  `tip`: 基础库 1.9.0 起支持插在 `view` 等标签下。在此之前只可嵌套在原生组件`map`、`video`、`canvas`、`camera`内，避免嵌套在其他组件内。
7.  `tip`: 基础库 1.6.0 起支持css transition动画，`transition-property`只支持`transform (translateX, translateY)`与`opacity`。
8.  `tip`: 基础库 1.6.0 起支持css opacity。
9.  `tip`: 事件模型遵循冒泡模型，但不会冒泡到原生组件。
10.  `tip`: 文本建议都套上cover-view标签，避免排版错误。
11.  `tip`: 只支持基本的定位、布局、文本样式。不支持设置`单边的border`、`background-image`、`shadow`、`overflow: visible`等。
12.  `tip`: 建议子节点不要溢出父节点
13.  `tip`: 支持使用 z-index 控制层级
14.  `tip`: 默认设置的样式有：`white-space: nowrap;` `line-height: 1.2;` `display: block;`
15.  `bug`: 自定义组件嵌套 `cover-view` 时，自定义组件的 slot 及其父节点暂不支持通过 wx:if 控制显隐，否则会导致 `cover-view` 不显示

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/cover-view.html#%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81) 示例代码

```xml
<view class="container">
  <view class="page-body">
    <view class="page-section page-section-gap">
      <map
        style="width: 100%; height: 300px;"
        latitude="{{latitude}}"
        longitude="{{longitude}}"
      >
        <cover-view class="cover-view">
          <cover-view class="container">
            <cover-view class="flex-wrp" style="flex-direction:row;">
              <cover-view class="flex-item demo-text-1"></cover-view>
              <cover-view class="flex-item demo-text-2"></cover-view>
              <cover-view class="flex-item demo-text-3"></cover-view>
            </cover-view>
          </cover-view>
        </cover-view>
      </map>
    </view>
  </view>
</view>
```

```css
.cover-view {
  position: absolute;
  top: calc(50% - 150rpx);
  left: calc(50% - 300rpx);
  /* opacity: .7; */
}

.flex-wrp{
  display:flex;
}

.flex-item{
  width: 200rpx;
  height: 300rpx;
  font-size: 26rpx;
}

.demo-text-1 {
  background: rgba(26, 173, 25, 0.7);
}

.demo-text-2 {
  background: rgba(39, 130, 215, 0.7);
}

.demo-text-3 {
  background: rgba(255, 255, 255, 0.7);
}
```

```js
Page({
  onShareAppMessage() {
    return {
      title: 'cover-view',
      path: 'page/component/pages/cover-view/cover-view'
    }
  },

  data: {
    latitude: 23.099994,
    longitude: 113.324520,
  }
})
```