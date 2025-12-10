# switch

> 基础库 1.0.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Windows 版**：支持
>
> **微信 Mac 版**：支持
>
> **微信 鸿蒙 OS 版**：支持

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）、WebView

## 功能描述

开关选择器。

## 属性说明

| 属性       | 类型        | 默认值  | 必填 | 说明                                                         | 最低版本                                                     |
| ---------- | ----------- | ------- | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| checked    | boolean     | false   | 否   | 是否选中                                                     | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| disabled   | boolean     | false   | 否   | 是否禁用                                                     | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| type       | string      | switch  | 否   | 样式，有效值：switch, checkbox                               | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| color      | string      | #04BE02 | 否   | switch 的颜色，同 css 的 color                               | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindchange | eventhandle |         | 否   | 点击导致 checked 改变时会触发 change 事件，event.detail={ value} | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## Bug & Tip

1. `tip`: switch类型切换时在iOS自带振动反馈，可在系统设置 -> 声音与触感 -> 系统触感反馈中关闭

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/6db9lcmu6VYt)

```xml
<view class="page">
    <view class="page__hd">
        <text class="page__title">switch</text>
        <text class="page__desc">开关</text>
    </view>
    <view class="page__bd">
        <view class="section section_gap">
            <view class="section__title">type="switch"</view>
            <view class="body-view">
                <switch checked="{{switch1Checked}}" bindchange="switch1Change"/>
            </view>
        </view>

        <view class="section section_gap">
            <view class="section__title">type="checkbox"</view>
            <view class="body-view">
                <switch type="checkbox" checked="{{switch2Checked}}" bindchange="switch2Change"/>
            </view>
        </view>
    </view>
</view>
```



```js
var pageData = {
  data: {
    switch1Checked: true,
    switch2Checked: false,
    switch1Style: '',
    switch2Style: 'text-decoration: line-through'
  }
}
for (var i = 1; i <= 2; ++i) {
  (function (index) {
    pageData[`switch${index}Change`] = function (e) {
      console.log(`switch${index}发生change事件，携带值为`, e.detail.value)
      var obj = {}
      obj[`switch${index}Checked`] = e.detail.value
      this.setData(obj)
      obj = {}
      obj[`switch${index}Style`] = e.detail.value ? '' : 'text-decoration: line-through'
      this.setData(obj)
    }
  })(i)
}
Page(pageData)
```