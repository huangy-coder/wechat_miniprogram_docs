# InnerAudioContext.onError(function listener)

> 官方文档：[InnerAudioContext.onError(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.onError.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / InnerAudioContext / InnerAudioContext.onError
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：支持

## 功能描述

监听音频播放错误事件

## 参数

### function listener

音频播放错误事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string |   |
| errCode | number |   |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 10001 | 系统错误 |
| 10002 | 网络错误 |
| 10003 | 文件错误 |
| 10004 | 格式错误 |
| -1 | 未知错误 |

## Tips

1. errCode=100001 时，如若 errMsg 中有 INNERCODE -11828 ，请先检查 response header 是否缺少 Content-Length
2. errCode=100001 时，如若 errMsg 中有 systemErrCode:200333420，请检查文件编码格式和 fileExtension 是否一致
