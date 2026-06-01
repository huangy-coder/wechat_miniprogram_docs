# Interface: IGLTFLoaderOptions

> 官方文档：[Interface: IGLTFLoaderOptions](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IGLTFLoaderOptions.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IGLTFLoaderOptions
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IGLTFLoaderOptions

## Table of contents

### Properties

- [ignoreError](IGLTFLoaderOptions.md)
- [preserveRaw](IGLTFLoaderOptions.md)

## Properties

### ignoreError

• **ignoreError**: `number`[]

*(基础库2.31.1及之后)*
可以忽略xr-frame对GLTF模型的某一些限制，来强行渲染有问题的GLTF模型。
ErrorCode会在渲染模型失败后，由console报出。
填写-1则忽略所有限制。


### preserveRaw

• **preserveRaw**: `boolean`

*(基础库2.32.1及之后)*
开启了之后会在GLTFModel中保留原始json。
