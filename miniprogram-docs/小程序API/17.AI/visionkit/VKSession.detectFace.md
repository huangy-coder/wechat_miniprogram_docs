# VKSession.detectFace(Object object)

> 官方文档：[VKSession.detectFace(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.detectFace.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / 视觉算法 / VKSession / VKSession.detectFace
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.25.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.25.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

静态图像人脸关键点检测。当 wx.createVKSession 参数传入 {track: {face: {mode: 2} } } 时可用。用法详情[指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/face.html)。安卓微信8.0.25开始支持，iOS微信8.0.24开始支持。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| frameBuffer | ArrayBuffer |   | 是 | 人脸图像像素点数据，每四项表示一个像素点的 RGBA |
| width | number |   | 是 | 图像宽度 |
| height | number |   | 是 | 图像高度 |
| scoreThreshold | number | 0.8 | 否 | 评分阈值。正常情况传入 0.8 即可。 |
| sourceType | number | 1 | 否 | 图像源类型。正常情况传入 1 即可。当输入的图片是来自一个连续视频的每一帧图像时，sourceType 传入 0 会得到更优的效果 |
| modelModel | number | 1 | 否 | 算法模型类型。正常情况传入 1 即可。0、1、2 分别表示小、中、大模型，模型越大识别准确率越高，但资源占用也越高。建议根据用户设备性能进行选择。 |
| pupilInfo | boolean | false | 否 | 是否返回瞳孔周围点信息，默认为 false。 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 1 | 表示输入的图片是随机的图片 |
| 0 | 表示输入的图片是来自一个连续视频的每一帧图像 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 0 | 小模型 |
| 1 | 中模型 |
| 2 | 大模型 |

### 特别说明

若小程序人脸识别功能涉及采集、存储用户生物特征（如人脸照片或视频、身份证和手持身份证、身份证照和免冠照等），此类型服务需使用[微信原生人脸识别接口](https://developers.weixin.qq.com/community/develop/doc/000442d352c1202bd498ecb105c00d?highline=%E4%BA%BA%E8%84%B8%E6%A0%B8%E8%BA%AB)。
