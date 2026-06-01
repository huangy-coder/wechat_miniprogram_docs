# Interface: IComponentSchema

> 官方文档：[Interface: IComponentSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IComponentSchema.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IComponentSchema
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IComponentSchema

`Component`属性的注解接口。

`key`是可以写在组件对应于`xml`中的属性的名字。
`type`是属性的类型，由[registerDataValue](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#registerDataValue)注册。
可选的`defaultValue`可以定义默认值。

## Indexable

▪ [key: `string`]: { `defaultValue?`: `any` ; `type`: `string` }
