# Interface: IFeatures

> 官方文档：[Interface: IFeatures](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IFeatures.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IFeatures
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IFeatures

渲染层提供的特性列表。

## Table of contents

### Properties

- [colorBufferFloat](IFeatures.md)
- [depthTexture](IFeatures.md)
- [dynamicBatch3D](IFeatures.md)
- [fragDepth](IFeatures.md)
- [gpuInstance](IFeatures.md)
- [srgb](IFeatures.md)
- [textureAnisotropic](IFeatures.md)
- [textureFloat](IFeatures.md)
- [textureHalfFloat](IFeatures.md)

## Properties

### colorBufferFloat

• **colorBufferFloat**: `boolean`

是否支持浮点类型的颜色缓冲。


### depthTexture

• **depthTexture**: `boolean`

是否支持深度纹理。


### dynamicBatch3D

• **dynamicBatch3D**: `boolean`

是否支持3D动态合批。


### fragDepth

• **fragDepth**: `boolean`

是否支持在片段着色器采样深度。


### gpuInstance

• **gpuInstance**: `boolean`

是否支持GPU实例化。


### srgb

• **srgb**: `boolean`

是否支持硬件SRGB解码。


### textureAnisotropic

• **textureAnisotropic**: `boolean`

是否支持各向异性滤波。


### textureFloat

• **textureFloat**: `boolean`

是否支持浮点纹理。


### textureHalfFloat

• **textureHalfFloat**: `boolean`

是否支持半精度浮点纹理。
