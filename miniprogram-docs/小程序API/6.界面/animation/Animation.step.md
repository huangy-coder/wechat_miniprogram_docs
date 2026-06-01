# Animation Animation.step(Object object)

> 官方文档：[Animation Animation.step(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.step.html)
> 所属分类：[界面](../界面目录.md)
> 导航路径：界面 / 动画 / Animation / Animation.step
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持

> 相关文档: [动画](https://developers.weixin.qq.com/miniprogram/dev/framework/view/animation.html)

## 功能描述

表示一组动画完成。可以在一组动画中调用任意多个动画方法，一组动画中的所有动画会同时开始，一组动画完成后才会进行下一组动画。

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

animation
