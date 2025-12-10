视图容器 /view /

> 基础库 1.0.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Windows 版**：支持
>
> **微信 Mac 版**：支持
>
> **微信 鸿蒙 OS 版**：支持

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）、WebView

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/view.html#%E5%8A%9F%E8%83%BD%E6%8F%8F%E8%BF%B0) 功能描述

视图容器

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/view.html#%E5%B1%9E%E6%80%A7%E8%AF%B4%E6%98%8E) 属性说明

| 属性                   | 类型    | 默认值 | 必填 | 说明                                                         | 最低版本                                                     |
| ---------------------- | ------- | ------ | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| hover-class            | string  | none   | 否   | 指定按下去的样式类。当 `hover-class="none"` 时，没有点击态效果 | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| hover-stop-propagation | boolean | false  | 否   | 指定是否阻止本节点的祖先节点出现点击态                       | [1.5.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| hover-start-time       | number  | 50     | 否   | 按住后多久出现点击态，单位毫秒                               | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| hover-stay-time        | number  | 400    | 否   | 手指松开后点击态保留时间，单位毫秒                           | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/view.html#Bug-Tip) Bug & Tip

1.  `tip`: 如果需要使用滚动视图，请使用 [scroll-view](https://developers.weixin.qq.com/miniprogram/dev/component/scroll-view.html)

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/view.html#%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81) 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/v2BmcQmM7qJa "在开发者工具中预览效果")