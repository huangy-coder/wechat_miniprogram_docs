# image

> 基础库 1.0.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Windows 版**：支持
>
> **微信 Mac 版**：支持
>
> **微信 鸿蒙 OS 版**：支持

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）、WebView

## 功能描述

图片。支持 JPG、PNG、SVG、WEBP、GIF 等格式，[2.3.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 起支持云文件ID。

1. 使用 svg 格式且 mode=scaleToFill 时，WebView 会居中（除非 svg 里加上 preserveAspectRatio="none"），Skyline 则会撑满 
2. svg 格式不支持百分比单位 
3. svg 格式不支持 <style> element

## 通用属性

|      | 属性                                                         | 类型        | 默认值      | 必填 | 说明                                                         | 最低版本                                                     |
| ---- | ------------------------------------------------------------ | ----------- | ----------- | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|      | src                                                          | string      |             | 否   | 图片资源地址                                                 | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | mode                                                         | string      | scaleToFill | 否   | 图片裁剪、缩放的模式                                         | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | 合法值说明最低版本scaleToFill缩放模式，不保持纵横比缩放图片，使图片的宽高完全拉伸至填满 image 元素aspectFit缩放模式，保持纵横比缩放图片，使图片的长边能完全显示出来。也就是说，可以完整地将图片显示出来。aspectFill缩放模式，保持纵横比缩放图片，只保证图片的短边能完全显示出来。也就是说，图片通常只在水平或垂直方向是完整的，另一个方向将会发生截取。widthFix缩放模式，宽度不变，高度自动变化，保持原图宽高比不变heightFix缩放模式，高度不变，宽度自动变化，保持原图宽高比不变[2.10.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)top裁剪模式，不缩放图片，只显示图片的顶部区域。仅 Webview 支持。bottom裁剪模式，不缩放图片，只显示图片的底部区域。仅 Webview 支持。center裁剪模式，不缩放图片，只显示图片的中间区域。仅 Webview 支持。left裁剪模式，不缩放图片，只显示图片的左边区域。仅 Webview 支持。right裁剪模式，不缩放图片，只显示图片的右边区域。仅 Webview 支持。top left裁剪模式，不缩放图片，只显示图片的左上边区域。仅 Webview 支持。top right裁剪模式，不缩放图片，只显示图片的右上边区域。仅 Webview 支持。bottom left裁剪模式，不缩放图片，只显示图片的左下边区域。仅 Webview 支持。bottom right裁剪模式，不缩放图片，只显示图片的右下边区域。仅 Webview 支持。 |             |             |      |                                                              |                                                              |
|      | show-menu-by-longpress                                       | boolean     | false       | 否   | 长按图片显示发送给朋友、收藏、保存图片、搜一搜、打开名片/前往群聊/打开小程序（若图片中包含对应二维码或小程序码）的菜单。 | [2.7.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | binderror                                                    | eventhandle |             | 否   | 当错误发生时触发，event.detail = {errMsg}                    | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | bindload                                                     | eventhandle |             | 否   | 当图片载入完毕时触发，event.detail = {height, width}         | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## Skyline 特有属性

|      | 属性    | 类型    | 默认值 | 必填 | 说明     |
| ---- | ------- | ------- | ------ | ---- | -------- |
|      | fade-in | boolean | false  | 否   | 是否渐显 |

## WebView 特有属性

|      | 属性       | 类型    | 默认值 | 必填 | 说明                                                         | 最低版本                                                     |
| ---- | ---------- | ------- | ------ | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|      | webp       | boolean | false  | 否   | 默认不解析 webP 格式，只支持网络资源                         | [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | lazy-load  | boolean | false  | 否   | 图片懒加载，在即将进入一定范围（上下三屏）时才开始加载。Skyline 默认懒加载。 | [1.5.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | forceHttps | boolean | false  | 否   | 自动将 http 链接替换为 https 链接                            | [3.9.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 支持长按识别的码

| 类型           | 说明                               | 最低版本                                                     |
| -------------- | ---------------------------------- | ------------------------------------------------------------ |
| 小程序码       |                                    |                                                              |
| 微信个人码     |                                    | [2.18.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| 企业微信个人码 |                                    | [2.18.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| 普通群码       | 指仅包含微信用户的群               | [2.18.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| 互通群码       | 指既有微信用户也有企业微信用户的群 | [2.18.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| 公众号二维码   |                                    | [2.18.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## Bug & Tip

1. `tip`：image组件默认宽度320px、高度240px
2. `tip`：image组件进行缩放时，计算出来的宽高可能带有小数，在不同webview内核下渲染可能会被抹去小数部分

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/NwPpTRmS7AJf)

```xml
<view class="page">
  <view class="page__hd">
    <text class="page__title">image</text>
    <text class="page__desc">图片</text>
  </view>
  <view class="page__bd">
    <view class="section section_gap" wx:for="{{array}}" wx:for-item="item">
      <view class="section__title">{{item.text}}</view>
      <view class="section__ctn">
        <image style="width: 200px; height: 200px; background-color: #eeeeee;" mode="{{item.mode}}" src="{{src}}"></image>
      </view>
    </view>
  </view>
</view>
```

```js

Page({
  data: {
    array: [{
      mode: 'scaleToFill',
      text: 'scaleToFill：不保持纵横比缩放图片，使图片完全适应'
    }, {
      mode: 'aspectFit',
      text: 'aspectFit：保持纵横比缩放图片，使图片的长边能完全显示出来'
    }, {
      mode: 'aspectFill',
      text: 'aspectFill：保持纵横比缩放图片，只保证图片的短边能完全显示出来'
    }, {
      mode: 'top',
      text: 'top：不缩放图片，只显示图片的顶部区域'
    }, {
      mode: 'bottom',
      text: 'bottom：不缩放图片，只显示图片的底部区域'
    }, {
      mode: 'center',
      text: 'center：不缩放图片，只显示图片的中间区域'
    }, {
      mode: 'left',
      text: 'left：不缩放图片，只显示图片的左边区域'
    }, {
      mode: 'right',
      text: 'right：不缩放图片，只显示图片的右边边区域'
    }, {
      mode: 'top left',
      text: 'top left：不缩放图片，只显示图片的左上边区域'
    }, {
      mode: 'top right',
      text: 'top right：不缩放图片，只显示图片的右上边区域'
    }, {
      mode: 'bottom left',
      text: 'bottom left：不缩放图片，只显示图片的左下边区域'
    }, {
      mode: 'bottom right',
      text: 'bottom right：不缩放图片，只显示图片的右下边区域'
    }],
    src: 'https://res.wx.qq.com/wxdoc/dist/assets/img/0.4cb08bb4.jpg'
  },
  imageError: function(e) {
    console.log('image3发生error事件，携带值为', e.detail.errMsg)
  }
})
```