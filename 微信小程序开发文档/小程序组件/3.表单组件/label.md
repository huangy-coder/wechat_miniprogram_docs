# label

> 基础库 1.0.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Windows 版**：支持
>
> **微信 Mac 版**：支持
>
> **微信 鸿蒙 OS 版**：支持

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）、WebView

## 功能描述

用来改进表单组件的可用性。

使用for属性找到对应的id，或者将控件放在该标签下，当点击时，就会触发对应的控件。 for优先级高于内部控件，内部有多个控件的时候默认触发第一个控件。 目前可以绑定的控件有：[button](https://developers.weixin.qq.com/miniprogram/dev/component/button.html), [checkbox](https://developers.weixin.qq.com/miniprogram/dev/component/checkbox.html), [radio](https://developers.weixin.qq.com/miniprogram/dev/component/radio.html), [switch](https://developers.weixin.qq.com/miniprogram/dev/component/switch.html), [input](https://developers.weixin.qq.com/miniprogram/dev/component/input.html)。

## 属性说明

| 属性 | 类型   | 默认值 | 必填 | 说明          | 最低版本                                                     |
| ---- | ------ | ------ | ---- | ------------- | ------------------------------------------------------------ |
| for  | string |        | 否   | 绑定控件的 id | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/vt1UCSmQ7MJY)

```xml
<view class="container">
  <view class="page-body">
    <view class="page-section page-section-gap">
      <view class="page-section-title">表单组件在label内</view>
      <checkbox-group class="group" bindchange="checkboxChange">
        <view class="label-1" wx:for="{{checkboxItems}}">
          <label>
            <checkbox value="{{item.name}}" checked="{{item.checked}}"></checkbox>
            <text class="label-1-text">{{item.value}}</text>
          </label>
        </view>
      </checkbox-group>
    </view>

    <view class="page-section page-section-gap">
      <view class="page-section-title">label用for标识表单组件</view>
      <radio-group class="group" bindchange="radioChange">
        <view class="label-2" wx:for="{{radioItems}}">
          <radio id="{{item.name}}" value="{{item.name}}" checked="{{item.checked}}"></radio>
          <label class="label-2-text" for="{{item.name}}"><text>{{item.name}}</text></label>
        </view>
      </radio-group>
    </view>

    <view class="page-section page-section-gap">
      <view class="page-section-title">label内有多个时选中第一个</view>
      <label class="label-3">
        <checkbox class="checkbox-3">选项一</checkbox>
        <checkbox class="checkbox-3">选项二</checkbox>
        <view class="label-3-text">点击该label下的文字默认选中第一个checkbox</view>
      </label>
    </view>
  </view>
</view>
```

```css
.label-1, .label-2{
  margin: 30rpx 0;
}
.label-3-text{
  color: #576B95;
  font-size: 28rpx;
}
.checkbox-3{
  display: block;
  margin: 30rpx 0;
}
```

```js
Page({
  onShareAppMessage() {
    return {
      title: 'label',
      path: 'page/component/pages/label/label'
    }
  },

  data: {
    checkboxItems: [
      {name: 'USA', value: '美国'},
      {name: 'CHN', value: '中国', checked: 'true'}
    ],
    radioItems: [
      {name: 'USA', value: '美国'},
      {name: 'CHN', value: '中国', checked: 'true'}
    ],
    hidden: false
  },

  checkboxChange(e) {
    const checked = e.detail.value
    const changed = {}
    for (let i = 0; i < this.data.checkboxItems.length; i++) {
      if (checked.indexOf(this.data.checkboxItems[i].name) !== -1) {
        changed['checkboxItems[' + i + '].checked'] = true
      } else {
        changed['checkboxItems[' + i + '].checked'] = false
      }
    }
    this.setData(changed)
  },

  radioChange(e) {
    const checked = e.detail.value
    const changed = {}
    for (let i = 0; i < this.data.radioItems.length; i++) {
      if (checked.indexOf(this.data.radioItems[i].name) !== -1) {
        changed['radioItems[' + i + '].checked'] = true
      } else {
        changed['radioItems[' + i + '].checked'] = false
      }
    }
    this.setData(changed)
  },

  tapEvent() {
    console.log('按钮被点击')
  }
})
```