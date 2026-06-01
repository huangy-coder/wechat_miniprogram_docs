# Interface: IDownloader

> 官方文档：[Interface: IDownloader](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IDownloader.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IDownloader
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IDownloader

下载器。

## Table of contents

### Properties

- [REAL_DOWNLOADER](IDownloader.md)
- [inWX](IDownloader.md)

### Methods

- [LOAD](IDownloader.md)

## Properties

### REAL_DOWNLOADER

• **REAL_DOWNLOADER**: [`IRealDownloader`](IRealDownloader.md)


### inWX

• **inWX**: `boolean`

## Methods

### LOAD

▸ **LOAD**(`options`): `void`

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
