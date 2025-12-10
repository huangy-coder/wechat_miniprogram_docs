# radio

> 基础库 1.0.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Windows 版**：支持
>
> **微信 Mac 版**：支持
>
> **微信 鸿蒙 OS 版**：支持

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）、WebView

## 功能描述

单选项目。

## 属性说明

| 属性     | 类型    | 默认值  | 必填 | 说明                                                         | 最低版本                                                     |
| -------- | ------- | ------- | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| value    | string  |         | 否   | [radio](https://developers.weixin.qq.com/miniprogram/dev/component/radio.html) 标识。当该[radio](https://developers.weixin.qq.com/miniprogram/dev/component/radio.html) 选中时，[radio-group](https://developers.weixin.qq.com/miniprogram/dev/component/radio-group.html) 的 change 事件会携带[radio](https://developers.weixin.qq.com/miniprogram/dev/component/radio.html)的value | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| checked  | boolean | false   | 否   | 当前是否选中                                                 | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| disabled | boolean | false   | 否   | 是否禁用                                                     | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| color    | string  | #09BB07 | 否   | radio的颜色，同css的color                                    | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/p65odSmE7IJV)

```xml
<view class="page-body">
  <view class="page-section">
    <view class="page-section-title">默认样式</view>
    <label class="radio">
      <radio value="r1" checked="true"/>选中
    </label>
    <label class="radio">
      <radio value="r2" />未选中
    </label>
  </view>


  <view class="page-section">
    <view class="page-section-title">推荐展示样式</view>
    <view class="weui-cells weui-cells_after-title">
      <radio-group bindchange="radioChange">
        <label class="weui-cell weui-check__label" wx:for="{{items}}" wx:key="{{item.value}}">

          <view class="weui-cell__hd">
            <radio value="{{item.value}}" checked="true"/>
          </view>
          <view class="weui-cell__bd">{{item.name}}</view>
        </label>
      </radio-group>
    </view>
  </view>
</view>
```

```js
Page({
  onShareAppMessage() {
    return {
      title: 'radio',
      path: 'page/component/pages/radio/radio'
    }
  },

  data: {
    items: [
      {value: 'USA', name: '美国'},
      {value: 'CHN', name: '中国', checked: 'true'},
      {value: 'BRA', name: '巴西'},
      {value: 'JPN', name: '日本'},
      {value: 'ENG', name: '英国'},
      {value: 'FRA', name: '法国'},
    ]
  },

  radioChange(e) {
    console.log('radio发生change事件，携带value值为：', e.detail.value)

    const items = this.data.items
    for (let i = 0, len = items.length; i < len; ++i) {
      items[i].checked = items[i].value === e.detail.value
    }

    this.setData({
      items
    })
  }
})
```