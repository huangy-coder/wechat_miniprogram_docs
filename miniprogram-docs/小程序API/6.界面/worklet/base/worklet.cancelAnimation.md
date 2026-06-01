# worklet.cancelAnimation(SharedValue SharedValue)

> 官方文档：[worklet.cancelAnimation(SharedValue SharedValue)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/base/worklet.cancelAnimation.html)
> 所属分类：[界面](../../界面目录.md)
> 导航路径：界面 / worklet 动画 / 基础 / worklet.cancelAnimation
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

> 相关文档: [worklet 动画](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/worklet.html)

## 功能描述

取消由 `SharedValue` 驱动的动画。

## 参数

### SharedValue SharedValue

共享变量。

## 示例代码

```javascript
const { shared, timing, cancelAnimation } = wx.worklet
const offset = shared(0);
offset.value = timing(100);
cancelAnimation(offset)
```
