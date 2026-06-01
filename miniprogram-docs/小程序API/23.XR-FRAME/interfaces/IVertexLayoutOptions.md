# Interface: IVertexLayoutOptions

> 官方文档：[Interface: IVertexLayoutOptions](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IVertexLayoutOptions.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IVertexLayoutOptions
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IVertexLayoutOptions

顶点布局解构初始化参数。

## Table of contents

### Properties

- [attributes](IVertexLayoutOptions.md)
- [step](IVertexLayoutOptions.md)
- [stepRate](IVertexLayoutOptions.md)
- [stride](IVertexLayoutOptions.md)

## Properties

### attributes

• **attributes**: { `format`: [`EVertexFormat`](../enums/EVertexFormat.md) ; `name`: `string` ; `offset`: `number` ; `usage`: [`EVertexLayoutUsage`](../enums/EVertexLayoutUsage.md) }[]

顶点属性列表。


### step

• `Optional` **step**: [`EVertexStep`](../enums/EVertexStep.md)

步进类型。

**`default`** EVertexStep.PER_VERTEX


### stepRate

• `Optional` **stepRate**: `number`

步进单位。

**`default`** 1


### stride

• `Optional` **stride**: `number`

步长，不设定会自动计算。
