# sticky-header

> 基础库 2.29.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)、[Skyline 迁移起步](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/migration.html)

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）

## 功能描述

吸顶布局容器，仅支持作为 `<scroll-view type="custom">` 模式的直接子节点或 [sticky-section](https://developers.weixin.qq.com/miniprogram/dev/component/sticky-section.html) 组件直接子节点

## 属性说明

| 属性                  | 类型        | 默认值       | 必填 | 说明                                                         | 最低版本                                                     |
| --------------------- | ----------- | ------------ | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| offset-top            | number      | 0            | 否   | 吸顶时与视窗顶部的距离(px)                                   | [3.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| allow-overlapping     | bool        | false        | 否   | 是否允许与前一个 sticky-header 重叠                          | [3.7.11](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| padding               | Array       | [0, 0, 0, 0] | 否   | 长度为 4 的数组，按 top、right、bottom、left 顺序指定内边距(px) | [3.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bind:stickontopchange | eventhandle |              | 否   | 吸顶状态变化事件，仅支持非 worklet 的组件方法作为回调。event.detail = { isStickOnTop }，当 sticky-header 吸顶时为 true，否则为 false。 | [3.6.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/v3jr1Wm17ZYE)