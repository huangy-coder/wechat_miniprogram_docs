基础内容 /text /

> 基础库 1.0.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Windows 版**：支持
>
> **微信 Mac 版**：支持
>
> **微信 鸿蒙 OS 版**：支持

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）、WebView

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/text.html#%E5%8A%9F%E8%83%BD%E6%8F%8F%E8%BF%B0) 功能描述

文本。

1.  内联文本只能用 text 组件，不能用 view，如 <text> foo <text>bar</text> </text>
    
2.  新增 span 组件用于内联文本和图片，如 <span> <image> </image> <text>bar</text> </span>

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/text.html#%E9%80%9A%E7%94%A8%E5%B1%9E%E6%80%A7) 通用属性

| 属性        | 类型    | 默认值 | 必填 | 说明                                                | 最低版本                                                     |
| ----------- | ------- | ------ | ---- | --------------------------------------------------- | ------------------------------------------------------------ |
| selectable  | boolean | false  | 否   | 文本是否可选 (已废弃)                               | [1.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| user-select | boolean | false  | 否   | 文本是否可选，该属性会使文本节点显示为 inline-block | [2.12.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/text.html#Skyline-%E7%89%B9%E6%9C%89%E5%B1%9E%E6%80%A7) Skyline 特有属性

| 属性      | 类型   | 默认值  | 必填             | 说明         |
| --------- | ------ | ------- | ---------------- | ------------ |
| overflow  | string | visible | 是               | 文本溢出处理 |
| 合法值    |        |         |                  |              |
| max-lines | number | 是      | 限制文本最大行数 |              |

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/text.html#WebView-%E7%89%B9%E6%9C%89%E5%B1%9E%E6%80%A7) WebView 特有属性

| 属性   | 类型    | 默认值 | 必填         | 说明                                                         | 最低版本                                                     |
| ------ | ------- | ------ | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| space  | string  | 否     | 显示连续空格 | [1.4.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |                                                              |
| 合法值 |         |        |              |                                                              |                                                              |
| decode | boolean | false  | 否           | 是否解码                                                     | [1.4.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/text.html#Bug-Tip) Bug & Tip

1.  `tip`: decode可以解析的有 `&nbsp;` `&lt;` `&gt;` `&amp;` `&apos;` `&ensp;` `&emsp;`
2.  `tip`: 各个操作系统的空格标准并不一致。
3.  `tip`:[text](https://developers.weixin.qq.com/miniprogram/dev/component/text.html) 组件内只支持 [text](https://developers.weixin.qq.com/miniprogram/dev/component/text.html) 嵌套。
4.  `tip`: 除了文本节点以外的其他节点都无法长按选中。
5.  `bug`: 基础库版本低于 `2.1.0` 时， [text](https://developers.weixin.qq.com/miniprogram/dev/component/text.html) 组件内嵌的 [text](https://developers.weixin.qq.com/miniprogram/dev/component/text.html) style 设置可能不会生效。

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/text.html#%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81) 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/LQxYkQmm7fJj "在开发者工具中预览效果")



```xml
<view class="container">
  <view class="page-body">
    <view class="page-section page-section-spacing">
      <view class="text-box" scroll-y="true" scroll-top="{{scrollTop}}">
        <text>{{text}}</text>
      </view>
      <button disabled="{{!canAdd}}" bindtap="add">add line</button>
      <button disabled="{{!canRemove}}" bindtap="remove">remove line</button>
    </view>
  </view>
</view>
```

```js
const texts = [
  '2011年1月，微信1.0发布',
  '同年5月，微信2.0语音对讲发布',
  '10月，微信3.0新增摇一摇功能',
  '2012年3月，微信用户突破1亿',
  '4月份，微信4.0朋友圈发布',
  '同年7月，微信4.2发布公众平台',
  '2013年8月，微信5.0发布微信支付',
  '2014年9月，企业号发布',
  '同月，发布微信卡包',
  '2015年1月，微信第一条朋友圈广告',
  '2016年1月，企业微信发布',
  '2017年1月，小程序发布',
  '......'
]

Page({
  onShareAppMessage() {
    return {
      title: 'text',
      path: 'page/component/pages/text/text'
    }
  },

  data: {
    text: '',
    canAdd: true,
    canRemove: false
  },
  extraLine: [],

  add() {
    this.extraLine.push(texts[this.extraLine.length % 12])
    this.setData({
      text: this.extraLine.join('\n'),
      canAdd: this.extraLine.length < 12,
      canRemove: this.extraLine.length > 0
    })
    setTimeout(() => {
      this.setData({
        scrollTop: 99999
      })
    }, 0)
  },
  remove() {
    if (this.extraLine.length > 0) {
      this.extraLine.pop()
      this.setData({
        text: this.extraLine.join('\n'),
        canAdd: this.extraLine.length < 12,
        canRemove: this.extraLine.length > 0,
      })
    }
    setTimeout(() => {
      this.setData({
        scrollTop: 99999
      })
    }, 0)
  }
})
```