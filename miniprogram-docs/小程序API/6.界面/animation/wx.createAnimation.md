# Animation wx.createAnimation(Object object)

> 官方文档：[Animation wx.createAnimation(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/wx.createAnimation.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 动画 / wx.createAnimation
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持，需要小程序基础库版本不低于 [1.9.6](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [动画](https://developers.weixin.qq.com/miniprogram/dev/framework/view/animation.html)

## 功能描述

创建一个动画实例 [animation](Animation.md)。调用实例的方法来描述动画。最后通过动画实例的 export 方法导出动画数据传递给组件的 animation 属性。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 400 | 否 | 动画持续时间，单位 ms |
| timingFunction | string | 'linear' | 否 | 动画的效果 |
| delay | number | 0 | 否 | 动画延迟时间，单位 ms |
| transformOrigin | string | '50% 50% 0' | 否 |   |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 'linear' | 动画从头到尾的速度是相同的 |
| 'ease' | 动画以低速开始，然后加快，在结束前变慢 |
| 'ease-in' | 动画以低速开始 |
| 'ease-in-out' | 动画以低速开始和结束 |
| 'ease-out' | 动画以低速结束 |
| 'step-start' | 动画第一帧就跳至结束状态直到结束 |
| 'step-end' | 动画一直保持开始状态，最后一帧跳到结束状态 |

## 返回值

### Animation
