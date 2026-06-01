# Interface: IRealDownloader

> 官方文档：[Interface: IRealDownloader](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IRealDownloader.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IRealDownloader
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IRealDownloader

外部需要注入的下载器接口。

## Table of contents

### Methods

- [load](IRealDownloader.md)

## Methods

### load

▸ **load**(`options`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `options` | `Object` |
| `options.onError` | (`error`: `Error`) => `void` |
| `options.onLoad` | (`res`: { `data`: `ArrayBuffer` ; `filePath`: `string` }) => `void` |
| `options.encoding` | `"binary"` \| `"utf-8"` |
| `options.src` | `string` |

#### Returns

`void`
