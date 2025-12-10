基础内容 /progress /

> 基础库 1.0.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Windows 版**：支持
>
> **微信 Mac 版**：支持

渲染框架支持情况：WebView

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/progress.html#%E5%8A%9F%E8%83%BD%E6%8F%8F%E8%BF%B0) 功能描述

进度条。组件属性的长度单位默认为px，[2.4.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)起支持传入单位(rpx/px)。

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/progress.html#%E5%B1%9E%E6%80%A7%E8%AF%B4%E6%98%8E) 属性说明

| 属性            | 类型          | 默认值    | 必填         | 说明                                                         | 最低版本                                                     |
| --------------- | ------------- | --------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| percent         | number        | 否        | 百分比0~100  | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |                                                              |
| show-info       | boolean       | false     | 否           | 在进度条右侧显示百分比                                       | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| border-radius   | number/string | 0         | 否           | 圆角大小                                                     | [2.3.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| font-size       | number/string | 16        | 否           | 右侧百分比字体大小                                           | [2.3.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| stroke-width    | number/string | 6         | 否           | 进度条线的宽度                                               | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| color           | string        | #09BB07   | 否           | 进度条颜色（请使用activeColor）                              | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| activeColor     | string        | #09BB07   | 否           | 已选择的进度条的颜色                                         | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| backgroundColor | string        | #EBEBEB   | 否           | 未选择的进度条的颜色                                         | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| active          | boolean       | false     | 否           | 进度条从左往右的动画                                         | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| active-mode     | string        | backwards | 否           | backwards: 动画从头播；forwards：动画从上次结束点接着播      | [1.7.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| duration        | number        | 30        | 否           | 进度增加1%所需毫秒数                                         | [2.8.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| bindactiveend   | eventhandle   | 否        | 动画完成事件 | [2.4.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |                                                              |

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/progress.html#%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81) 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/Oga4Hcmj6cYS "在开发者工具中预览效果")

```xml
<view class="progress-box">
  <progress percent="20" show-info stroke-width="3"/>
</view>

<view class="progress-box">
  <progress percent="40" active stroke-width="3" />
  <icon class="progress-cancel" type="cancel"></icon>
</view>

<view class="progress-box">
  <progress percent="60" active stroke-width="3" />
</view>

<view class="progress-box">
  <progress percent="80" color="#10AEFF" active stroke-width="3" />
</view>
```