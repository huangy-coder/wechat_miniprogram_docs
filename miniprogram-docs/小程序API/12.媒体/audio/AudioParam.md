# AudioParam

> 官方文档：[AudioParam](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioParam.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / AudioParam
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.19.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

AudioParam 接口代表音频相关的参数，通常是 AudioNode（例如 GainNode.gain）的参数

## 属性

### number defaultValue

代表被具体的 AudioNode 创建的 AudioParam 的属性的初始值（只读）

### number maxValue

代表参数有效范围的最大可能值（只读）

### number minValue

代表参数有效范围的最小可能值（只读）

### number value

当前属性的值（比如音量值或播放倍速值）（可读可写）
