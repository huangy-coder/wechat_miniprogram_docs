# Enumeration: EShadowFitMode

> 官方文档：[Enumeration: EShadowFitMode](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/enums/EShadowFitMode.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Enumerations / EShadowFitMode
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / EShadowFitMode

阴影匹配类型枚举。

## Table of contents

### Enumeration members

- [FitFrustum](EShadowFitMode.md)
- [FitObjects](EShadowFitMode.md)

## Enumeration members

### FitFrustum

• **FitFrustum** = `0`

阴影范围适配视锥体。
更稳定，可能降低阴影精度。


### FitObjects

• **FitObjects** = `1`

阴影范围适配物体。
能提高阴影精度，但可能会导致阴影不稳定。
