# Interface: ILightData

> 官方文档：[Interface: ILightData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ILightData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / ILightData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / ILightData

[Light](../classes/Light.md)组件数据接口。

## Table of contents

### Properties

- [castShadow](ILightData.md)
- [color](ILightData.md)
- [innerConeAngle](ILightData.md)
- [intensity](ILightData.md)
- [outerConeAngle](ILightData.md)
- [range](ILightData.md)
- [shadowBias](ILightData.md)
- [shadowDistance](ILightData.md)
- [type](ILightData.md)

## Properties

### castShadow

• `Optional` **castShadow**: `boolean`

是否要产生阴影，仅对平行光有效。
`xml`中的数据类型`boolean`，默认为`false`。


### color

• **color**: `number`[]

颜色。
`xml`中的数据类型`color`，默认为`[1, 1, 1, 1]`。


### innerConeAngle

• **innerConeAngle**: `number`

仅在聚光有效。
`xml`中的数据类型`number`，默认为`1`。


### intensity

• **intensity**: `number`

强度。
`xml`中的数据类型`number`，默认为`1`。


### outerConeAngle

• **outerConeAngle**: `number`

仅在聚光有效。
`xml`中的数据类型`number`，默认为`1`。


### range

• **range**: `number`

范围，仅在点光和聚光有效。
`xml`中的数据类型`number`，默认为`1`。


### shadowBias

• `Optional` **shadowBias**: `number`

阴影采样时的容许偏移，仅对平行光有效。
`xml`中的数据类型`number`，默认为`0.002`。


### shadowDistance

• `Optional` **shadowDistance**: `number`

产生阴影的最大距离，仅对平行光有效。
`xml`中的数据类型`number`，默认为`10`。


### type

• **type**: `ELightType`

类型。
`xml`中的数据类型`string`，默认为`directional`。
