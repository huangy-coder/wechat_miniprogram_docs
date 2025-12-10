# icon

> 基础库 1.0.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Windows 版**：支持
> 
> **微信 Mac 版**：支持
> 
> **微信 鸿蒙 OS 版**：支持

渲染框架支持情况：WebView

## 功能描述

图标组件

## 属性说明

|属性|类型|默认值|必填|说明|最低版本|
|---|---|---|---|---|---|
|type|string||是|icon的类型，有效值：success, success_no_circle, info, warn, waiting, cancel, download, search, clear|[1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)|
|size|number/string|23|否|icon的大小，单位默认为px，[2.4.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)起支持传入单位(rpx/px)，[2.21.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)起支持传入其余单位(rem 等)。|[1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)|
|color|string||否|icon的颜色，同css的color|[1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)|

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/LK9tzcmM6QYj "在开发者工具中预览效果")

```xml
<view class="container">
  <view class="icon-box">
    <icon class="icon-box-img" type="success" size="93"></icon>
    <view class="icon-box-ctn">
      <view class="icon-box-title">成功</view>
      <view class="icon-box-desc">用于表示操作顺利完成</view>
    </view>
  </view>
  <view class="icon-box">
    <icon class="icon-box-img" type="info" size="93"></icon>
    <view class="icon-box-ctn">
      <view class="icon-box-title">提示</view>
      <view class="icon-box-desc">用于表示信息提示；也常用于缺乏条件的操作拦截，提示用户所需信息</view>
    </view>
  </view>
  <view class="icon-box">
    <icon class="icon-box-img" type="warn" size="93" color="#C9C9C9"></icon>
    <view class="icon-box-ctn">
      <view class="icon-box-title">普通警告</view>
      <view class="icon-box-desc">用于表示操作后将引起一定后果的情况；也用于表示由于系统原因而造成的负向结果</view>
    </view>
  </view>
  <view class="icon-box">
    <icon class="icon-box-img" type="warn" size="93"></icon>
    <view class="icon-box-ctn">
      <view class="icon-box-title">强烈警告</view>
      <view class="icon-box-desc">用于表示由于用户原因造成的负向结果；也用于表示操作后将引起不可挽回的严重后果的情况</view>
    </view>
  </view>
  <view class="icon-box">
    <icon class="icon-box-img" type="waiting" size="93"></icon>
    <view class="icon-box-ctn">
      <view class="icon-box-title">等待</view>
      <view class="icon-box-desc">用于表示等待，告知用户结果需等待</view>
    </view>
  </view>
  <view class="icon-box">
    <view class="icon-small-wrp">
      <icon class="icon-small" type="success_no_circle" size="23"></icon>
    </view>
    <view class="icon-box-ctn">
      <view class="icon-box-title">多选控件图标_已选择</view>
      <view class="icon-box-desc">用于多选控件中，表示已选择该项目</view>
    </view>
  </view>
  <view class="icon-box">
    <view class="icon-small-wrp">
      <icon class="icon-small" type="circle" size="23"></icon>
    </view>
    <view class="icon-box-ctn">
      <view class="icon-box-title">多选控件图标_未选择</view>
      <view class="icon-box-desc">用于多选控件中，表示该项目可被选择，但还未选择</view>
    </view>
  </view>
  <view class="icon-box">
    <view class="icon-small-wrp">
      <icon class="icon-small" type="warn" size="23"></icon>
    </view>
    <view class="icon-box-ctn">
      <view class="icon-box-title">错误提示</view>
      <view class="icon-box-desc">用于在表单中表示出现错误</view>
    </view>
  </view>
  <view class="icon-box">
    <view class="icon-small-wrp">
      <icon class="icon-small" type="success" size="23"></icon>
    </view>
    <view class="icon-box-ctn">
      <view class="icon-box-title">单选控件图标_已选择</view>
      <view class="icon-box-desc">用于单选控件中，表示已选择该项目</view>
    </view>
  </view>
  <view class="icon-box">
    <view class="icon-small-wrp">
      <icon class="icon-small" type="download" size="23"></icon>
    </view>
    <view class="icon-box-ctn">
      <view class="icon-box-title">下载</view>
      <view class="icon-box-desc">用于表示可下载</view>
    </view>
  </view>
  <view class="icon-box">
    <view class="icon-small-wrp">
      <icon class="icon-small" type="info_circle" size="23"></icon>
    </view>
    <view class="icon-box-ctn">
      <view class="icon-box-title">提示</view>
      <view class="icon-box-desc">用于在表单中表示有信息提示</view>
    </view>
  </view>
  <view class="icon-box">
    <view class="icon-small-wrp">
      <icon class="icon-small" type="cancel" size="23"></icon>
    </view>
    <view class="icon-box-ctn">
      <view class="icon-box-title">停止或关闭</view>
      <view class="icon-box-desc">用于在表单中，表示关闭或停止</view>
    </view>
  </view>
  <view class="icon-box">
    <view class="icon-small-wrp">
      <icon class="icon-small" type="search" size="14"></icon>
    </view>
    <view class="icon-box-ctn">
      <view class="icon-box-title">搜索</view>
      <view class="icon-box-desc">用于搜索控件中，表示可搜索</view>
    </view>
  </view>

</view>
```

```js
Page({
  data: {
    iconSize: [20, 30, 40, 50, 60, 70],
    iconColor: [
      'red', 'orange', 'yellow', 'green', 'rgb(0,255,255)', 'blue', 'purple'
    ],
    iconType: [
      'success', 'success_no_circle', 'info', 'warn', 'waiting', 'cancel', 'download', 'search', 'clear'
    ]
  }
})
```