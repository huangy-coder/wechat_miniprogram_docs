# Interface: ITextData

> 官方文档：[Interface: ITextData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ITextData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / ITextData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / ITextData

`Text`数据接口。

## Table of contents

### Properties

- [anchor](ITextData.md)
- [color](ITextData.md)
- [height](ITextData.md)
- [horzAlign](ITextData.md)
- [lineHeight](ITextData.md)
- [neverCull](ITextData.md)
- [padding](ITextData.md)
- [size](ITextData.md)
- [states](ITextData.md)
- [uniforms](ITextData.md)
- [value](ITextData.md)
- [vertAlign](ITextData.md)
- [width](ITextData.md)

## Properties

### anchor

• `Optional` **anchor**: `number`[]

文本轴点
`xml`中的数据类型为`number-array`，默认为`0 1`。


### color

• `Optional` **color**: `number`[]

文本颜色
`xml`中的数据类型为`number-array`，默认为`0 0 0 1`。


### height

• `Optional` **height**: `number`

文本框高度
`xml`中的数据类型为`number`


### horzAlign

• `Optional` **horzAlign**: `string`

文本水平定位
`xml`中的数据类型为`string`，默认为`left`。


### lineHeight

• `Optional` **lineHeight**: `number`

文本框行高，为比例
`xml`中的数据类型为`number`


### neverCull

• `Optional` **neverCull**: `boolean`

是否不参与剔除，默认false(即参与剔除)。


### padding

• `Optional` **padding**: `number`[]

文本内边距
`xml`中的数据类型为`number-array`，默认为`0 0 0`。


### size

• `Optional` **size**: `number`

文本大小
`xml`中的数据类型为`number`


### states

• `Optional` **states**: [`string`, `string`][]

覆盖`material`中的默认`states`，如果覆盖了，则会先创建一个材质副本。
`xml`中同{@link IMaterialData.states}。


### uniforms

• `Optional` **uniforms**: [`string`, `string`][]

覆盖`material`中的默认`uniforms`，如果覆盖了，则会先创建一个材质副本。
`xml`中同{@link IMaterialData.uniforms}。


### value

• `Optional` **value**: `string`

文本内容
`xml`中的数据类型为`string`


### vertAlign

• `Optional` **vertAlign**: `string`

文本垂直定位
`xml`中的数据类型为`string`，默认为`top`。


### width

• `Optional` **width**: `number`

文本框宽度
`xml`中的数据类型为`number`
