# Interface: IEntityComponents

> 官方文档：[Interface: IEntityComponents](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IEntityComponents.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IEntityComponents
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IEntityComponents

`Element`的默认组件集接口。

`name`是组件注册时的名字，`key`是要默认设置的组件的属性名字，值是默认值，但应当和`xml`中一致，为**字符串**。

## Indexable

▪ [name: `string`]: { `[key: string]`: `string`; }
