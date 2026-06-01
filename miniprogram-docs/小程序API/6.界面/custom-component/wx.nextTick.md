# wx.nextTick(function callback)

> 官方文档：[wx.nextTick(function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/custom-component/wx.nextTick.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 自定义组件 / wx.nextTick
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.2.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.7.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

延迟一部分操作到下一个时间片再执行。（类似于 setTimeout）

## 参数

### function callback

## 说明

因为自定义组件中的 setData 和 triggerEvent 等接口本身是同步的操作，当这几个接口被连续调用时，都是在一个同步流程中执行完的，因此若逻辑不当可能会导致出错。

一个极端的案例：当父组件的 setData 引发了子组件的 triggerEvent，进而使得父组件又进行了一次 setData，期间有通过 wx:if 语句对子组件进行卸载，就有可能引发奇怪的错误，所以对于不需要在一个同步流程内完成的逻辑，可以使用此接口延迟到下一个时间片再执行。

## 示例代码

```js
Component({
  doSth() {
    this.setData({ number: 1 }) // 直接在当前同步流程中执行

    wx.nextTick(() => {
      this.setData({ number: 3 }) // 在当前同步流程结束后，下一个时间片执行
    })

    this.setData({ number: 2 }) // 直接在当前同步流程中执行
  }
})
```
