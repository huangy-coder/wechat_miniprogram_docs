# Interface: IEnvData

> 官方文档：[Interface: IEnvData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IEnvData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IEnvData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IEnvData

[Env](../classes/Env.md)组件数据接口。

## Table of contents

### Properties

- [diffuseExp](IEnvData.md)
- [envData](IEnvData.md)
- [isSky2D](IEnvData.md)
- [rotation](IEnvData.md)
- [skyMap](IEnvData.md)
- [specularExp](IEnvData.md)

## Properties

### diffuseExp

• **diffuseExp**: `number`

漫反射部分曝光。
`xml`中的数据类型为`number`，默认为`1`。


### envData

• `Optional` **envData**: [`EnvData`](../classes/EnvData.md)

要使用的环境数据资源。
`xml`中的数据类型为`env-data`资源。


### isSky2D

• `Optional` **isSky2D**: `boolean`

是否用2D模式渲染天空盒，此时必须为`skyMap`必须**不**为`CubeTexture`。


### rotation

• **rotation**: `number`

环境旋转角度。
`xml`中的数据类型为`number`，默认为`0`。


### skyMap

• `Optional` **skyMap**: `default` | [`ITextureWrapper`](ITextureWrapper.md)

可以用于覆盖`envData`中的`skybox`。
`xml`中的数据类型为`texture`资源。


### specularExp

• **specularExp**: `number`

镜面反射部分曝光。
`xml`中的数据类型为`number`，默认为`1`。
