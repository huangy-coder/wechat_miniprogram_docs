表单组件 /checkbox /

> 基础库 1.0.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Windows 版**：支持
>
> **微信 Mac 版**：支持
>
> **微信 鸿蒙 OS 版**：支持

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）、WebView

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/checkbox.html#%E5%8A%9F%E8%83%BD%E6%8F%8F%E8%BF%B0) 功能描述

多选项目。

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/checkbox.html#%E5%B1%9E%E6%80%A7%E8%AF%B4%E6%98%8E) 属性说明

| 属性     | 类型    | 默认值  | 必填                                                         | 说明                                                         | 最低版本                                                     |
| -------- | ------- | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| value    | string  | 否      | [checkbox](https://developers.weixin.qq.com/miniprogram/dev/component/checkbox.html)标识，选中时触发[checkbox-group](https://developers.weixin.qq.com/miniprogram/dev/component/checkbox-group.html)的 change 事件，并携带 [checkbox](https://developers.weixin.qq.com/miniprogram/dev/component/checkbox.html) 的 value | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |                                                              |
| disabled | boolean | false   | 否                                                           | 是否禁用                                                     | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| checked  | boolean | false   | 否                                                           | 当前是否选中，可用来设置默认选中                             | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| color    | string  | #09BB07 | 否                                                           | checkbox的颜色，同css的color                                 | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/checkbox.html#%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81) 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/4K0JISmt7uJR "在开发者工具中预览效果")

```xml
<view class="container">
  <view class="page-body">
    <view class="page-section page-section-gap">
      <view class="page-section-title">默认样式</view>
      <label class="checkbox">
        <checkbox value="cb" checked="true"/>选中
      </label>
      <label class="checkbox">
        <checkbox value="cb" />未选中
      </label>
    </view>
  
    <view class="page-section">
      <view class="page-section-title">推荐展示样式</view>
      <view class="weui-cells weui-cells_after-title">
        <checkbox-group bindchange="checkboxChange">
          <label class="weui-cell weui-check__label" wx:for="{{items}}" wx:key="{{item.value}}">
            <view class="weui-cell__hd">
              <checkbox value="{{item.value}}" checked="{{item.checked}}"/>
            </view>
            <view class="weui-cell__bd">{{item.name}}</view>
          </label>
        </checkbox-group>
      </view>
    </view>
  </view>
  
</view>
```

```js
Page({
  onShareAppMessage() {
    return {
      title: 'checkbox',
      path: 'page/component/pages/checkbox/checkbox'
    }
  },

  data: {
    items: [
      {value: 'USA', name: '美国'},
      {value: 'CHN', name: '中国', checked: 'true'},
      {value: 'BRA', name: '巴西'},
      {value: 'JPN', name: '日本'},
      {value: 'ENG', name: '英国'},
      {value: 'FRA', name: '法国'}
    ]
  },

  checkboxChange(e) {
    console.log('checkbox发生change事件，携带value值为：', e.detail.value)

    const items = this.data.items
    const values = e.detail.value
    for (let i = 0, lenI = items.length; i < lenI; ++i) {
      items[i].checked = false

      for (let j = 0, lenJ = values.length; j < lenJ; ++j) {
        if (items[i].value === values[j]) {
          items[i].checked = true
          break
        }
      }
    }

    this.setData({
      items
    })
  }
})
```