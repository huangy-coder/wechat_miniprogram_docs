基础内容 /selection /

> 基础库 3.6.4 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

渲染框架支持情况：WebView

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/selection.html#%E5%8A%9F%E8%83%BD%E6%8F%8F%E8%BF%B0) 功能描述

局部文本选区。

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/selection.html#%E5%B1%9E%E6%80%A7%E8%AF%B4%E6%98%8E) 属性说明

| 属性                 | 类型        | 默认值 | 必填                                                         | 说明                                                         | 最低版本                                                     |
| -------------------- | ----------- | ------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| disable-context-menu | boolean     | false  | 否                                                           | 是否隐藏客户端原生文本选区按钮                               | [3.6.4](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindselectionchange  | eventhandle | 否     | 当选区发生变化时触发 selectionchange 事件 event.detail = { isCollapsed, selectedString, firstNodeId, firstOffset, lastNodeId, lastOffset, firstRangeRect } | [3.6.4](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |                                                              |

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/selection.html#Bug-Tip) Bug & Tip

1.  `tip`: 长按选区在 `wx-selection` 内才可以触发 disable-context-menu 的效果
2.  `tip`: `text` 和 `rich-text` 组件需要设置 `user-select` 为 `true`。
3.  `tip`: `firstNodeId` 和 `lastNodeId` 需要 `text` 和 `rich-text` 组件设置 `id`。
4.  `tip`: 超出 `wx-selection` 的情况下 `firstOffset` 和 `lastOffset` 为空。

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/selection.html#%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81) 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/nwLKK6mU7VVb "在开发者工具中预览效果")