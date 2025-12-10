# nested-scroll-body

> 基础库 3.2.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)、[Skyline 迁移起步](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/migration.html)

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）

## 功能描述

嵌套 scroll-view 场景中属于里层 scroll-view 的节点，仅支持作为 `<scroll-view type="nested">` 模式的直接子节点。不支持复数子节点，渲染时会取其第一个子节点来渲染。具体用法可参考 [scroll-view](https://developers.weixin.qq.com/miniprogram/dev/component/scroll-view.html#嵌套模式使用方法)

## 属性说明

| 属性       | 类型   | 默认值 | 必填 | 说明                                                         | 最低版本                                                     |
| ---------- | ------ | ------ | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| offset-top | number | 0      | 否   | 滚动目标距离顶部的距离(px)。在外层 scroll-view 滚动时此组件会在主轴方向会逐渐撑开，直到此组件顶部与视窗顶部距离为该属性值时才开始里层 scroll-view 的滚动。默认为 0，即表示此组件撑开到顶部与视窗顶部齐平时才开始里层 scroll-view 的滚动。 | [3.6.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 使用方法

```xml
<scroll-view
  type="nested"
  scroll-y
>
  <nested-scroll-header>
    <view></view>
  </nested-scroll-header>
  <nested-scroll-body>
    <scroll-view
      type="list"
      scroll-y
    >
      <view>嵌套里层的 scroll-view</view>
    </scroll-view>
    <view>不会渲染，因为 nested-scroll-body 只会渲染第一个子节点</view>
  </nested-scroll-body>
</scroll-view>
```