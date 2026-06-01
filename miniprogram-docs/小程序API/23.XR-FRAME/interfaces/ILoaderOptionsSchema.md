# Interface: ILoaderOptionsSchema

> 官方文档：[Interface: ILoaderOptionsSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/ILoaderOptionsSchema.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / ILoaderOptionsSchema
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / ILoaderOptionsSchema

指定继承自[AssetLoader](../classes/AssetLoader.md)的自定义资源加载器，可以接受的的额外配置的`schema`。
在基础库版本**v2.29.2**以上导出。

比如使用[CubeTextureLoader](../classes/CubeTextureLoader.md)加载资源时：

```xml
<xr-asset-load
  type="cube-texture" asset-id="sky-cube" src="/assets/textures/skybox/"
  options="faces: right.jpg left.jpg top.jpg bottom.jpg front.jpg back.jpg"
/>
```

对应的`schema`接口为：

```ts
export interface ICubeTextureLoaderOptions {
  // left right top bottom front back
  faces: string[];
}
```ts

对应的`schema`为：
```ts
schema = {
  faces: {type: 'array'}
};
```

## Indexable

▪ [key: `string`]: { `defaultValue?`: `any` ; `type`: `string` }
