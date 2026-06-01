# worklet.scrollViewContext.scrollTo(Object object)

> 官方文档：[worklet.scrollViewContext.scrollTo(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/base/worklet.scrollViewContext.scrollTo.html)
> 所属分类：[界面](../../界面目录.md)
> 导航路径：界面 / worklet 动画 / 基础 / worklet.scrollViewContext.scrollTo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.3.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

> 相关文档: [worklet 动画](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/worklet.html)、[NodesRef.ref](../../../19.WXML/NodesRef.ref.md)

## 功能描述

滚动至指定位置

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| top | number |   | 否 | 顶部距离 |
| left | number |   | 否 | 左边界距离 |
| duration | number |   | 否 | 滚动动画时长 |
| animated | boolean |   | 否 | 是否启用滚动动画 |
| easingFunction | string |   | 否 | 动画曲线 |

## 示例代码

```javascript
const { scrollViewContext } = wx.workelt

Page {
  onLoad() {
    this.scrollRef = shared()
    this.createSelectorQuery().select('.scrollable').ref(function(res) {
      this.scrollRef.value = res.ref
    }).exec()
  },

  onTap() {
    'worklet'
    scrollViewContext.scrollTo(this.scrollRef.value, {
      top: 200,
      duration: 2000,
      animated: true,
      easingFunction: 'ease'
    })
  }
}
```

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/iYlm76mv7uUg)
