WXML 语法参考 /介绍

WXML（WeiXin Markup Language）是框架设计的一套标签语言，结合[基础组件](https://developers.weixin.qq.com/miniprogram/dev/component/index.html)、[事件系统](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/event.html)，可以构建出页面的结构。

用以下一些简单的例子来看看 WXML 具有什么能力：

## [数据绑定](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/data.html)

```php-template
<!--wxml-->
<view> {{message}} </view>
```

```css
// page.js
Page({
  data: {
    message: 'Hello MINA!'
  }
})
```

## [列表渲染](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/list.html)

```php-template
<!--wxml-->
<view wx:for="{{array}}"> {{item}} </view>
```

```css
// page.js
Page({
  data: {
    array: [1, 2, 3, 4, 5]
  }
})
```

## [条件渲染](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/conditional.html)

```php-template
<!--wxml-->
<view wx:if="{{view == 'WEBVIEW'}}"> WEBVIEW </view>
<view wx:elif="{{view == 'APP'}}"> APP </view>
<view wx:else="{{view == 'MINA'}}"> MINA </view>
```

```css
// page.js
Page({
  data: {
    view: 'MINA'
  }
})
```

## [模板](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/template.html)

```php-template
<!--wxml-->
<template name="staffName">
  <view>
    FirstName: {{firstName}}, LastName: {{lastName}}
  </view>
</template>

<template is="staffName" data="{{...staffA}}"></template>
<template is="staffName" data="{{...staffB}}"></template>
<template is="staffName" data="{{...staffC}}"></template>
```

```php
// page.js
Page({
  data: {
    staffA: {firstName: 'Hulk', lastName: 'Hu'},
    staffB: {firstName: 'Shang', lastName: 'You'},
    staffC: {firstName: 'Gideon', lastName: 'Lin'}
  }
})
```

具体的能力以及使用方式在以下章节查看：

[数据绑定](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/data.html)、[列表渲染](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/list.html)、[条件渲染](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/conditional.html)、[模板](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/template.html)、[引用](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/import.html)