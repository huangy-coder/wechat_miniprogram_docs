视图容器 /swiper-item /

> 基础库 1.0.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Windows 版**：支持
>
> **微信 Mac 版**：支持
>
> **微信 鸿蒙 OS 版**：支持

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）、WebView

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/swiper-item.html#%E5%8A%9F%E8%83%BD%E6%8F%8F%E8%BF%B0) 功能描述

仅可放置在[swiper](https://developers.weixin.qq.com/miniprogram/dev/component/swiper.html)组件中，宽高自动设置为100%。

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/swiper-item.html#%E5%B1%9E%E6%80%A7%E8%AF%B4%E6%98%8E) 属性说明

| 属性                    | 类型    | 默认值 | 必填                    | 说明                                                         | 最低版本                                                     |
| ----------------------- | ------- | ------ | ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| item-id                 | string  | 否     | 该 swiper-item 的标识符 | [1.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |                                                              |
| skip-hidden-item-layout | boolean | false  | 否                      | 是否跳过未显示的滑块布局，设为 true 可优化复杂情况下的滑动性能，但会丢失隐藏状态滑块的布局信息 | [1.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |