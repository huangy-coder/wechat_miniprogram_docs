# Class: VideoTexture

> 官方文档：[Class: VideoTexture](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/VideoTexture.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / VideoTexture
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / VideoTexture

视频纹理。

## Table of contents

### Constructors

- [constructor](VideoTexture.md)

### Properties

- [onEnd](VideoTexture.md)

### Accessors

- [autoPause](VideoTexture.md)
- [height](VideoTexture.md)
- [state](VideoTexture.md)
- [texture](VideoTexture.md)
- [width](VideoTexture.md)

### Methods

- [pause](VideoTexture.md)
- [play](VideoTexture.md)
- [release](VideoTexture.md)
- [resume](VideoTexture.md)
- [seek](VideoTexture.md)
- [stop](VideoTexture.md)

## Constructors

### constructor

• **new VideoTexture**(`scene`, `options`, `onReady`, `onEnd?`)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `scene` | [`Scene`](Scene.md) | - |
| `options` | [`IVideoTextureOptions`](../interfaces/IVideoTextureOptions.md) | - |
| `onReady` | (`vt`: [`VideoTexture`](VideoTexture.md), `error?`: `Error`) => `void` | 创建成功时的回调。 |
| `onEnd?` | () => `void` | 播放结束时的回调。 |

## Properties

### onEnd

• `Optional` **onEnd**: () => `void`

#### Type declaration

▸ (): `void`

##### Returns

`void`

## Accessors

### autoPause

• `get` **autoPause**(): `boolean`

#### Returns

`boolean`


### height

• `get` **height**(): `number`

#### Returns

`number`


### state

• `get` **state**(): [`EVideoState`](../enums/EVideoState.md)

当前视频纹理播放状态。

#### Returns

[`EVideoState`](../enums/EVideoState.md)


### texture

• `get` **texture**(): `default`

#### Returns

`default`


### width

• `get` **width**(): `number`

#### Returns

`number`

## Methods

### pause

▸ **pause**(): `Promise`<`void`>

暂停当前播放的视频。
需要在基础库`v2.33.0`及以上支持。

#### Returns

`Promise`<`void`>


### play

▸ **play**(): `Promise`<`void`>

播放视频。

#### Returns

`Promise`<`void`>


### release

▸ **release**(): `void`

释放视频。

#### Returns

`void`


### resume

▸ **resume**(): `Promise`<`void`>

唤醒已暂停的视频。
需要在基础库`v2.33.0`及以上支持。

#### Returns

`Promise`<`void`>


### seek

▸ **seek**(`pos`): `Promise`<`any`>

从某处开始播放。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `pos` | `number` | 事件，单位为s |

#### Returns

`Promise`<`any`>


### stop

▸ **stop**(): `void`

停止播放视频。

#### Returns

`void`
