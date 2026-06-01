# Interface: IEngineSettings

> 官方文档：[Interface: IEngineSettings](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IEngineSettings.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IEngineSettings
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IEngineSettings

index.ts

**`author`** : hikaridai(hikaridai@tencent.com)

**`date`** : 2020/8/18 下午4:48:36

## Table of contents

### Properties

- [alpha](IEngineSettings.md)
- [audio](IEngineSettings.md)
- [backupURLs](IEngineSettings.md)
- [baseURL](IEngineSettings.md)
- [cacheDelimiter](IEngineSettings.md)
- [cacheSizeLimit](IEngineSettings.md)
- [designHeight](IEngineSettings.md)
- [designWidth](IEngineSettings.md)
- [fixedDeltaTime](IEngineSettings.md)
- [gfxIgnoreAssert](IEngineSettings.md)
- [globalHTTPRetry](IEngineSettings.md)
- [gravity](IEngineSettings.md)
- [logFilter](IEngineSettings.md)
- [logLevel](IEngineSettings.md)
- [mainScreenMSAA](IEngineSettings.md)
- [physics3DLayerCollisionMatrix](IEngineSettings.md)
- [profileGfx](IEngineSettings.md)
- [realSizeLimit](IEngineSettings.md)
- [renderHeight](IEngineSettings.md)
- [renderWidth](IEngineSettings.md)
- [shaderGlobalProperties](IEngineSettings.md)
- [useEngineSubcontext](IEngineSettings.md)
- [workerPath](IEngineSettings.md)
- [workerTimeout](IEngineSettings.md)

## Properties

### alpha

• `Optional` **alpha**: `boolean`

是否开启透明通道输出


### audio

• `Optional` **audio**: `Object`

音频全局定义

#### Type declaration

| Name | Type | Description |
| --- | --- | --- |
| `globalVolume?` | `number` | 全局音量 |
| `maxRealVoices?` | `number` | 真实音频数量上限 |


### backupURLs

• **backupURLs**: `string`[]

如果baseURL找不到并且重试次数`globalHTTPRetry`大于0，则会依次尝试使用


### baseURL

• **baseURL**: `string`

loader下载文件的默认根路径


### cacheDelimiter

• **cacheDelimiter**: `string`

拼缓存的文件名的


### cacheSizeLimit

• **cacheSizeLimit**: `number`

最大缓存极限


### designHeight

• **designHeight**: `number`

设计分辨率高


### designWidth

• **designWidth**: `number`

设计分辨率宽


### fixedDeltaTime

• **fixedDeltaTime**: `number`

物理引擎的模拟步进固定间隔


### gfxIgnoreAssert

• **gfxIgnoreAssert**: `boolean`


### globalHTTPRetry

• **globalHTTPRetry**: `string`

全局loader下载文件重试次数


### gravity

• **gravity**: `number`

物理引擎的重力


### logFilter

• **logFilter**: `boolean`

log过滤器


### logLevel

• **logLevel**: `string`

log等级


### mainScreenMSAA

• **mainScreenMSAA**: `boolean`

是否开启MSAA


### physics3DLayerCollisionMatrix

• **physics3DLayerCollisionMatrix**: `string`

物理碰撞矩阵，以十六进制字符串表示


### profileGfx

• **profileGfx**: `string`


### realSizeLimit

• **realSizeLimit**: `number`

是否开启MSAA


### renderHeight

• **renderHeight**: `number`

渲染分辨率高


### renderWidth

• **renderWidth**: `number`

渲染分辨率宽


### shaderGlobalProperties

• **shaderGlobalProperties**: { `default`: `string` | `number` | `number`[] ; `key`: `string` ; `type`: `"Float"` | `"Vector2"` | `"Vector3"` | `"Vector4"` | `"Matrix4"` | `"Texture"` }[]

全局Uniform定义


### useEngineSubcontext

• **useEngineSubcontext**: `boolean`


### workerPath

• **workerPath**: `string`

自动生成的worker文件入口路径


### workerTimeout

• **workerTimeout**: `number`

worker执行任务超时时间
