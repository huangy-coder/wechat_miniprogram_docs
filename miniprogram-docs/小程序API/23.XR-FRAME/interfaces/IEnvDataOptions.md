# Interface: IEnvDataOptions

> 官方文档：[Interface: IEnvDataOptions](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IEnvDataOptions.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IEnvDataOptions
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IEnvDataOptions

`EnvData`的参数接口。

## Table of contents

### Properties

- [diffuse](IEnvDataOptions.md)
- [skybox](IEnvDataOptions.md)
- [specular](IEnvDataOptions.md)

## Properties

### diffuse

• `Optional` **diffuse**: `Object`

环境漫反射部分。

#### Type declaration

| Name | Type | Description |
| --- | --- | --- |
| `coefficients` | `Float32Array` | 球谐系数SH9。 |


### skybox

• `Optional` **skybox**: `Object`

天空盒。

#### Type declaration

| Name | Type | Description |
| --- | --- | --- |
| `half` | `boolean` | 是否只使用贴图的上半部分，一般在和`specular`共用贴图的时候为`true`。 |
| `map` | `default` | 贴图。 |


### specular

• `Optional` **specular**: `Object`

环境高光反射部分。

#### Type declaration

| Name | Type | Description |
| --- | --- | --- |
| `map` | `default` | 贴图。 |
| `mipmapCount?` | `number` | 使用的mipmap级数。 |
| `mipmaps` | `boolean` | 是否使用mipmap。 |
| `rgbd` | `boolean` | 是否使用`rgbd`编码来。 |
| `type` | `"2D"` | 贴图类型，目前只支持2D。 |
